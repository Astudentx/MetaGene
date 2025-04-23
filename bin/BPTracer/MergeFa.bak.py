import os
import subprocess
from metaGene import config

def read_metadata(meta_data_in, meta_data_out):
    sampleid = {}
    metainfo = {}
    samplerlen = {}

    with open(meta_data_in, 'r') as f:
        header = f.readline().strip()
        with open(meta_data_out, 'w') as meta_out:
            meta_out.write(f"{header}\t#ofReads\t#of16Sreads\tCellNumber\n")
            for line in f:
                tm = line.strip().split("\t")
                sampleid[tm[0]] = tm[1]
                samplerlen[tm[0]] = int(tm[3])
                metainfo[tm[0]] = line.strip()
    return sampleid, metainfo, samplerlen

def parse_coglist(coglist):
    seq2OGs = {}
    seqlen = {}
    with open(coglist, 'r') as f:
        for line in f:
            tem = line.strip().split("\t")
            if len(tem) >= 3 and tem[0] and tem[1] and tem[2].isdigit():
                seq2OGs[tem[0]] = tem[1]
                seqlen[tem[0]] = int(tem[2])
    return seq2OGs, seqlen

def count_reads(indir, sample):
    file1 = os.path.join(indir, f"{sample}_1.fa")
    file2 = os.path.join(indir, f"{sample}_2.fa")
    if os.path.exists(file1) and os.path.exists(file2):
        num1 = int(subprocess.getoutput(f"grep '>' {file1} -c"))
        num2 = int(subprocess.getoutput(f"grep '>' {file2} -c"))
        return num1 + num2
    else:
        raise RuntimeError(f"Input files missing for sample {sample}!")

def count_16s_reads(outdir, sample, samplerlen):
    sam_file = os.path.join(outdir, f"{sample}.sam")
    if os.path.exists(sam_file):
        num_16s = int(subprocess.getoutput(f"{config.BP_SAMTOOLS_SOFTWARE} view -f 3 {sam_file} | wc -l"))
        return num_16s * samplerlen / 1432
    else:
        raise RuntimeError(f"SAM file missing for sample {sample}!")

def estimate_cell_number(outdir, sample, seq2OGs, seqlen):
    blastx_file = os.path.join(outdir, f"{sample}.uscmg.blastx.txt")
    ko_averagecov_file = os.path.join(outdir, f"{sample}.uscmg.ko_averagecov.txt")

    if os.path.exists(blastx_file):
        seqcov = {}
        with open(blastx_file, 'r') as f:
            for line in f:
                tem = line.strip().split("\t")
                seqcov[tem[1]] = seqcov.get(tem[1], 0) + float(tem[3])

        kocov = {}
        for sid, coverage in seqcov.items():
            if sid in seq2OGs:
                og = seq2OGs[sid]
                if og not in kocov:
                    kocov[og] = {}
                kocov[og][sid] = kocov[og].get(sid, 0) + coverage

        avgKOcopy = 0
        KOcount = 0
        with open(ko_averagecov_file, 'w') as ko_out:
            for og, seq_coverage in kocov.items():
                seqnum = len(seq_coverage)
                ave = sum(cov / seqlen[sid] for sid, cov in seq_coverage.items())
                ko_out.write(f"{og}\t{ave:.6f}\t{seqnum}\n")
                avgKOcopy += ave
                KOcount += 1

        if KOcount == 0:
            raise RuntimeError("No KO mapping found!")

        return avgKOcopy / KOcount
    else:
        raise RuntimeError("BLASTx file missing!")

def merge_fasta(outdir, sample, extracted_fasta):
    # 定义输入文件路径
    extract1 = os.path.join(outdir, f"{sample}.extract_1.fa")
    extract2 = os.path.join(outdir, f"{sample}.extract_2.fa")

    # 如果输出文件已存在，先删除
    if os.path.exists(extracted_fasta):
        os.remove(extracted_fasta)

    # 检查输入文件是否存在
    if not (os.path.exists(extract1) and os.path.exists(extract2)):
        raise RuntimeError(f"Missing files: {extract1 if not os.path.exists(extract1) else extract2}")

    # 合并文件内容
    count = 1
    with open(extracted_fasta, 'w') as out_fasta:
        for file_path in [extract1, extract2]:
            with open(file_path, 'r') as f:
                for header in f:
                    sequence = next(f).strip()
                    out_fasta.write(f">{sample}_{count}\n{sequence}\n")
                    count += 1


def update_metadata(meta_data_out, metainfo, sampleid, hashreads, hash16s, cellnum):
    with open(meta_data_out, 'a') as meta_out:
        for id in sorted(metainfo.keys(), key=int):
            meta_out.write(f"{metainfo[id]}\t{hashreads[sampleid[id]]}\t"
                           f"{hash16s[sampleid[id]]:.6f}\t{cellnum[sampleid[id]]:.6f}\n")

def main(indir, outdir, meta_data_in, meta_data_out, extracted_fasta, coglist):
    sampleid, metainfo, samplerlen = read_metadata(meta_data_in, meta_data_out)
    seq2OGs, seqlen = parse_coglist(coglist)

    hashreads = {}
    hash16s = {}
    cellnum = {}

    for ids in sorted(sampleid.keys(), key=int):
        sample = sampleid[ids]

        hashreads[sample] = count_reads(indir, sample)
        hash16s[sample] = count_16s_reads(outdir, sample, samplerlen[ids])
        cellnum[sample] = estimate_cell_number(outdir, sample, seq2OGs, seqlen)
        merge_fasta(outdir, sample, extracted_fasta)

    update_metadata(meta_data_out, metainfo, sampleid, hashreads, hash16s, cellnum)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 7:
        print("Usage: python script.py <Indir> <Outdir> <Meta_data_in> <Meta_data_out> <Extracted_fasta> <Coglist>")
        sys.exit(1)
    main(*sys.argv[1:])
