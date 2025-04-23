import subprocess
class BaseRunner:
    def __init__(self, **kwargs):
        self.params = kwargs  # Store parameters as a dictionary

    def build_command(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def print_command(self, should_print=False):
        cmd = self.build_command()
        # 修正条件，支持字符串 'T' 或布尔值 True
        if should_print == True or should_print == 'T':
            print(cmd)
        return cmd

    def run_command(self):
        cmd = self.build_command()
        if not cmd:
            raise ValueError("build_command did not return a valid command!")
        # 运行命令
        result = subprocess.run(cmd, shell=True, check=True)
        if result.returncode == 0:
            print("Command executed successfully!")
        else:
            print("Command execution failed!")
            print("Standard Output:", result.stdout)
            print("Standard Error:", result.stderr)
