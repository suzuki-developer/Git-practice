## 'r+'
- `'r+'` モード
    - 既存のファイルを読み取りつつ、その内容を更新したい場合などに使用される
    - ファイルを読み書き両方の目的で開くためのファイルモード
    - ファイルが既に存在する場合にはファイルの先頭から読み取りが行われる
    - 書き込みも行うことができる
    - 制約
        - ファイルの読み取り位置: 
            - 'r+' モードでは、ファイルの読み取り位置が先頭に設定される
            - 書き込み前にファイルポインタを移動する必要がある
        - ファイルの書き込み:
            -  'r+' モードでは、既存のデータを上書きする形で書き込みが行われる
            - 新しいデータをファイルの途中や末尾に追加することはできない

- `r (read)` モード
    - ファイルを読み取りモードで開く

- `+ (update)` モード
    - ファイルの読み書きを両方の操作できる

- 参考
    - ＜fopen関数のモード＞
    - http://rainbow.pc.uec.ac.jp/edu/program/b1/Ex7-1b.htm


## flock()

## LOCK_EX

## (int)fread($fileHandle, filesize($accessCounterFile))

## rewind()

## LOCK_UN