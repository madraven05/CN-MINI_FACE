import pymysql

def user_register(self):
    
    try:   #database connectivity
        con = pymysql.connect(host = "localhost", user = "root", password ="", database = "mydata")
        cur = con.cursor()
        cur.execute("insert into data (entry1, entry2,entry3,entry4) values(%s,%s,%s,%s)", 
            ( self.txt_entry1.get(),
                self.txt_entry2.get(),
                self.txt_entry3.get(),
                self.txt_entry4.get()

            )) 
    
        sql = "SELECT * FROM data WHERE entry1 = %s AND entry2 = %s AND entry3 = %s AND entry4 = %s"
        
        mytuple = ( self.txt_entry1.get(),
            

            self.txt_entry2.get(),
                self.txt_entry3.get(),
                self.txt_entry4.get() )

        cur.execute(sql,mytuple)

        print ("%d rows were returned" % (cur.rowcount-1))

        

        if cur.rowcount<=1 :  #user doesn't exist, insert new entry
            con.commit()
            con.close()
            messagebox.showinfo("Success", parent= self.root)

        else :     # user already exist
            messagebox.showinfo("Error", "This user profile already exist", parent= self.root)

    except Exception as es:
        messagebox.showerror("Error ", f"due to {str(es)}", parent = self.root)

'''
Function to check user in the database and login
'''
def user_login(login_info):
    print(login_info)

'''
Function for user logout
'''
def user_logout():
    pass