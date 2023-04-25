db_info = {'host': 'ayalganem.mysql.pythonanywhere-services.com',
           'database': 'my_project',
           'psw': 'getthere',
           'user': 'ayalganem',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
