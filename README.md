# MMKG-SearchSystem  
Multi-Modal Knowledge Graph Search System

## Overview
**MMKG-SearchSystem** は．複数のモダリティから特徴を抽出し．  
**マルチモーダル埋め込み（Multi-Modal Embedding）を生成して高速類似検索を実行する．

---

## Features

```bash
MMKG-SearchSystem/
├── README.md
├── models/　     # 自由入力時に使用するモデルを格納　別途配布
├── DATA/
│   ├── jpbook_and_BR/
│   │   ├──DB/
│   │   ├──Query/
│   │   ├──from_ontology
│   │   ├──original.parquet #オリジナルのデータ
│   │   ├──test.parquet     #オリジナルをテスト用に分割
│   │   ├──train_only.parquet #オリジナルをモデル用に分割
│   │   └──WavDesc2bid.bin　 #オリジナルに含まれる表記をWikiDataのID番号に統一したもの．手動で作成
│   ├── xeno_cant/
│   └── api_reference.md
├── src/                          # ★ システム主要コード
│   ├── config.py                 # パス管理（DATA_PATH 等） 
│   ├── get_AudioVec.py           # 音声→SVec 抽出（wav2vec2 用） 
│   ├── gpu.py                    # GPU 管理・情報表示ユーティリティ 
│   ├── main.py                   # FastAPI ベースの検索 UI / API 本体（大量の処理を含む） 
│   ├── mymodule.py               # 汎用 I/O（bin 読み書き）などのモジュール 
│   ├── preprocessing.py          # カタカナ変換ほかテキスト前処理機能 
│   └── retrieval.py              # 類似度計算・GLS 埋め込み統合・検索補助関数群 
├── 0_test_make.ipynb
├── 04_CV_notMean_concatVecs_making.ipynb
├── 05_2_CV_Retrieval_test.ipynb
├── 05_CV_Retrieval_test.ipynb
├── 06_CV_Retrieval_test_Lang_Graph_forSave.ipynb
├── 07_missing_Data_fix.ipynb
├── 08_CV_Rank.ipynb
└── code_recipe.ipynb # コード断片まとめ・メモ


```


### 1. 0_test_make.ipynb
- 検索に必要なモダリティ・言語ごとの統合埋め込みをDATA/{データ名称}/{DB|Query}配下に生成

### 2. 04_CV_notMean_concatVecs_making.ipynb
### ~06_CV_Retrieval_test_Lang_Graph_forSave.ipynb
- 生成されたデータに基づく検索実験

### 3. 07_missing_Data_fix.ipynb
- データ欠損等への手動での対応

### 3. 08_CV_Rank.ipynb
- 検索結果の最終評価の出力

---

## System Requirements

- **Python 3.8+**
- **Ubuntu 20.04**
- 推奨：16GB RAM / GPU (任意)
- Pythonライブラリ

---

## Installation

```bash
git clone https://github.com/TRMT-Yuka/MMKG-SearchSystem.git
cd MMKG-SearchSystem
python3 -m venv venv
source venv/bin/activate
# MMKG-SearchSystem
