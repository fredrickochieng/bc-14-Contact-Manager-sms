import sqlite3
from messenger import send_message
from tabulate import tabulate



class ContactManager(object):#this class creates a database 

	def __init__(self):

		conn = sqlite3.connect('contacts_v1.db')
		conn.execute('''CREATE TABLE IF NOT EXISTS CONTACTS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
		NAME TEXT NOT NULL,
		PHONE_NUM TEXT NOT NULL) 
		''')

		conn.commit()
		conn.close()

	


	def add_new(self, name, number):#populates the database table with required values
		conn = sqlite3.connect('contacts_v1.db')
		conn.execute("INSERT INTO CONTACTS (NAME, PHONE_NUM)  VALUES ('{}', '{}')" .format(name, number));

		conn.commit()
		conn.close()

		return 'Contact added successfully'
	def search_for_contact(self, name):
		conn = sqlite3.connect('contacts_v1.db')
		cursor = conn.execute("SELECT * from CONTACTS WHERE NAME='{}'" .format(name));
		
		data = cursor.fetchall()

		if not len(data):
			return 'No such contact found '
		elif len(data) > 1:

			print "Which %s" %name, "?" 

			results = []
			for row in data:
				each_row = []
				
				each_row.append('[' + str(row[0]) + ']')
				each_row.append(row[1])
				each_row.append(row[2])
				results.append(each_row)

			print tabulate(results, headers=["ID", "Name", "Number"])

			response = input("Kindly respond with a number ")

			if response > results[len(results)-1][0] or response <= 0:
				return 'Your response is invalid'
			else:
				new_cursor = conn.execute("SELECT NAME from CONTACTS WHERE ID='{}'" .format(response))
				theNumber = new_cursor.fetchall()
				return theNumber[0][0]

		else:

			results = []
			for row in data:
				each_row = []
				
				each_row.append(row[1])
				each_row.append(row[2])
				results.append(each_row)

			return tabulate(results, headers=["Name", "Number"])

		conn.close()


def send_text(name, message):
	conn = sqlite3.connect('contacts_v1.db')
	cursor = conn.execute("SELECT * from CONTACTS WHERE NAME='{}'" .format(name)); 		

	data = cursor.fetchall()

	if not len(data):
		return 'Contact not in the database!Kindly add the contact you want to send a message to : '
	elif len(data) > 1:
		print "Which %s" %name, "do you want to send a messege to : ?" 

		results = []
		for row in data:
			each_row = []
			
			each_row.append('[' + str(row[0]) + ']')
			each_row.append(row[1])
			each_row.append(row[2])
			results.append(each_row)

		print tabulate(results, headers=["ID", "Name", "Number"])

		response = input("Kindly respond with a number :")

		if response > results[len(results) - 1][0] or response <= 0:
			return 'Invalid response'
		else:
			new_cursor = conn.execute("SELECT PHONE_NUM from CONTACTS WHERE ID='{}'" .format(response))

			theNumber = new_cursor.fetchall()
			print "\nPlease wait while your message is being sent to %s %s" %(name,theNumber[0][0]) + "..."

			print theNumber[0][0]
			send_message(theNumber[0][0], message)
	else:
			to_number = data[0][2]
			print "\nPlease wait while your message is being sent to %s %s" %(name, int (to_number))
			send_message(to_number, message)
if __name__ == '__main__':
	instance = ContactManager()
	#instance.add_record('fred', '0977666')
	#instance.sync_to_firebase("fred","07198034")
	#instance.search_record('matt')
	
	