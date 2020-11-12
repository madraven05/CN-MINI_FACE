'''
Python File to handle Login/Logout and Signups
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import engine, User

Session = sessionmaker() # Creating a session

# Function to login
def login(username, password):
    pass

# Function to logout
def logout():
    pass

# Function to signup
def signup(username, password, id):
    
    Session.configure(bind=engine)
    session = Session()
    
    # Creating new_user object of the class User
    new_user = User(username=username, password=password, id=id) 
    
    # Add to the database
    session.add(new_user)
    session.commit()
    session.close()