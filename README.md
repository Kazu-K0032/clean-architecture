# リポジトリ

クリーンアーキテクチャの概要やコード例を管理するリポジトリです。

学習用として構築しています。

# 導入手順

## 環境構築

1. リポジトリをクローンします。
   ```bash
   git clone <リポジトリのURL>
   cd <リポジトリのディレクトリ>
   ```

2. 仮想環境を作成し、有効化します。
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. 必要なライブラリをインストールします。
   ```bash
   pip install -r requirements.txt
   ```

4. アプリケーションを起動します。
   ```bash
   python main.py
   ```

5. ブラウザで `http://localhost:8000/docs` にアクセスし、APIの動作を確認できます。
