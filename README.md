# PythonStudy
Python3の勉強会で使う程度の雑なリポジトリです。

## Homebrewの導入

ここから( https://brew.sh/index_ja.html )

## Pythonのインストール

```
brew install python3
```

## gitの使い方

#### 手元にディレクトリを持ってこよう。

```
cd documents
mkdir git
cd git
git clone https://github.com/c-a-c/PythonStudy.git
cd PythonStudy
```

#### 自分のブランチ（作業場所）を作ろう

```
git branch "自分の名前"
git checkout "自分の名前"
```

#### ファイルを作成しよう
```
mkdir "自分の名前"
cd "自分の名前"
```

#### 勉強会の日付がわかるようなファイルを作成しよう
```
mkdir 西暦日付曜日
```

##### 例
```
2019June19Wed
```

コードを書こう！

#### 変更点をGitHubに適応しましょう！

```
git add 対象のファイル名
git commit -m "作業内容"
git push origin ブランチ名
```

#### プルリクエストを発行しよう!

ページの上のところに "Pull Requests" に移動しよう。

"New Pull Requests" を押しましょう。

" base:master <- compare:自分のブランチ " になるように変更しましょう。

最後に Create Pull Requests が押せたら完了！



