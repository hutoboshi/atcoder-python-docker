# AtCoder 用 Docker 環境構築手順

このリポジトリは、AtCoder の競技プログラミングを Python (PyPy) で行うためのシンプルな Docker 環境を提供します。提出の自動化機能は含まれていません。

---

## 1. プロジェクト構成

```
atcoder-env/
├── Dockerfile
├── docker-compose.yml
└── src/
    └── main.py
```

---

## 2. 環境構築手順

### 1. リポジトリのクローン

```
git clone https://github.com/username/atcoder-env.git
cd atcoder-env
```

### 2. Docker イメージのビルド

```
docker-compose build
```

### 3. コンテナの起動

```
docker-compose up -d
```

### 4. コンテナに入る

```
docker-compose exec app /bin/bash
```

---

## 3. 動作確認

### 1. コード例: src/main.py

```python
def main():
    a, b = map(int, input().split())
    print(a + b)

if __name__ == "__main__":
    main()
```

### 2. コード実行

```
python3 main.py
```

入力例:

```
2 3
```

出力例:

```
5
```

---

## 4. テストケース取得と検証

### 1. オンラインジャッジツールの利用

```
oj d https://atcoder.jp/contests/abc100/tasks/abc100_a
```

### 2. テスト実行

```
oj t -c "pypy3 main.py"
```

---

## 5. 注意点

### 警告への対応

起動時に以下の警告が表示されることがあります:

```
Warning: cannot find your CPU L2 & L3 cache size in /sys/devices/system/cpu/cpuX/cache
```

この警告は PyPy が CPU キャッシュ情報を取得できないため表示されるもので、競技プログラミングでは無視しても問題ありません。

必要に応じて以下の方法で警告を非表示にできます。

1. 標準エラー出力を無視する

```
pypy3 main.py 2>/dev/null
```

2. 環境変数を設定する (Dockerfile 修正例)

```dockerfile
ENV PYPY_GC_L2=262144
ENV PYPY_GC_L3=8388608
```

---

## 6. 環境終了

```
docker-compose down
```

---

## 7. 参考情報

- [online-judge-tools](https://github.com/online-judge-tools/oj)
