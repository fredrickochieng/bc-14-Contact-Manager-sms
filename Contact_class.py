import sqlite3
import sys
from tabulate import tabulate#for tabling
class Contact(object):
	def __init__ (self):
		connection=sqlite3.connect(contact.db)
		connection.execute('''CREATE TABLE IF NOT EXISTS CONTACT (
			ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
			SUB_NAME TEXT NOT NULL,
			PHONE_NUM INT NOT NULL) 
		''')
		connection.commit()
		connection.close()
		def addContact(self,name,number):
			connection=sqlite3.connect("contact.db")
			connection.execute("INSERT INTO CONTACT (NAME, PHONE_NUM)  VALUES ('{}', '{}')" .format(name, number));
			connection.commit()
			connection.close()
			return "Number added successfully"
def search_contact(self,name):
	connection=sqlite3.connect("contact.db")
	cursor=connection.execute("SELECT * from CONTACT WHERE NAME='{}'" .format(name));
	info=cursor.fetchall()
	if not len(info):
		return "No such contact with name %s" %name
	elif len(info)>1:
		print "Which %s" %name, "?"
		searched_name=[]
		for row in info:
			each_row=[]
			each_row.append("[" + str(data[0]) + "]")
			each_row.append(row[1])
			each_row.append(row[2])
			searched_name.append(each_row)
			print tabulate(searched_name,headers=["ID", "NAME", "NUMBER"])
			option=input("Please search by number ")
			if option>searched_name[len(searched_name)-1[0]] or option<=0:
				return "invalid"
			else :
					searched_name=[]
					for row in info:
						each_row=[]
						each_row.append(data[1])
						each_row.append(data[2])
						searched_name.append(each_row)
						return tabulate(searched_name,headers=["Name", "Number"])
						connection.close()
def send_text(name,message):
	connection=sqlite3.connect("contact.db")
	cursor = connection.execute("SELECT * from CONTACT WHERE NAME='{}'" .format(name)); 
	info=cursor.fetchdata()
	if not len(info):
		return "Please add the number you want to send sms to"
	elif len(info)>1:
		print "Please select the name you want to text"
		searched_name=[]
		for data in info:
			each_data=[]
			each_data.append("[" + str(data[0])+ "]")
			each_data.append(data[1])
			each_data.append(data[2])
			searched_name.append(each_data)
			print tabulate(searched_name, headers=["ID", "Name", "Number"])
			option=input("Please enter the number corresponding to the person")
			if option>searched_name[len(searched_name)-1][0] or option<=0:
				return "Wrong selection"
			else:
				n_cursor=connection.execute("SELECT PHONE_NUM from contact where ID ='{}'".format(choice))
				searched_number=n_cursor.fetchall()
				print "Please wait while your message is being sent to %s %d" %(name,searched_number[0][0] + "...")
				send_text(searched_number,message)
		else:
				entered_number=info[0][2]
				print "Please wait while your mesage is being sent to %s %d" %(name,entered_number)
				send_text(entered_number,message)

	
	












    #firstname = ""
    #lastname =""
    #phone =""
    #email =""
    #def addContact():
    	#contact=Contact()
    	#contact.firstname=input("Please enter your first name: ")
    	#contact.lastname=input("Please enter your last name: ")
    	#contact.phone=input("Please enter your pnone number: ")
    	#contact.email=input("Please enter your Email address: ")
    	#con= sqlite3.connect("Contact.db")
    	#with con:
			#cur=con.cursor()
			#cur.execute("DROP TABLE IF EXISTS Contact")
			#cur.execute("CREATE TABLE Contact (firstname TEXT, lastname TEXT, Phone TEXT, Email TEXT);")
			#cur.execute("INSERT INTO Contact VALUES (?, ?, ?, ?);", (firstname, lastname, phone,email))
			#cur.commit()
			#get user input
			#print ("Please enter a new contact")
			#print("")
			#firstname=input("Please enter your first name:")
			#lastname=input("Please enter your last name:")
			#phone=input("Please enter your pnone number")
			#email=input("Please enter your Email address")
			#createnewdb=input("To create a new database,kindly enter 1:")
			#if createnewdb==1:
				#addContact()
			#else:
				#sys.exit(0)
#if __name__ == '__main__':
	#addContact()