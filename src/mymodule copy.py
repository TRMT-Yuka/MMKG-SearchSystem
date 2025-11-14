import pickle
import pandas as pd
import os

#バイナリファイルの読み書き
def read_bin(filename):
    with open(filename,'rb') as bf:
        bin_data = pd.read_pickle(bf)
    return bin_data

def save_bin(filename,data):
    with open(filename,'wb') as bf:
        pickle.dump(data,bf)

# =============================================================================

import time
from requests.exceptions import RequestException
from openai import OpenAI
import openai

import configparser
config = configparser.ConfigParser()
config.read('config.ini')
from openai import OpenAI
api_key = config['openai']['api_key_mil2']
client = OpenAI(api_key=api_key)

def print_apikey():
    print(api_key)


def Prompt_for_6label_FC(claim):
    labels = ['False', 'Pants on Fire', 'Mostly False', 'Half True', 'Mostly True', 'True']
    few_shot = f"""Among {labels}, the claim ”’Emerson Moser, who was Crayola’s top crayon molder for almost 40 years, was colorblind.”’ can be classified as true.
Among {labels}, the claim ”’Bernie Sanders said 85 million Americans have no health insurance.”’ can be classified as half-true.
Among {labels}, the claim ”’Cheri Beasley “backs tax hikes — even on families making under $75,000.”’ can be classified as False.
 """
    return f"""{few_shot} Among {labels}, the claim ”’{claim}”’ can be classified as"""

def Prompt_for_52list(claim,question):
    return f"""Read the following claim and evaluate the question provided.
    Return the answer as <answer>Yes, No, or Unknown</answer>. 
    claim: {claim} 
    Question: {question}.
    Please explain your reasoning in <reason>tags</reason>.
    """


def gpt4o_ans(prompt):
    stream = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        # model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        stream=True,)
    ans = []
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            ans.append(chunk.choices[0].delta.content)
            
    return "".join(ans)    

def validate_claim_via_pi(prompt):
    for i in range(3):  # 3回までリトライ
        try:
            return gpt4o_ans(prompt)
            
        except openai.OpenAIError as e:
            time.sleep(5)
            if i == 2:
                return ""
                
        except RequestException as e:
            time.sleep(5)
            if i == 2:
                return ""

# def make_ans_dict(df):#12_Direct_Prompt用
#     ans_dict = dict()
#     ids = list(df["id"])
#     gold_labels = list(df["reviewRating.alternateName"])
#     claims = list(df["claimReviewed"])

#     for i in range(400):
#         if ids[i] not in ans_dict:
#             prompt = Prompt(claims[i])
#             ans = validate_claim_via_pi(prompt)
#             ans_dict[ids[i]] = {"id":ids[i],"ans":ans,"label":gold_labels[i]}
#             # print("\r%d / %d  ans:%s %s" %(i,400,ans," "*3000), end='')
#     return ans_dict


# =============================================================================

labels = [
    ('Pants on Fire', 'POF', 0),('False', 'F', 1),('Mostly False', 'MF', 2),
    ('Half True', 'HT', 3),('Mostly True', 'MT', 4),('True', 'T', 5)
]

def labeled(df):
    for k,v in df.items():
        v["ans"] = v["ans"].replace("  ","_").replace("_"," ")
        flg = {"F":0,"MF":0,"POF":0,"HT":0,"MT":0,"T":0,"UNK":0}
        if "False" in v["ans"]:
            flg = flg | {"F":1}
        if "Mostly False" in v["ans"]:
            flg = flg | {"F":0,"MF":1}
        if "True" in v["ans"]:
            flg = flg | {"T":1}
        if "Mostly True" in v["ans"] :
            flg = flg | {"T":0,"MT":1}
        if "Half True" in v["ans"]:
            flg = flg | {"T":0,"HT":1}
        if "Pants on Fire" in v["ans"] or "P ants on Fire" in v["ans"]:
            flg = flg | {"F":0,"MF":0,"POF":1}
        if flg["F"]+flg["MF"]+flg["POF"]+flg["HT"]+flg["MT"]+flg["T"] != 1:
            flg = {"F":0,"MF":0,"POF":0,"HT":0,"MT":0,"T":0,"UNK":1}
        df[k] = v | flg

    unk_list = []
    for k,v in df.items():
        if v["UNK"] == 1:
            unk_list.append(k)
            
    for k in unk_list:
        df.pop(k, None)

    for k,v in df.items():
        new_v = {"pred_grad":None,"pred":None,"ans_grad":None}
        for label,mini_label,level in labels:
            if v[mini_label] == 1:
                new_v = new_v | {"pred":label,"pred_grad":level}
            if v["label"] == label:
                new_v = new_v | {"ans_grad":level}
        df[k] = v | new_v

    return df


