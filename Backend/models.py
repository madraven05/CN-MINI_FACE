'''
All the MySQL Tables will be defined here
''' 
from sqlalchemy import create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# User Database Class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    # status = Column(Integer)

    def __repr__(self):
        return "<User(username='%s', id='%s')>" % (
            self.username, self.id)

def create_tables():
    return Base.metadata.create_all(engine)

def show_all_users(User):
    
    for instance in session.query(User):
        print(instance.username, instance.id)
# Post Database Class

# Messages Database Class

#