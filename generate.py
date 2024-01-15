import os
import pandas as pd
import re

SECTION_TITLE = {
    "Sec2": "Foundation Model Overview",
    "Sec3": "Resource-efficient Architectures",
    "Sec4": "Resource-efficient Algorithms",
    "Sec5": "Resource-efficient Systems",
}

SECTIONS = {
    "Sec2.1": "Language Foundation Models",
    "Sec2.2": "Vision Foundation Models",
    "Sec2.3": "Multimodal Large FMs",
    "Sec3.1": "Efficient Attention",
    "Sec3.2": "Dynamic Neural Network",
    "Sec3.3": "Diffusion-specific Optimization",
    "Sec3.4": "ViT-specific Optimizations",
    "Sec4.1": "Pre-training Algorithms",
    "Sec4.2": "Finetuning Algorithms",
    "Sec4.3": "Inference Algorithms",
    "Sec4.4": "Model Compression",
    "Sec5.1": "Distributed Training",
    "Sec5.2": "Federated Learning",
    "Sec5.3": "Serving on Cloud",
    "Sec5.4": "Serving on Edge",
}

def proc_single_section(secname, df):
    # files = os.listdir()
    # df = None
    # for f in files:
    #     if f.endswith(secname):
    #         df = pd.read_csv(f)
    # if df is None:
    #     print(f"No file found for {secname}")
    #     exit
    
    for index, row in df.iterrows():
        # process paper/blog title
        title = row["Paper title"]
        if pd.isna(title):
            continue
        title = title.replace("\n", " ")
        title = title[:-1] if title.endswith(".") else title
        title = " ".join(title.split())

        # process conference
        conf = row["Conference"]
        conf = "URL" if "blog" in conf else conf
        conf = conf.replace("`", "'")
        conf = re.sub(r'(?i)arxiv', 'arXiv', conf)
        conf = conf.strip()

        # process Link
        link = row["Link"]
        link = link[:-1] if link.endswith(".") else link

        # process code
        code = row["Code"]
        if not pd.isna(code):
            code = code[:-1] if code.endswith(".") else code

        if conf == "URL":
            final_string = f"- {title}. [[URL]]({link})"
        else:
            final_string = f"- {title}. *[{conf}]* [[Paper]]({link})"
            if not pd.isna(code):
                final_string += f" [[Code]]({code})"
        print(final_string)


def proc_all():
    sheets_dir = pd.read_excel("Paper List for Github Repo.xlsx", sheet_name=None)
    for sec, sheet in sheets_dir.items():
        if "2.1" in sec:
            print(f"\n## {SECTION_TITLE['Sec2']}\n")
        elif "3.1" in sec:
            print(f"\n## {SECTION_TITLE['Sec3']}\n")
        elif "4.1" in sec:
            print(f"\n## {SECTION_TITLE['Sec4']}\n")
        elif "5.1" in sec:
            print(f"\n## {SECTION_TITLE['Sec5']}\n")

        print(f"\n### {SECTIONS[sec]}\n")

        proc_single_section(sec, sheet)


if __name__ == "__main__":
    proc_all()
