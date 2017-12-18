# myadvent2017
アドベントカレンダー用

- impress.py 指定した語をインプレスで検索して，URLを指定した語の名前のファイルに出力する
- nikkei.py 指定した語を日経BPで検索して，URLを指定した語の名前のファイルに出力する
- getcontents.py 指定したファイルに書かれているインプレスのURLを読んで、中身をディレクトリ(指定した語+.dir)配下のファイルに出力する
- nikkei-getcontents.py 指定したファイルに書かれている日経BPのURLを読んで、中身をresultsディレクトリ配下のファイルに出力する
- mecab.py 引数で指定したディレクトリ配下のファイル(最大1000)を読んで中身を分かち書きにした結果を、引数+".mecab"ファイルに出力する(mecabディレクトリの下には置かない)
- word2vec.py 指定したmecab出力ファイルを読んでモデルをmodelファイルに出力する
- similars.py modelファイルを読んで指定した語に類似する語トップ10を出力する
- strength.py modelファイルを読んで第一引数 - 第二引数をstrength、第二引数 - 第一引数をweakとして表示する
- strength2.py modelファイルを読んで第一引数+第二引数-第三引数-第四引数をstrength, 第一引数+第二引数-第三引数-第四引数をweakとして表示する
- strength3.py modelファイルを読んで第一引数+第二引数-第三引数をstrength, 第一引数+第二引数-第三引数をweakとして表示する
