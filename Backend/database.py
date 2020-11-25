import pymysql
from cryptography.fernet import Fernet





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
        cur.execute("insert into users (fname,lname,username,encrypt_pw) values(%s,%s,%s,%s,%s)", 
            ( 
                fname, 
                lname, 
                username,
                encrypt_pw
                
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
def publish_post(author, title, content, published_at):
    print("Adding Post to database...")
    try:   #database connectivity
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        cur.execute("insert into posts (author, title, content, published_at) values(%s,%s,%s,%s)", 
            ( 
                author, 
                title, 
                content,
                published_at
            )) 
        con.commit()
        con.close()

        print("Post added to database!")
        return 1
    
    except Exception as es:
        print(f"due to {str(es)}")
        print("Post publishing failed! :(")
        return 0


'''
Function to fetch posts
'''
def fetch_posts():
    print("Fetching posts...")
    
    try:
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()

        sql = "SELECT * FROM posts"
        cur.execute(sql)
        
        posts = cur.fetchall()
        # print(posts)

        post_list = []
        # (('neel', 'password', 'encryption', datetime.datetime(2020, 11, 25, 18, 27, 25)), 
        # ('neel ', 'done', 'done', datetime.datetime(2020, 11, 25, 18, 37, 24)), 
        # ('sagar', 'mynewpost', 'uploaded', datetime.datetime(2020, 11, 25, 18, 40, 46)), 
        # ('sagar', 'ghbjnkm', 'cgvhbjnk', datetime.datetime(2020, 11, 25, 19, 23, 47)))

        for post in posts:
            username = post[0]
            title = post[1]
            content = post[2]
            datetime = str(post[3])
            
            post_list.append([username, title, content, datetime])

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