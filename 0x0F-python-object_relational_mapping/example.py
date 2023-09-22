#!/usr/bin/python3

# connect

import MySQLdb
MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = 'ilyassLf123'
MY_DB = 'my_db'

db = MySQLdb.connect(host = MY_HOST, user = MY_USER, passwd = MY_PASS, db = MY_DB)

# Perform Database Operations

cur = db.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS employees(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, \
    title TEXT NOT NULL)"
)
db.commit()

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine



# corrected database URL
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    
    def __repr__(self):
        return f"<User(name='{self.name}', fullname = '{self.fullname}')>)"
