from pathlib import Path

PROJECT_ROOT = Path.cwd().resolve()   #プロジェクトルート
DATA_ROW = PROJECT_ROOT / "data" / "row" #生データ格納ディレクトリ
DATA_CCWP_ROW = PROJECT_ROOT / "data" / "row" / "CCWP" #生データ格納ディレクトリ
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"  #中間データ格納ディレクトリ
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"  #前処理後データ格納ディレクトリ
