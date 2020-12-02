import pymysql
from cryptography.fernet import Fernet
import datetime




# unique key for encryption and decryption

key = b'wrSpkmSaEi4HxFLZp5Ii_Vsx0hN0RGqnak2sSilOrjo='
  
  

# function for encryption of password
def encrypt(pw):
    cipher_suite = Fernet(key)
    new = pw.encode('UTF-8')
    ciphered_text = cipher_suite.encrypt(new)   
    # print(ciphered_text.decode('utf-8')) 
    return ciphered_text.decode('utf-8')



# function for decryption of password
def decrypt(enc_pw):
    cipher_suite1 = Fernet(key)
    ciphered_text1 = enc_pw.encode('utf-8')
    unciphered_text1 = (cipher_suite1.decrypt(ciphered_text1))
    # print(unciphered_text1.decode('utf-8')) 
    return unciphered_text1.decode('utf-8')


def user_register(fname, lname, username, user_password):
    
    
    # encrypted password 
    
    encrypt_pw = encrypt(user_password)
    
    try:   #database connectivity
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        
        # five entries in database 
        cur.execute("insert into users (fname,lname,username,encrypt_pw, online) values(%s,%s,%s,%s,%s)", 
            ( 
                fname, 
                lname, 
                username,
                encrypt_pw,
                0
                
            )) 
    
        sql = "SELECT * FROM users WHERE fname = %s AND lname = %s AND username = %s"
        
        mytuple = (
            fname,
            lname,
            username
        )

        cur.execute(sql,mytuple)

        print ("%d rows were returned" % (cur.rowcount-1))

        
        if cur.rowcount<=1 :  #user doesn't exist, insert new entry
            con.commit()
            con.close()
            print("Success!")
            return 1 # Success Code 

        else :     # user already exist
            print("This user profile already exist!")
            return 0 # Failure code

    except Exception as es:
        print(f"due to {str(es)}")

'''
Function to check user in the database and login
'''
def user_login(username,password):
    

    try:
        
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        sql = "SELECT * FROM users WHERE username = %s"
        
            
        mytuple = (username)

        cur.execute(sql,mytuple)
        
        records = cur.fetchall()
        
        decrypt_pw = ""
        
        # check if username exist in data base
        
        if cur.rowcount >=1:
            for row in records:
                # print(row[4])
                decrypt_pw = row[3]    # get encrypted password of corresponding username 
                
            decrypt_pw = decrypt(decrypt_pw)     # decrypt that encrypted password
            

            if decrypt_pw == password : # row already exist  now you can login
                print(" Now you can login")
                return 1
            
            else :        # row do not exist, cant login
                print("Incorrect password")
                return 0
            
        else:
            print(" User not found")
            return 0
        
        con.close()
    except Exception as es:
        print("Error: ", str(es))
        return 0



def online(username):
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        
        sql = "UPDATE users SET online = %s  WHERE username = %s "
        
        mytuple = (
            1,
            username
        )

        cur.execute(sql,mytuple)
        con.commit()
        con.close()
        return 1
        
    except Exception as es:
        print(f"due to {str(es)}")
        return 0



'''
Function to return the username list
'''
def fetch_all_users():
    print("Fetching all users...")
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        sql = "SELECT username FROM users"
        cur.execute(sql)

        users = cur.fetchall()
        user_list = []
        # (('c',), ('nb',), ('pranshu.kumar',), ('sb',))
        for user in users:
            user = user[0]
            user_list.append(user)

        print("Fetching Done!")
        return user_list

    except Exception as es:
        print(f"due to {str(es)}")
        print("Failed! :(")
        return 0

    print("Fetching all users done!")


'''
Function to Publish Post
'''
def publish_post(author, title, content, published_at, ownership):
    print("Adding Post to database...")
    # print(ownership)
    # print(type(ownership))
    try:   #database connectivity
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        cur.execute("insert into posts (author, title, content, published_at, ownership) values(%s,%s,%s,%s,%s)", 
            ( 
                author, 
                title, 
                content,
                published_at,
                ownership
            )) 
        con.commit()
        con.close()

        print("Post added to database!")
        return 1
    
    except Exception as es:# store message in the database
        print(f"due to {str(es)}")
        print("Post publishing failed! :(")
        return 0


