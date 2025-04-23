import subprocess
import textwrap
from metaGene import config
from metaGene.BaseRunner import BaseRunner

class MegahitRunner(BaseRunner):
    def build_command(self):
        id = self.params.get('id')
        file1 = self.params.get('file1')
        file2 = self.params.get('file2')

        cmd = textwrap.dedent(rf"""
        cd {config.Megahit_OUTPUT_PATH}
        {config.BIN_PATH}/megahit/megahit -1 {file1} -2 {file2} --min-contig-len 500 -t 40 -o ./{id}
        perl {config.BIN_PATH}/BPTracer/renamefa.pl ./{id}/final.contigs.fa {id} {id}.contig.ok.fa
        perl {config.BIN_PATH}/BPTracer/deal_fa.pl -format 3 {id}.contig.ok.fa | perl -e 'while(<>){{chomp;@a=split; if($a[1] > 10000){{$a[1]=10000;}} print "$a[0]\t$a[1]\n";}}' > {id}.contig.ok.fa.chrlist
        #perl {config.BIN_PATH}/BPTracer/fa_fq_len_bar.pl {id}.contig.ok.fa.chrlist {id}.contig.length.pdf contig
        rm -r {config.Megahit_OUTPUT_PATH}/{id}/
        """)
        return cmd