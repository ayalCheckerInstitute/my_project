db_info = {'host': 'dpg-ch59kklgk4q8pauei490-a.oregon-postgres.render.com',
           'database': 'my_db_juju',
           'psw': 'uiidH4VZCHH4JBcUzurHUwSlF4ryOUZp',
           'user': 'admin',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
    # SQLALCHEMY_DATABASE_URI = f"postgresql://admin:uiidH4VZCHH4JBcUzurHUwSlF4ryOUZp@dpg-ch59kklgk4q8pauei490-a.oregon-postgres.render.com/my_db_juju"
