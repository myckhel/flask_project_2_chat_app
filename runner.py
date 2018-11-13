from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sys

conn = create_engine('sqlite:///chat.db')
db = conn.connect()

# db.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER  PRIMARY KEY AUTOINCREMENT, isbn VARCHAR(10) NOT NULL UNIQUE, title VARCHAR(10) NOT NULL, author VARCHAR(10) NOT NULL, year DATE NOT NULL)")
# db.execute("ALTER TABLE users DROP users")
all = db.execute("SELECT * FROM users")
# for user in all:
    # print('1')
print(all)
