import pymysql

def user_register(fname, lname, username, user_password):
    
    try:   #database connectivity
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "miniface")
        cur = con.cursor()
        cur.execute("insert into users (fname,lname,username,user_password) values(%s,%s,%s,%s)", 
            ( 
                fname, 
                lname, 
                username,
                user_password
            )) 
    
        sql = "SELECT * FROM users WHERE fname = %s AND lname = %s AND username = %s AND user_password = %s"
        
        mytuple = (
            fname,
            lname,
            username,
            user_password
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
    sql = "SELECT * FROM users WHERE username = %s AND user_password = %s"
        
    mytuple = (
        
        username,
        password
    )

    cur.execute(sql,mytuple)

    # print ("%d rows were returned" % (cur.rowcount))

    if cur.rowcount >=1 :    # row already exist  now you can login
        print(" Now you can login")
        return 1
    
    else :        # row do not exist, cant login
        print(" User not found")
        return 0
    

    con.close()
    

'''
Function for user logout
'''

def user_logout():
    pass


'''
Function to return the username list
'''
def fetch_users():
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