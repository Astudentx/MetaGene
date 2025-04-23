import sys

def main():
    # 检查命令行参数
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} species.txt ppm.gene.txt1 ppm.gene.txt2")
        sys.exit(1)

    species_file = sys.argv[1]
    gene_file = sys.argv[2]
    output_file = sys.argv[3]

    # 读取物种信息
    species = {}
    with open(species_file, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                species[parts[0]] = parts[1]

    # 处理基因列表并添加物种信息
    with open(gene_file, 'r') as fin, open(output_file, 'w') as fout:
        header = fin.readline().strip()
        columns = header.split('\t')
        # 写入新的表头
        fout.write("Gene\tSubtype\tType\tSpecies\t" + "\t".join(columns[3:]) + "\n")

        for line in fin:
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                gene_id = parts[0]
                species_name = species.get(gene_id, "Unknown")  # 如果找不到物种信息，使用"Unknown"
                # 写入新的行
                fout.write(f"{parts[0]}\t{parts[1]}\t{parts[2]}\t{species_name}\t" + "\t".join(parts[3:]) + "\n")

if __name__ == "__main__":
    main()