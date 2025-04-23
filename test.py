CONFIG=None
def load_config(config_name):
    global CONFIG
    try:
        CONFIG = importlib.import_module(f"metaGene.{config_name}")
        if not CONFIG:
            raise ImportError(f"模块加载返回 None: {config_name}")
        # 测试模块是否定义了需要的属性
        assert hasattr(CONFIG, 'set_output_path'), f"模块 {config_name} 缺少属性 'set_output_path'"
    except Exception as e:
        print(f"加载模块时出现错误: {e}")
        raise
    print(f"CONFIG 的内容: {dir(CONFIG)}")
    

import sys
# 设置工作路径
project_root = "/mnt/sdb/zhangyz/bin/MetaGene"  # 修改为你的项目路径
if project_root not in sys.path:
    sys.path.append(project_root)
load_config("config_default")
import metaGene