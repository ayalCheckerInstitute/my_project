db_info = {'host': 'localhost',
           'database': 'bookstore',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
