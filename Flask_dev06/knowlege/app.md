## Flaskではsessionを使う際、session情報を暗号化する為のsession_keyの設定が必要
- 例
```
key = os.urandom(10) # 10桁の乱数を生成
app.secret_key = key # セッション情報の暗号化
```

## app.configについて
- Flaskの設定オブジェクトで、アプリの設定を行うことができる
- 辞書形式であり、設定を格納することができる
- app.config['KEY1'] = 'value1'
    - 上記は、app.configという辞書にキーと値を格納する文法
- 例
```
URI = 'sqlite:///trip.db'                             # アプリで使用するDBのURIを定義（DBの作成） 
app.config['SQLALCHEMY_DATABASE_URI'] = URI           # アプリがデータベースに接続する際に使用するURIを設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 自動的な更新処理も行わないように設定
print('------辞書の中身を出力------')
print(app.config)
```

## データベースオブジェクトについて
- SQLAlchemyオブジェクトは、データベースの操作やクエリの実行など、データベース関連の機能を提供している
- dbという変数にSQLAlchemyオブジェクトを代入することで、アプリ内のどの部分でもdbを使用して
- データベース操作を行うことができるようになる
- dbを介してテーブルの作成、データの追加や更新、クエリの実行などが行える
- 例えば、db.create_all()を呼び出すと、モデルクラスを基にデータベース内にテーブルを作成することができる
- 例
```
# FlaskのインスタンスをセットしてDB変数に格納（Flaskアプリへの関連付けを行う）
db = SQLAlchemy(app) 
```

## データベースとモデルを紐づける（マッピング）
- このクラスをインスタンス化してデータの保存、取得、削除を行う
- 例
```
class Trip(db.Model):
    __tablename__ = 'trip_table'                   # テーブルの作成
    id = db.Column(db.Integer, primary_key=True)   # 登録データのID
    title = db.Column(db.String(30), unique=True)  # タイトル
    content = db.Column(db.String(300))            # 本文
    latitude = db.Column(db.String(100))           # 緯度
    longitude = db.Column(db.String(100))          # 経度
    create_date = db.Column(                       # 登録時間
        db.DateTime,
        nullable=False,
        default=datetime.now()
    )
```

## データベースの初期化
- VSCodeのターミナルから実行する
- 作業ディレクトリ内で、flask initialize_DB　のコマンドを実行する
- パスが通ってない場合は、python -m flask initialize_DB　のコマンドを実行する
- 例
```
@app.cli.command('initialize_DB') # Flaskアプリ内で実行可能なカスタムコマンドを作成
def initialize_DB():              # initialize_DB()は、initialize_DBというコマンドで登録される
    db.create_all()               # Tripクラスの記述を基にデータベース内にテーブルを作成することができる
    print('データベースの初期化が完了しました。')
```

## redirect()
- 引数に指定したページにリダイレクトさせる

## url_for()
- 特定の関数へのURLを作成
