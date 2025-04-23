import os
import sys

"""Default values for filenames and common constants."""
# ====================== 路径配置 ======================
# 获取主脚本所在目录路径
#MAIN_SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
MAIN_SCRIPT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 指向上一级目录
MAIN_SCRIPT = os.path.join(MAIN_SCRIPT_DIR, "MetaGene.py")  # 主程序路径
CONFIG_SCRIPT = os.path.abspath(__file__) # 默认config路径

# bin与DB子目录路径
BIN_PATH = os.path.join(MAIN_SCRIPT_DIR, 'bin')
DATABASE_PATH = os.path.join(MAIN_SCRIPT_DIR, 'db')

# 输出路径
OUTPUT_PATH = os.getcwd()  # 默认初始化为当前工作目录，防止OUTPUT_PATH无法识别的问题
SHELL_PATH = os.path.join(OUTPUT_PATH, "shell/")  # 初始化路径

def set_output_path(pwd=None):
    global OUTPUT_PATH, SHELL_PATH, SARG_OUTPUT_PATH, Kraken2_OUTPUT_PATH, HGT_OUTPUT_PATH  # 声明全局变量
    global SPAdes_OUTPUT_PATH, Megahit_OUTPUT_PATH, BP_OUTPUT_PATH, BP_TAX_PATH
    if pwd is not None:
        OUTPUT_PATH = os.path.abspath(pwd)  # Use absolute path
    else:
        OUTPUT_PATH = os.getcwd()  # Default to current working directory
    SHELL_PATH = os.path.join(OUTPUT_PATH, "shell/")
    SARG_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "SARG/")
    Kraken2_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "Kraken2/")
    HGT_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "WAAFLE/")
    SPAdes_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "Assamble_SPADde")
    Megahit_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "Assamble_Megahit")
    BP_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "BPTracer")


#"""Mapping software and Functional gene databases"""
#SARG_MAPPING_SOFTWARE = "diamond blastp"
#SARG_DATABASE = os.path.join(os.path.dirname(__file__), 'db/SARG.3.2.fasta')
#SARG_EVALUE = 1e-5
#SARG_MAX_TARGET_SEQS = 10
#SARG_THREADS = 8
#SARG_FORMAT = 6


"""FastqStat software"""
FASTQSTAT_SOFTWARE =  os.path.join(BIN_PATH, 'FastqStat')

"""Kraken2 software and k-mer gene databases"""        
Kraken2_MAPPING_SOFTWARE = os.path.join(BIN_PATH, 'Kraken2')
def set_kraken2_database(database=None):
    global Kraken2_DATABASE, Kraken2_TAXLIST
    if database is None:
        Kraken2_DATABASE = os.path.join(DATABASE_PATH, 'Kraken2/krakenDB-202212')
        Kraken2_TAXLIST = os.path.join(Kraken2_DATABASE, 'tax.list')
    else:
        Kraken2_DATABASE = os.path.join(DATABASE_PATH, "Kraken2", database)
        Kraken2_TAXLIST = os.path.join(Kraken2_DATABASE, 'tax.list')

# 原本的默认参数设置        
# Kraken2_DATABASE = os.path.join(DATABASE_PATH, 'Kraken2/krakenDB-20221209')
# Kraken2_TAXLIST = os.path.join(Kraken2_DATABASE, 'tax.list')
Kraken2_THREADS = 50


"""SPAdes software"""
SPAdes_MAPPING_SOFTWARE = os.path.join(BIN_PATH, 'SPAdes-3.15.3')
SPAdes_THREADS = 140
SPAdes_MEMARY = 400

"""BP-Tracer software and Functional gene databases"""
BP_SAMTOOLS_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/samtools")
BP_DIAMOND_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/diamond blastx")
BP_BLAST_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/blastx")

BP_FQ2FA_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/Fq2fa.pl")
BP_FQ2FA_SOFTWARE2 = "seqtk" # 提供第二种方案1
BP_MINIMAP2 = os.path.join(BIN_PATH,"BPTracer/minimap2")