'''
Function to fetch posts
'''
def fetch_posts(username):
    print("Fetching posts...")
    
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()

        sql = "SELECT * FROM posts WHERE author = %s"
        mytuple = (username)
        cur.execute(sql, mytuple)
        
        posts = cur.fetchall()
        # print(posts)

        post_list = []
       

        for post in posts:
            username = post[0]
            title = post[1]
            content = post[2]
            datetime = str(post[3])
            ownership = post[4]
            
            post_list.append([username, title, content, datetime, ownership])

        print("Fetching Done!")

        return post_list
    except Exception as es:
        print(f"due to {str(es)}")
        print("Post fetching failed! :(")
        return 0


'''
Function to fetch user posts
'''
def fetch_user_posts(username):
    print("Fetching posts...")
    
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()

        sql = "SELECT * FROM posts WHERE author = %s"
        mytuple = (username)
        cur.execute(sql, mytuple)
        
        posts = cur.fetchall()
        # print(posts)

        post_list = []
       

        for post in posts:
            username = post[0]
            title = post[1]
            content = post[2]
            datetime = str(post[3])
            ownership = post[4]
            if ownership == 0:
                post_list.append([username, title, content, datetime, ownership])

        print("Fetching Done!")

        return post_list
    except Exception as es:
        print(f"due to {str(es)}")
        print("Post fetching failed! :(")
        return 0


'''
Fetch Searched user
'''
def fetch_user(search_username):
    print("Fetching searched user...")

    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()

        sql = "SELECT username FROM users WHERE username = %s"
        
        mytuple = (
            search_username
        )
        cur.execute(sql, mytuple)

        user = cur.fetchall()
        
        user = user[0][0]
        
        return user

    except Exception as es:
        print(f"due to {str(es)}")
        print("User fetching failed! :(")
        return 0
    
    
    ###################
    #######Friends
    ##################
    
    
    # user name to id
def user_to_id(username):
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
    
        sql = "SELECT id FROM users WHERE username = %s"
        
        mytuple = (
            username
        )
        cur.execute(sql, mytuple)

        user = cur.fetchall()

        id1 = 0 
        id1 = user[0][0]
        print(id1)
        return id1
     
    except Exception as es:
        print(f"due to {str(es)}")
    

# convert set to list

def set_to_name_list(set1):
    ll = []
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        for i in set1:
            sql = "SELECT username FROM users WHERE id = %s"
            
            mytuple = (
                i
            )
            cur.execute(sql, mytuple)

            user = cur.fetchall()
            if cur.rowcount >=1 :
                # print(user[0])
                
                ll.append(user[0][0])
            else :
                break
            
        print(ll)
        
        return ll  
     
    except Exception as es:
        print(f"due to {str(es)}")
        

def namelist_to_dict(list1):
    dict = {}
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        for i in list1:
            sql = "SELECT * FROM users WHERE username = %s"
            
            mytuple = (
                i
            )
            cur.execute(sql, mytuple)

            user = cur.fetchall()
            if cur.rowcount >=1 :
                # print(user[0])
                dict.update({user[0][2]:user[0][5]})
                
            else :
                break
            
        print(dict)
        
        return dict 
     
    except Exception as es:
        print(f"due to {str(es)}")
        









def not_connected(user_one_id):
    
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        
        # all possible connection of user logged in here it is user_one_id
        sql = "SELECT * FROM relationship WHERE (user_one_id = %s OR user_two_id = %s )" 
        mytuple = (
                user_one_id, user_one_id
            )
        cur.execute(sql,mytuple)
        
        # print(cur.rowcount)
        
        records = cur.fetchall()
        
        connected = set()
        
        for row in records:
            connected.add(row[0])
            connected.add(row[1])
            # print(row)
            
        # print(connected)
        
        # print("sep \n")

        # list of all users
        cur.execute("SELECT * FROM users")
        records2 = cur.fetchall()
        all_users = set()
        for row1 in records2:
            all_users.add(row1[4])
            # print(row1)
            
            
        not_connected_set= set()
        not_connected_set = all_users - connected  # total list - connected ones
        print(not_connected_set)
        # return list 
        ll = set_to_name_list(not_connected_set)
        return ll
            
    
    except Exception as es:
        print(f"due to {str(es)}")
        


