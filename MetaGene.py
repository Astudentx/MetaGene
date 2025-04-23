#!/usr/bin/env python3
import sys
import os
import argparse
from argparse import RawTextHelpFormatter
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print(base_dir)

#from metaGene import fq2fa
from metaGene import Kraken2
#from metaGene import Kraken2Old
from metaGene import inputList
from metaGene import BP
from metaGene import BP2
from metaGene import HGT
from metaGene import Megahit
from metaGene import SPAdes
from metaGene import fileManager
from metaGene.tool import load_config_module
from metaGene import version

print("version ：",version.__version__,sep="")
print("author  ：",version.__author__,sep="")
print("email   ：",version.__email__,sep="")

def new_subparser(subparsers, parser_name, parser_description):
    subpar = subparsers.add_parser(parser_name,
                                   description=parser_description,
                                   help=parser_description,
                                   formatter_class=RawTextHelpFormatter,
                                   parents=[parent_parser])
    subparser_name_to_parser[parser_name] = subpar
    return subpar

# 判断当前是否作为主程序运行
if __name__ == '__main__':
    # 父解析器
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--version', help='output version information and quit', action='version',version=version.__version__)

    # 主解析器
    parser = argparse.ArgumentParser(parents=[parent_parser])
    parser.add_argument(
        '--config',
        type=str,
        default= "metaGene.config",
        help=(
        "Specify the configuration module name to load (e.g., metaGene.config or metaGene.config_custom). "
        "If not provided, the default 'metaGene.config' will be used.")    
    )
    subparsers = parser.add_subparsers(title="Sub-commands", dest='subparser_name', parser_class=argparse.ArgumentParser)
    subparser_name_to_parser = {}

    # 子命令描述
    BP_description = (
        "Run the BP-Tracer pipeline for comprehensive metagenomic analysis.\n"
        "This includes raw data statistics and ARG annotation.\n"
        "Example usage:\n"
        "\t\tMetaGene BP --file <Paired_fastaq_list> --pwd <output_folder>\n\n"
    )

    BP2_description = (
        "Perform functional gene extraction based on the BP-Tracer results.\n"
        "This step processes BP-Tracer outputs to generate filtered functional gene sequences.\n"
        "Example usage:\n"
        "\t\tMetaGene BP2 --file <Paired_fastaq_list> --pwd <output_folder>\n\n"
    )

    Kraken2_description = (
        "Classify metagenomic sequences using Kraken2 based on k-mer analysis.\n"
        "This enables taxonomic assignment of sequences to various microbial taxa.\n"
        "Example usage:\n"
        "\t\tMetaGene Kraken2 --file <Paired_fastaq_list> --pwd <output_folder>\n\n"
    )

    Megahit_description = (
        "Assemble metagenomic sequences using Megahit.\n"
        "This generates high-quality assemblies from paired-end metagenomic sequence data.\n"
        "Example usage:\n"
        "\t\tMetaGene Megahit --file <Paired_fastaq_list> --pwd <output_folder>\n\n"
    )
    
    SPAdes_description = (
        "Assemble metagenomic sequences using SPAdes.\n"
        "This generates high-quality assemblies from paired-end metagenomic sequence data.\n"
        "Example usage:\n"
        "\t\tMetaGene SPAdes --file <Paired_fastaq_list> --pwd <output_folder>\n\n"
    )
    
    HGT_description = (
        "Detect Horizontal Gene Transfer (HGT) events using WAAFLE.\n"
        "This tool identifies novel Lateral Gene Transfer (LGT) events in assembled metagenomes, including those from human microbiomes.\n"
        "Example usage:\n"
        "\t\tMetaGene HGT --file <Single_fasta_list> --pwd <output_folder>\n\n"
    )


    # 添加母体程序
    Anno_parser = new_subparser(subparsers, 'BP', BP_description)
    Anno_arguments = Anno_parser.add_argument_group('required arguments')
    Anno_arguments.add_argument('--file', '-f', help="The metagenome list of all fasta", required=True)
    Anno_arguments.add_argument('--pwd', '-o',  help="Path output to folder", default= "./")
    Anno_arguments.add_argument('--print', choices=['T', 'F'], default='F', help="Specify T for True or F for False")
    Anno_arguments.add_argument('--GeneType', '-g', 
    help="Specify gene types to analyze (e.g., 'ARGs,MGEs'). Default: 'ALL' (analyze all types).",
    default='ALL')

    # 添加母体程序
    Anno_parser = new_subparser(subparsers, 'BP2', BP2_description)
    Anno_arguments = Anno_parser.add_argument_group('required arguments')
    Anno_arguments.add_argument('--file', '-f', help="The metagenome list of all fasta", required=True)
    Anno_arguments.add_argument('--pwd', '-o',  help="Path output to folder", default= "./")
    Anno_arguments.add_argument('--thread', '-t', type=int, help="The thread of Blast", default= 4)
    Anno_arguments.add_argument('--print', choices=['T', 'F'], default='F', help="Specify T for True or F for False")
    Anno_arguments.add_argument('--GeneType', '-g', 
    help="Specify gene types to analyze (e.g., 'ARGs,MGEs'). Default: 'ALL' (analyze all types).",
    default='ALL')


    # 添加母体程序
    Anno_parser = new_subparser(subparsers, 'Kraken2', Kraken2_description)
    Anno_arguments = Anno_parser.add_argument_group('required arguments')
    Anno_arguments.add_argument('--file', '-f', help="The metagenome list of all fasta", required=True)
    Anno_arguments.add_argument('--db', '-d', help="Database for Kraken2 classification. Options: BPTax_V1, BPTax_V2, krakenDB-202212, krakenDB-202406.", default= "krakenDB-202212")
    Anno_arguments.add_argument('--pwd', '-o',  help="Path output to folder", default= "./")
    Anno_arguments.add_argument('--print', choices=['T', 'F'], default='F', help="Specify T for True or F for False")

    # 添加母体程序
    Anno_parser = new_subparser(subparsers, 'SPAdes', SPAdes_description)
    Anno_arguments = Anno_parser.add_argument_group('required arguments')
    Anno_arguments.add_argument('--file', '-f', help="The metagenome list of all fasta", required=True)
    Anno_arguments.add_argument('--pwd', '-o',  help="Path output to folder", default= "./")
    Anno_arguments.add_argument('--print', choices=['T', 'F'], default='F', help="Specify T for True or F for False")
    
    # 添加母体程序
    Anno_parser = new_subparser(subparsers, 'Megahit', Megahit_description)
    Anno_arguments = Anno_parser.add_argument_group('required arguments')
    Anno_arguments.add_argument('--file', '-f', help="The metagenome list of all fasta", required=True)
    Anno_arguments.add_argument('--pwd', '-o',  help="Path output to folder", default= "./")
    Anno_arguments.add_argument('--print', choices=['T', 'F'], default='F', help="Specify T for True or F for False")
    
    
    # 添加母体程序
    Anno_parser = new_subparser(subparsers, 'HGT', HGT_description)
    Anno_arguments = Anno_parser.add_argument_group('required arguments')
    Anno_arguments.add_argument('--file', '-f', help="The contig list of all fasta", required=True)
    Anno_arguments.add_argument('--db', '-d', help="Database for HGT classification. Options: RefseqPan2, chocophlan2, UnigeneSet-waafledb.v1.fa ,UnigeneSet-waafledb.v2.fa (from WAAFLE).", default= "RefseqPan2")
    Anno_arguments.add_argument('--pwd', '-o',  help="Path output to folder", default= "./")
    Anno_arguments.add_argument('--print', choices=['T', 'F'], default='F', help="Specify T for True or F for False")



    # 检查命令行，第一个字符是否是1，否则就运行下面的代码
    if (len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == 'help'):
        #print('{}'.format(fileManager.generate_header()))
        print('{}'.format(fileManager.generate_header_metagene()))
        print('...::: MetaGene v' + version.__version__ + ' :::...''')
        print('General usage:')
        print('MetaGene subparser --config ->,'
              "Specify the configuration module name to load (e.g., config_default or config_custom).\n"
              'If not provided, the default "metaGene.config" will be used.\n')
        print(' \n')
        print('Kraken2 -> %s' % Kraken2_description)
        print('BP -> %s' % BP_description)
        print('BP2 -> %s' % BP2_description)
        print('SPAdes -> %s' % SPAdes_description)
        print('Megahit -> %s' % Megahit_description)
        sys.exit(0)
    else:
        args = parser.parse_args()
        

    # 加载用户指定的配置参数模块
    if args.config:
        print(f"加载用户指定的配置模块: {args.config}")
        config = load_config_module(args.config)
    else:
        print("使用默认配置模块: metaGene.config")
        config = load_config_module('metaGene.config')
    

    # 检查 config 是否正确加载
    if config is None:
        raise ValueError("config 未初始化，请检查 load_config_module 调用！")
     # 检查 config 是否包含 set_output_path 方法
    if not hasattr(config, "set_output_path"):
        raise AttributeError(f"配置模块 {args.config} 中缺少 set_output_path 方法")
    

    config.set_output_path(args.pwd)
    # Now you can use config.OUTPUT_PATH throughout your program
    print(f"Output path set to: {config.OUTPUT_PATH}")
    print(f"mkdir analysis folders")

    
    # 如果子程序是BP-Tracer
    if args.subparser_name == 'BP':
        fileManager.mkdir(config.SHELL_PATH)
        fileManager.mkdir(config.Kraken2_OUTPUT_PATH)
        print(f"Shells set to: {config.SHELL_PATH}")
        print(f"Results set to: {config.Kraken2_OUTPUT_PATH}")
        # 读取fqlist信息
        dataList = inputList.read_paired_list(args.file)
        
        # 生成inputList用于分析
        inputList.generate_inputlist(args.file,"intput.list",config.Kraken2_OUTPUT_PATH)
        
        geneType = args.GeneType.split(',') if args.GeneType != 'ALL' else ['ARGs', 'MGEs', 'MRGs', 'VFs', 'SGs']

        # 首先生成 RawStat 脚本（仅一次）
        script_paths_all = []
        for i in range(0, dataList.number, 1):
            ID = dataList.id[i]
            file1 = dataList.file1[i]
            file2 = dataList.file2[i]
            # 执行 RawStat
            soft_runner = BP.RawdataStat(config=config, id=ID, file1=file1, file2=file2)
            soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"BP.S01.RawStat.{ID}.sh")
            soft_runner.generate_script(script_path)
            script_paths_all.append(script_path)

        script_paths_all = []
        # 然后针对每种基因类型生成 ARGAnno 脚本
        for geneType in geneType:
            for i in range(0, dataList.number, 1):
                ID = dataList.id[i]
                file1 = dataList.file1[i]
                file2 = dataList.file2[i]

                soft_runner = BP.GeneAnno(config=config, id=ID, file1=file1, file2=file2, geneType=geneType)
                soft_runner.print_command(should_print=args.print)
                script_path = os.path.join(config.SHELL_PATH, f"BP.S02.{geneType}Anno.{ID}.sh")
                soft_runner.generate_script(script_path)
                script_paths_all.append(script_path)
                
        
        # Kraken2相关分析脚本生成
        
        fileManager.mkdir(config.SHELL_PATH)
        fileManager.mkdir(config.BP_OUTPUT_PATH)
        
        # 设置数据库
        config.set_kraken2_database("BPTax_V2")
        print(f"Output set to: {config.OUTPUT_PATH}")
        print(f"Shells set to: {config.SHELL_PATH}")
        print(f"Results set to: {config.BP_OUTPUT_PATH}")
        print(f"Database set to: {config.Kraken2_DATABASE}")
        
        # 读取fqlist信息

        script_paths_all = []
        for i in range(0, dataList.number, 1):
            ID = dataList.id[i]
            file1 = dataList.file1[i]
            file2 = dataList.file2[i]
            # 执行命令输入参数
            soft_runner = Kraken2.Kraken2Runner(config= config, id=ID, file1=file1, file2=file2)

            # 直接打印命令
            content = soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"Tax.S01.Kraken2.{ID}.sh")
            soft_runner.generate_script(script_path)
            script_paths_all.append(script_path)
        #soft_runner.run_scripts_parallel(script_paths_all1, max_workers=3)
        
        soft_runner = Kraken2.Kraken2Runner2(config= config,id_list= dataList.id)
        soft_runner.print_command(should_print=args.print)
        script_path = os.path.join(config.SHELL_PATH, f"Tax.S02.Kraken2.Merge.sh")
        soft_runner.generate_script(script_path)
        
        soft_runner = Kraken2.FastqStatRunner(config= config,fqlist= args.file)
        soft_runner.print_command(should_print=args.print)
        script_path = os.path.join(config.SHELL_PATH, f"Tax.S00.Stat.sh")
        soft_runner.generate_script(script_path)

    
            
    # 修改 BP2 的逻辑以支持 --GeneType 参数
    if args.subparser_name == 'BP2':
        # 根据 `--print` 参数值控制打印逻辑
        if args.print == 'T':
            print("This message is printed because --print=T")
        else:
            print("Printing is disabled because --print=F")
            geneType = args.GeneType.split(',') if args.GeneType != 'ALL' else ['ARGs', 'MGEs', 'MRGs', 'VFs', 'SGs']
            print(f"Processing gene types: {geneType}")
        
        for geneType in geneType:
            # ExtractedFaFiles
            soft_runner = BP2.ExtractedFaFiles(config= config,geneType=geneType,thread= args.thread)
            soft_runner.process_files()
            # 循环生成脚本并运行
            script_paths_all = []
            for i, split_fa in enumerate(soft_runner.split_fa):
                # 获取当前分割文件的命令
                soft_runner.build_command(index = i)
                soft_runner.print_command(should_print=args.print,index = i)

                # 定义脚本路径,写入命令到脚本 指定Index，将动态传入到build_command()中间
                script_path = os.path.join(config.SHELL_PATH, f"BP.S03.temp.{geneType}.{i}.sh")
                soft_runner.generate_script(script_path,index = i)
                script_paths_all.append(script_path)
                print(f"Generated script for file {split_fa}: {script_path}")
            #soft_runner.run_scripts_parallel(script_paths_all, max_workers=3)

            # CatBlastFiles
            soft_runner = BP2.CatBlastFiles(config= config,geneType=geneType)
            soft_runner.process_files()
            soft_runner.build_command()
            soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"BP.S04.{geneType}.Merge.sh")
            soft_runner.generate_script(script_path)
            # soft_runner.run_command()
        
        

     # 如果子程序是Kraken2
    if args.subparser_name == 'Kraken2':
        fileManager.mkdir(config.SHELL_PATH)
        fileManager.mkdir(config.Kraken2_OUTPUT_PATH)
        
        # 设置数据库
        config.set_kraken2_database(args.db)
        print(f"Output set to: {config.OUTPUT_PATH}")
        print(f"Shells set to: {config.SHELL_PATH}")
        print(f"Results set to: {config.Kraken2_OUTPUT_PATH}")
        print(f"Database set to: {config.Kraken2_DATABASE}")
        
        # 读取fqlist信息
        dataList = inputList.read_paired_list(args.file)

        script_paths_all = []
        for i in range(0, dataList.number, 1):
            ID = dataList.id[i]
            file1 = dataList.file1[i]
            file2 = dataList.file2[i]
            # 执行命令输入参数
            soft_runner = Kraken2.Kraken2Runner(config= config, id=ID, file1=file1, file2=file2)

            # 直接打印命令
            content = soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"Tax.S01.Kraken2.{ID}.sh")
            soft_runner.generate_script(script_path)
            script_paths_all.append(script_path)
        #soft_runner.run_scripts_parallel(script_paths_all1, max_workers=3)
        
        soft_runner = Kraken2.Kraken2Runner2(config= config,id_list= dataList.id)
        soft_runner.print_command(should_print=args.print)
        script_path = os.path.join(config.SHELL_PATH, f"Tax.S02.Kraken2.Merge.sh")
        soft_runner.generate_script(script_path)
        
        soft_runner = Kraken2.FastqStatRunner(config= config,fqlist= args.file)
        soft_runner.print_command(should_print=args.print)
        script_path = os.path.join(config.SHELL_PATH, f"Tax.S00.Stat.sh")
        soft_runner.generate_script(script_path)


        
    # 如果子程序时SPAdes
    if args.subparser_name == 'SPAdes':
        fileManager.mkdir(config.SHELL_PATH)
        fileManager.mkdir(config.SPAdes_OUTPUT_PATH)
        print(f"Shells set to: {config.SHELL_PATH}")
        print(f"Results set to: {config.SPAdes_OUTPUT_PATH}")
        # 读取fqlist信息
        dataList = inputList.read_paired_list(args.file)
        
        script_paths_all = []
        for i in range(0, dataList.number, 1):
            ID = dataList.id[i]
            file1 = dataList.file1[i]
            file2 = dataList.file2[i]
            # 执行命令输入参数
            soft_runner = SPAdes.SPAdesRunner(config= config, id=ID, file1=file1, file2=file2)

            # 直接打印命令
            content = soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"SPAdes.S01.Assambly.{ID}.sh")
            soft_runner.generate_script(script_path)
            script_paths_all.append(script_path)
        #soft_runner.run_scripts_parallel(script_paths_all1, max_workers=3)
        
        # 如果子程序时Megahit
    if args.subparser_name == 'Megahit':
        fileManager.mkdir(config.SHELL_PATH)
        fileManager.mkdir(config.Megahit_OUTPUT_PATH)
        print(f"Shells set to: {config.SHELL_PATH}")
        print(f"Results set to: {config.Megahit_OUTPUT_PATH}")
        # 读取fqlist信息
        dataList = inputList.read_paired_list(args.file)
        
        script_paths_all = []
        for i in range(0, dataList.number, 1):
            ID = dataList.id[i]
            file1 = dataList.file1[i]
            file2 = dataList.file2[i]
            # 执行命令输入参数
            soft_runner = Megahit.MegahitRunner(config= config, id=ID, file1=file1, file2=file2)

            # 直接打印命令
            content = soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"Megahit.S01.Assambly.{ID}.sh")
            soft_runner.generate_script(script_path)
            script_paths_all.append(script_path)
        #soft_runner.run_scripts_parallel(script_paths_all1, max_workers=3)
        
        

     # 如果子程序是HGT
    if args.subparser_name == 'HGT':
        fileManager.mkdir(config.SHELL_PATH)
        fileManager.mkdir(config.HGT_OUTPUT_PATH)
        
        # 设置数据库
        config.set_HGT_database(args.db)
        print(f"Output set to: {config.OUTPUT_PATH}")
        print(f"Shells set to: {config.SHELL_PATH}")
        print(f"Results set to: {config.HGT_OUTPUT_PATH}")
        print(f"Database set to: {config.BP_HGT_DATABASE}")
        print(f"Structure set to: {config.BP_HGT_STRUCTURE}")
        
        # 读取fqlist信息
        dataList = inputList.read_single_list(args.file)

        script_paths_all = []
        for i in range(0, dataList.number, 1):
            ID = dataList.id[i]
            file1 = dataList.file1[i]
            # 执行命令输入参数
            soft_runner = HGT.HGTRunner(config= config, id=ID, file1=file1)

            # 直接打印命令
            content = soft_runner.print_command(should_print=args.print)
            script_path = os.path.join(config.SHELL_PATH, f"HGT.S01.{args.db}.{ID}.sh")
            soft_runner.generate_script(script_path)
            script_paths_all.append(script_path)
        #soft_runner.run_scripts_parallel(script_paths_all1, max_workers=3)
        