# =============================================================================


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, mean_absolute_error, f1_score

def AC_MAE_Matrix(data_list,matrix=False):
    true_labels = [v["ans_grad"] for v in data_list]
    pred_labels = [v["pred_grad"] for v in data_list]
    label_names = ['Pants on Fire','False','Mostly False','Half True','Mostly True','True']#"UnKnown"削除
    ac = np.mean(np.array(true_labels) == np.array(pred_labels))
    w_f1 = f1_score(true_labels, pred_labels, average='weighted')
    mae = mean_absolute_error(true_labels, pred_labels)

    print(f"Accuracy: {ac:.2f}  Weighted F1 Score: {w_f1:.2f}  Mean Absolute Error: {mae:.2f}")

    if matrix == True:
        conf_matrix = confusion_matrix(true_labels, pred_labels)
        plt.figure(figsize=(4, 3))
        # sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',xticklabels=label_names, yticklabels=label_names)
        plt.title('Confusion Matrix Heatmap')
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')

    return (ac,w_f1,mae)


# =============================================================================

import numpy as np
from scipy import stats

def analyze_data(data_a, data_b, label):
    A = np.array(data_a)
    B = np.array(data_b)

    A_var = np.var(A, ddof=1)  # Aの不偏分散
    B_var = np.var(B, ddof=1)  # Bの不偏分散
    A_df = len(A) - 1  # Aの自由度
    B_df = len(B) - 1  # Bの自由度
    f = A_var / B_var  # F比の値
    one_sided_pval1 = stats.f.cdf(f, A_df, B_df)  # 片側検定のp値 1
    one_sided_pval2 = stats.f.sf(f, A_df, B_df)   # 片側検定のp値 2
    two_sided_pval = min(one_sided_pval1, one_sided_pval2) * 2  # 両側検定のp値
    print(label)
    print(' F:', round(f, 3),'     p-value: ', round(two_sided_pval, 3))

def T_test(data_a, data_b, a = 0.05, equal_var=True):
    t_stat, p_value = stats.ttest_ind(data_a, data_b, equal_var=equal_var)
    print(f"P値: {p_value:.5f}",end=" 　")
    if p_value < a:
        print("有意差あり（帰無仮説を棄却）")
    else:
        print("有意差なし（帰無仮説を棄却できない）")


# =============================================================================

labels = [
    ('Pants on Fire', 'POF', 0),('False', 'F', 1),('Mostly False', 'MF', 2),
    ('Half True', 'HT', 3),('Mostly True', 'MT', 4),('True', 'T', 5)
]

def labeled(df):
    for k,v in df.items():
        v["ans"] = v["ans"].replace("  ","_").replace("_"," ")
        flg = {"F":0,"MF":0,"POF":0,"HT":0,"MT":0,"T":0,"UNK":0}
        if "False" in v["ans"]:
            flg = flg | {"F":1}
        if "Mostly False" in v["ans"]:
            flg = flg | {"F":0,"MF":1}
        if "True" in v["ans"]:
            flg = flg | {"T":1}
        if "Mostly True" in v["ans"] :
            flg = flg | {"T":0,"MT":1}
        if "Half True" in v["ans"]:
            flg = flg | {"T":0,"HT":1}
        if "Pants on Fire" in v["ans"] or "P ants on Fire" in v["ans"]:
            flg = flg | {"F":0,"MF":0,"POF":1}
        if flg["F"]+flg["MF"]+flg["POF"]+flg["HT"]+flg["MT"]+flg["T"] != 1:
            flg = {"F":0,"MF":0,"POF":0,"HT":0,"MT":0,"T":0,"UNK":1}
        df[k] = v | flg

    unk_list = []
    for k,v in df.items():
        if v["UNK"] == 1:
            unk_list.append(k)
            
    for k in unk_list:
        df.pop(k, None)

    for k,v in df.items():
        new_v = {"pred_grad":None,"pred":None,"ans_grad":None}
        for label,mini_label,level in labels:
            if v[mini_label] == 1:
                new_v = new_v | {"pred":label,"pred_grad":level}
            if v["label"] == label:
                new_v = new_v | {"ans_grad":level}
        df[k] = v | new_v

    return df