def fr_sent_na(user_one_id):
    
    
    
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        sql = "SELECT * FROM relationship WHERE user_one_id = %s AND status = %s"
            
        mytuple = (
                user_one_id, 0 
            )

        cur.execute(sql,mytuple)
    
        
        # print(cur.rowcount)
        
        records = cur.fetchall()
        
        mylist = set()
        
        for row in records:
            mylist.add(row[1])
            
            # print(row)
            
        print(mylist)
        # return list 
        ll = set_to_name_list(mylist)
        return ll
        
        # cur.rowcount
        
    except Exception as es:
        print(f"due to {str(es)}")
        

def pending_requested_list(user_one_id):
    
    
    
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        sql = "SELECT * FROM relationship WHERE user_two_id = %s AND status = %s"
            
        mytuple = (
                user_one_id, 0
            )

        cur.execute(sql,mytuple)
    
        
        # print(cur.rowcount)
        
        records = cur.fetchall()
        
        mylist = set()
        
        for row in records:
            mylist.add(row[0])
            
            # print(row)
            
        print(mylist)
        # return list 
        ll = set_to_name_list(mylist)
        return ll
        
        # cur.rowcount
        
    except Exception as es:
        print(f"due to {str(es)}")
        
def friend_list(user_one_id):
    
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        sql = "SELECT * FROM relationship WHERE (user_one_id = %s OR user_two_id = %s ) AND status = %s"
            
        mytuple = (
                user_one_id, user_one_id, 1
            )

        cur.execute(sql,mytuple)
    
        
        # print(cur.rowcount)
        
        records = cur.fetchall()
        
        mylist = set()
        one = set()
        one.add(user_one_id)
        
        for row in records:
            mylist.add(row[0])
            mylist.add(row[1])
            
            # print(row)
        mylist = mylist - one
        print(mylist)
        # return list 
        ll = set_to_name_list(mylist)
        dict1 = namelist_to_dict(ll)
        print(dict1)
        return dict1
        
        # cur.rowcount
        
    except Exception as es:
        print(f"due to {str(es)}")
        
        
def send_req(user_one_id , user_two_id):
        
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        cur.execute("insert into relationship (user_one_id,user_two_id, status , action_user) values(%s,%s,%s,%s)", 
            ( 
                user_one_id,user_two_id, 0 , user_one_id
                
            )) 
        con.commit()
        con.close()
        return 1
    
    except Exception as es:
        print(f"due to {str(es)}")
        return 0
    
def accept_req(user_one_id , user_two_id):
    
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        
        sql = "UPDATE relationship SET status = %s ,  action_user = %s WHERE user_one_id = %s AND user_two_id = %s"
        
        mytuple = (
            1,
            user_one_id ,
            user_two_id,
            user_one_id 
        )

        cur.execute(sql,mytuple)
        con.commit()
        con.close()
        return 1
        
    except Exception as es:
        print(f"due to {str(es)}")
        return 0
    
def logout(username):
    try: 
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        
        sql = "UPDATE users SET online = %s  WHERE username = %s "
        
        mytuple = (
            0,
            username
        )

        cur.execute(sql,mytuple)
        con.commit()
        con.close()
        return 1
        
    except Exception as es:
        print(f"due to {str(es)}")
        return 0
        

'''
Function to store messages
'''
def store_message(username, send_to, message, read_bool, published_at):
    print("Storing Message")

    try:   #database connectivity
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        cur.execute("insert into messages (sender, receiver, message, timestamp, read_bool) values(%s,%s,%s,%s,%s)", 
            ( 
                username, 
                send_to, 
                message,
                published_at,
                read_bool
            )) 
        con.commit()
        con.close()

        print("Message added to database!")
        return 1
    
    except Exception as es:# store message in the database
        print(f"due to {str(es)}")
        print("Storing Message Failed! :(")
        return 0


'''
Function to get all the messages
'''
def fetch_chat(username, send_to):
    print("Fetching Chat with user", send_to)

    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()

        sql = "SELECT * FROM messages WHERE (sender = %s AND receiver = %s) OR (sender = %s AND receiver = %s)"
        mytuple = (
            username,
            send_to,
            send_to,
            username
        )
        cur.execute(sql, mytuple)
        
        messages = cur.fetchall()
        # print(messages)

        message_list = []
       

        for message in messages:
            sender = message[0]
            message = message[2]
            read_bool = 1
            message = sender + ": " + message
            message_list.append([message, read_bool])

        print(message_list)

        print("Fetching Done!")

        return message_list
    except Exception as es:
        print(f"due to {str(es)}")
        print("Message fetching failed! :(")
        return 0

    
    