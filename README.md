
# MetaGene

**MetaGene** 是一个综合性的宏基因组数据分析工具，支持从原始测序数据出发，完成包括物种分类、功能基因识别、物种溯源以及水平基因转移（Horizontal Gene Transfer, HGT）分析的全流程处理。

## 🔧 核心功能

1. **基于Reads的物种分类学分析**  
   利用 [Kraken2](https://ccb.jhu.edu/software/kraken2/) 进行高效的分类学注释。默认自建的基于Pangenomes的数据库，同时支持自定义数据库。
   
2. **基于Reads的功能基因识别与溯源分析**  
   基于BP-Tracer流程，提取抗生素抗性基因（ARGs）、可移动遗传元件（MGEs）等主流功能基因并追踪其潜在宿主。同时还支持毒力因子（VFs）、金属抗性基因（MRGs）以及抗压力基因STREE（SGs）

3. **基于Contig的水平基因转移分析（HGT）**  
   集成 [WAAFLE](https://github.com/biobakery/waafle) 工具，识别可能的基因水平转移事件。默认自建的基于Pangenomes的数据库，同时支持自定义数据库，可使用WAAFLE自带的chocophlan2数据库。

---

## 📦 安装方式

软件主提安装
```bash
# git clone方式
git clone https://github.com/Astudentx/MetaGene
# 安装依赖（推荐使用conda）
conda env create -f environment.yml
conda activate metagene
```
数据库安装
```bash
# 数据库较大，请通过百度网盘下载，安装到 `MetaGene/db/`中
# 网盘链接如下：

```

---

## 🚀 快速开始

### 1. 物种分类分析 

```bash
# 默认使用
MetaGene BP --file <Paired_fastaq_list> --pwd <output_folder> --GeneType ARGs,MGEs
MetaGene Kraken2 --file <Paired_fastaq_list> --db <database_name> --pwd <output_folder>
```

- 支持的数据库包括：`BPTax_V1`, `BPTax_V2`, `krakenDB-202212`, `krakenDB-202406`

### 2. 功能基因识别与溯源分析

#### (1) 基因注释主流程 (BP)

```bash
MetaGene BP --file <Paired_fastaq_list> --pwd <output_folder> --GeneType ARGs,MGEs
```

#### (2) 基因序列提取 (BP2)

```bash
MetaGene BP2 --file <Paired_fastaq_list> --pwd <output_folder> --GeneType ARGs
```




### 3. 水平基因转移分析 (HGT)

```bash
MetaGene HGT --file <Contig_fasta_list> --db RefseqPan2 --pwd <output_folder>
```

- 可选数据库包括：`RefseqPan2`, `chocophlan2`, `UnigeneSet-waafledb.v1.fa`, `UnigeneSet-waafledb.v2.fa`
####  组装工具

```bash
# 额外封装了Megahit与SPAdes两种主流组装软件，可基于自身情况进行挑选
# Megahit: 推荐，占用资源更少，速度更快
# SPAdes: 长度更长，识别HGT的准确性更高，识别事件更多
MetaGene Megahit --file <Paired_fastaq_list> --pwd <output_folder> # Megahit
MetaGene SPAdes   --file <Paired_fastaq_list> --pwd <output_folder> # SPAdes
```
---

## 🧬 主要项目结构说明

```
MetaGene/
├── metaGene/
│   ├── Kraken2.py     # 物种分类模块
│   ├── BP.py               # 主功能基因注释流程
│   ├── BP2.py             # 功能基因序列提取
│   ├── HGT.py             # WAAFLE调用脚本
│   ├── Megahit.py         # Megahit拼接
│   ├── SPAdes.py          # SPAdes拼接
│   ├── config/            # 配置模块
│   ├── tool/              # 公共函数
│   └── ...
├── bin/
│   └── MetaGene           # 主执行脚本
├── README.md
├── environment.yml        # Conda依赖环境
└── ...
```

---

## 🔗 外部依赖

请确保已安装以下工具，或使用内置 Conda 环境进行统一管理：

- [Kraken2](https://ccb.jhu.edu/software/kraken2/)
- [MEGAHIT](https://github.com/voutcn/megahit)
- [SPAdes](https://github.com/ablab/spades)
- [WAAFLE](https://github.com/biobakery/waafle)
- BLAST+
---

## 📄 引用格式（如适用）

如您在研究中使用本工具，请引用以下文章/作者信息：
> **BP-tracer: A metagenomic pipeline for tracing the multifarious biopollutome**
> Yaozhong Zhang, Gaofei Jiang
> _XXXXX_ (2025)
> doi: [XXXXX](XXXXX)
---

## 📬 联系方式

如有问题或建议，欢迎通过 Issues 或 Email 联系我们。
yaozhongzyz@163.com & gjiang@njau.edu.cn