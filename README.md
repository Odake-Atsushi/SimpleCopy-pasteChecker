# SimpleCopy-pasteChecker
Simple copy and paste checker

# 簡易コピペチェッカー
## 概要
簡易的なコピペを判定するツールです．２つの文章に同じ並びがあるかどうかを判定します．

現在，英文のみに対応しています．
Windows用．

## 使い方
1. 実行ファイルをダウンロードする．
1. ダウンロードしたファイルをダブルクリックして起動する．
1. 検証したい文章が書かれたテキストファイル（文字コード：UTF-8）２つと連続単語数を指定する．
1. 大文字,小文字の区別をするかどうかを選択する．
1. 検索ボタンを押す．

## 注意
- 読み込ませるテキストファイルは，文字コードをUTF-8にしてください．
- 結果は参考程度にしてください．取りこぼしがある可能性があります．特に，文章中にハイフン等が入っていると，間違った区切りで単語を認識する可能性があります．

## ビルド方法
Pythonパッケージの `PySimpleGUI` と，`pyinstaller` をインストールする．
```
git clone https://github.com/Odake-Atsushi/SimpleCopy-pasteChecker.git
pyinstaller SCPChecker.py --onefile --noconsole --clean
```
`SimpleCopy-pasteChecker/dist` 以下に実行ファイルが生成される．