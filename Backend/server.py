'''
Python file for the Server
'''
from accounts import signup
from models import create_tables, show_all_users, User

create_tables()

signup(username="pranshu", password="abcd", id=12)
signup(username="dhruv", password="abcd", id=123)
signup(username="kumar", password="abcd", id=124)
show_all_users(User)