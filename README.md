# myadvent2017
社内アドベントカレンダー用

- impress.py 指定した語をインプレスで検索してURLを指定した語の名前のファイルに出力する
例: python impress.py NEC
- getcontents.py 指定したファイルに書かれているURLを読んで、中身をディレクトリ(指定した語+.dir)配下のファイルに出力する
- mecab.py getcontents.pyで作成した中身を分かち書きにした結果を、mecabディレクトリ配下の指定語+".mecab"ファイルに出力する
- word2vec.py mecabディレクトリ配下のファイルを読んでモデルをmodelファイルに出力する
- similars.py 指定した語に類似する語トップ10を出力する
- strength.py 第一引数 - 第二引数をstrength、第二引数 - 第一引数をweakとして表示する
