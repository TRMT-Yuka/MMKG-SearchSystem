def direct_prompt_template_v0(text):
    direct_prompt = f"""
        Does the following sentence/statement/tweet contain a check-worthy claim? 
        Answer only with Yes or No.
        ’{{text}}’
    """
    return direct_prompt.format(text=text)


def direct_prompt_template_v1(text):
    direct_prompt = f"""
    It is important that a verifiable factual check-worthy claim be verified by a professional fact-checker, 
    as the claim may cause harm to society, specific person(s), company(s), product(s), or some government entities. 
    However, not all factual claims are important or worth fact-checking by a professional fact-checker, as this very time-consuming. 
    Do you think that a professional fact-checker should verify the claim in the tweet:"{text}"? 
    Labels: No, no need to check; No, too trivial to check; Yes, not urgent; Yes, very urgent.
    Decide on one label. Then, answer only with Yes or No.
    """
    return direct_prompt.format(text=text)

def fable_52_questions_template(text,question):
    direct_prompt = f"""
    Read the following sentence/statement/tweet and evaluate the question provided.
    Return the answer with Yes, No, or Unknown.
    sentence/statement/tweet: {text}
    question: {question}
    """
    return direct_prompt.format(text=text, question=question)


# def fable_52_questions_template(text,question):
#     direct_prompt = f"""
#     Read the following sentence/statement/tweet and evaluate the question provided.
#     Return the answer with Yes, No, or Unknown.
#     sentence/statement/tweet: {text}
#     question: {question}
#     Decide on one label. Then, answer only with Yes ,No, or Unknown.
#     """
#     return direct_prompt.format(text=text, question=question)


import ollama
def get_llama3_response(input_text):
    response = ollama.chat(
        model='llama3',
        messages=[
            {'role': 'user', 'content': input_text}
        ],
        options={'temperature': 0},   # 決定論的出力（再現性が高い）
    )  
    return response['message']['content']



import csv
from typing import List, Dict

def Direct_Prompt(
    data: List[Dict],
    output_path: str,
    prompt_func,
    response_func,
    overwrite: bool = True,
):
    mode = "w" if overwrite else "a"# 初期化（上書き or 追記）
    with open(output_path, mode, newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if overwrite:
            writer.writerow(["local_id", "response"])  # ヘッダー
    for d in data:
        try:
            prompt = prompt_func(d["claim"])
            response = response_func(prompt)
        except Exception as e:
            response = f"ERROR: {e}"
        with open(output_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([d["local_id"], response])

    print(f"✅ Completed writing results to {output_path}")



from src.FABLE import FABLE
def FABLE_52_Questions(
    data: List[Dict],
    output_path: str,
    prompt_func,
    response_func,
    overwrite: bool = True,
):
    mode = "w" if overwrite else "a"# 初期化（上書き or 追記）
    with open(output_path, mode, newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if overwrite:
            writer.writerow(["local_id"] + [f"Q{i}" for i in range(1, 53)])  # ヘッダー
    for j,d in enumerate(data):
        try:
            answers = []
            for i, q in enumerate(FABLE, 1):
                print(f"\rProcessing {j}/{len(data)}  : Q{i}/52 ...", end="", flush=True)
                prompt = prompt_func(d["claim"], q)
                response = response_func(prompt)
                answers.append(response)
        except Exception as e:
            response = f"ERROR: {e}"
        with open(output_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([d["local_id"]] + answers)

    print(f"✅ Completed writing results to {output_path}")