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
    # Sagar add here the database methods to 
    # search the databse for a match for username and password
    # if exists return 1
    # else return 0

    # Also, I have added a file miniface.sql
    # Just import this file in localhost/phpmyadmin
    # It will create the entire database!

'''
Function for user logout
'''
def user_logout():
    pass