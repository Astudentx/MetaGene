import subprocess
import textwrap
from metaGene import config


# 构建cmd脚本
class SARGRunner():
    def __init__(self, id, file1):
        self.id = id
        self.file1 = file1
    def build_command(self):
        # 构建命令
        cmd = textwrap.dedent(rf"""
        mkdir {self.id}
        cd {self.id}
        {config.SARG_MAPPING_SOFTWARE} -d {config.SARG_DATABASE} -q {self.file1} \
            -o {self.id}.m8  \
            -t ./ \
            -b 8 \
            -f {config.SARG_FORMAT} \
            --evalue {config.SARG_EVALUE} \
            -k {config.SARG_MAX_TARGET_SEQS} \
            
        perl {config.BIN_PATH}/best_m8.pl {self.id}.SARG.m8  > {self.id}.SARG.m8.fil
        perl {config.BIN_PATH}/add.m8.func.pl {self.id}.SARG.m8.fil  {config.SARG_DATABASE}/SARG.3.2.list  {self.file1} > {self.id}.SARG.anno.xls
        """)
        return cmd

    def print_command(self):
        cmd = self.build_command()
        print(cmd) # 选择是否打印到主屏幕上



    def run_command(self):
        cmd = self.build_command()
        # 执行命令
        result= subprocess.run(cmd, shell=True, check=True)
        print("DIAMOND 比对成功!")
        # 检查命令是否成功执行
        if result.returncode == 0:
            print("DIAMOND 比对成功!")
        else:
            print("DIAMOND 比对失败!")
            print("标准输出:", result.stdout)
            print("标准错误:", result.stderr)