BP_EXTREA_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/extract_usearch_reads.pl")
# BP_MERGEFA_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/merge_extracted_fa_update_metadate.v2.3.pl")
BP_MERGEFA_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/MergeFa.py")
BP_16S_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/gg85_yinxiaole.fasta.mmi')
BP_USCMG_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/KO30_DIAMOND.dmnd')
BP_USCMG_LIST = os.path.join(DATABASE_PATH, 'BPTracer/Gene/all_KO30_name.list')

"""BP-Tracer Old USCMG databases"""
BP_USCMG_SOFTWARE = os.path.join(BIN_PATH,"BPTracer/diamond0.8.16 blastx")
BP_USCMG_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/KO30_DIAMOND.0.8.16.dmnd')



BP_EXTRACTEDFA_WINDOW = 200000
BP_META_LIBRARY_SIZE = 300
BP_TAX_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/species.info.txt')

BP_ARG_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-ARG.dmnd')
BP_MGE_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-MGE.dmnd')
BP_MRG_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-MRG.dmnd')
BP_VFs_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-VFs.dmnd')
BP_SGs_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-SGs.dmnd')

BP_ARG_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-ARG.list')
BP_MGE_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-MGE.list')
BP_MRG_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-MRG.list')
BP_VFs_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-VFs.list')
BP_SGs_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-SGs.list')

BP_BLASTARG_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-ARG.faa')
BP_BLASTMGE_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-MGE.faa')
BP_BLASTMRG_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-MRG.faa')
BP_BLASTVFs_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-VFs.faa')
BP_BLASTSGs_DATABASE = os.path.join(DATABASE_PATH, 'BPTracer/Gene/Gene-SGs.faa')

BP_ARG_EVALUE = 1e-5
BP_ARG_MAX_TARGET_SEQS = 10
BP_ARG_THREADS = 8
BP_ARG_FORMAT = 6


# BP Profile thresholds
BP_LENGTH_THRESHOLD = 25  
BP_IDENTITY_THRESHOLD = 80  
BP_EVALUE_THRESHOLD = 1E-7


## HGT WAAFLE 参数
## Database and Structure
#BP_HGT_DATABASE  = os.path.join(DATABASE_PATH, 'BPTracer/HGT/WAAFLE/chocophlan2/chocophlan2')
#BP_HGT_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/HGT/WAAFLE/chocophlan2_taxonomy.tsv')
## BP Pangenomes
#BP_HGT_DATABASE  = os.path.join(DATABASE_PATH, 'BPTracer/HGT/RefseqPan/UnigeneSet-waafledb.v2')
#BP_HGT_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/HGT/RefseqPan/UnigeneSet-waafledb.v2.taxonomy')



def set_kraken2_database(database=None):
    global Kraken2_DATABASE, Kraken2_TAXLIST
    if database is None:
        Kraken2_DATABASE = os.path.join(DATABASE_PATH, 'Kraken2/krakenDB-202212')
        Kraken2_TAXLIST = os.path.join(Kraken2_DATABASE, 'tax.list')
    else:
        Kraken2_DATABASE = os.path.join(DATABASE_PATH, "Kraken2", database)
        Kraken2_TAXLIST = os.path.join(Kraken2_DATABASE, 'tax.list')
        
        
def set_HGT_database(database=None):
    global BP_HGT_DATABASE, BP_HGT_STRUCTURE
    if database is None:
        BP_HGT_DATABASE  = os.path.join(DATABASE_PATH, 'BPTracer/HGT/RefseqPan2/RefseqPan2')
        BP_HGT_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/HGT/RefseqPan2/RefseqPan2_taxonomy.tsv')
    else:
        BP_HGT_DATABASE  = os.path.join(DATABASE_PATH, 'BPTracer/HGT/',database,database)
        BP_HGT_STRUCTURE = os.path.join(DATABASE_PATH, 'BPTracer/HGT/', database, f"{database}_taxonomy.tsv")


