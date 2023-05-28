import csv,os
from datetime import datetime

def createCSVfile(today, time):
	headers = ['ID', 'Insertion Time', 'Name', 'Address', 'Phone Number', 'Email']
	# records = [{'id':'1', 'iTime':time, 'name': 'Bakr', 'address':'zagazig', 'pNumber':'00201020205040', 'email':'engdiaa@gmail.com'},]

	with open(f"./contacts/contactbook_{today}.csv",'w') as file:
		csvWriter = csv.writer(file, delimiter=',')
		csvWriter.writerow(headers)
		name = input(f"Please enter The new {headers[2]} field\n").capitalize()
		address = input(f"Please enter The new {headers[3]} field\n").capitalize()
		pNumber = input(f"Please enter The new {headers[4]} field\n").capitalize()
		email = input(f"Please enter The new {headers[5]} field\n").capitalize()
		csvWriter.writerow([1, time, name, address, pNumber, email])

def appendCSVfile(today, time):
	headers = ['ID', 'Insertion Time', 'Name', 'Address', 'Phone Number', 'Email']
	lindex = 0
	with open(f"./contacts/contactbook_{today}.csv",'r') as file:
		csvSearch = csv.reader(file, delimiter=',')
		lindex = int(list(csvSearch)[-1][0]) + 1
	with open(f"./contacts/contactbook_{today}.csv",'a') as file:
		csvWriter = csv.writer(file, delimiter=',')
		name = input(f"Please enter The new {headers[2]} field\n").capitalize()
		address = input(f"Please enter The new {headers[3]} field\n").capitalize()
		pNumber = input(f"Please enter The new {headers[4]} field\n").capitalize()
		email = input(f"Please enter The new {headers[5]} field\n").capitalize()
		csvWriter.writerow([lindex, time, name, address, pNumber, email])

def createContact():
	contents = os.listdir('./contacts')
	today = datetime.now().strftime("%d-%m-%y")
	time = datetime.now().strftime("%H:%M:%S")
	if f"contactbook_{today}.csv" in contents:
		appendCSVfile(today, time)
	else:
		createCSVfile(today, time)
	print('*****************************************')
	print('Contact Created Succesfully')

def readCSVfile():
	today = datetime.now().strftime("%d-%m-%y")
	with open(f"./contacts/contactbook_{today}.csv",'r') as file:
		csvSearch = list(csv.reader(file, delimiter=','))
		print('*****************************************')
		print('Choose which kind of order you prefer (please enter the number only)')
		print('1.ID order (Creation date order)')
		print('2.Alphabetical name order')
		i = int(input())
		while i > 3 or i < 1:
			print('Please enter only one of mentioned Numbers')
			print('Choose which kind of order you prefer (please enter the number only)\n1.ID order\n2.Alphabetical order\n3.Creation date order')
			i = int(input())
		if i == 2:
			x = csvSearch.pop(0)
			csvSearch.sort(key=lambda x: x[2])
			csvSearch.insert(0, x)
		for row in csvSearch:
			if len(row)>0:
				print(*row, sep=" / ")

def deleteContact():
	[today, csvSearch, rowN] = findContact()
	if today == None:
		return None
	# del myList[2]
	id = rowN
	del csvSearch[rowN]
	for row in range(rowN,len(csvSearch)):
		csvSearch[row][0] = id
		id+=1
	with open(f"./contacts/contactbook_{today}.csv",'w') as file:
		for row in csvSearch:
			csvWriter = csv.writer(file, delimiter=',')
			csvWriter.writerow(row)
	print('*****************************************')			
	print('Contact Deleted Succesfully')

def editContact():
	[today, csvSearch, rowN] = findContact()
	if today == None:
		return None
	headers = ['ID', 'Insertion Time', 'Name', 'Address', 'Phone Number', 'Email']
	# Editing
	print(f'this is old {headers[2]}: {csvSearch[rowN][2]}')
	csvSearch[rowN][2] = input(f"Please enter The new {headers[2]} field\n").capitalize()
	print(f'this is old {headers[3]}: {csvSearch[rowN][3]}')
	csvSearch[rowN][3] = input(f"Please enter The new {headers[3]} field\n").capitalize()
	print(f'this is old {headers[4]}: {csvSearch[rowN][4]}')
	csvSearch[rowN][4] = input(f"Please enter The new {headers[4]} field\n").capitalize()
	print(f'this is old {headers[5]}: {csvSearch[rowN][5]}')
	csvSearch[rowN][5] = input(f"Please enter The new {headers[5]} field\n").capitalize()
	with open(f"./contacts/contactbook_{today}.csv",'w') as file:
		for row in csvSearch:
			csvWriter = csv.writer(file, delimiter=',')
			csvWriter.writerow(row)
	print('*****************************************')
	print('Contact Edited Succesfully')

def findContact():
	# just editing first name but I want it dynamic for any field based on user
	today = datetime.now().strftime("%d-%m-%y")
	headers = ['ID', 'Insertion Time', 'Name', 'Address', 'Phone Number', 'Email']
	eField = int(input(f"Which field do you want to search (please enter the number)\n0.ID\n1.Insertion Time\n2.Name\n3.Address\n4.Phone Number\n5.Email\n"))
	while eField > (len(headers)-1) or eField < 0:
		print('Please enter only one of mentioned Numbers')
		eField = int(input(f"Which field do you want to search (please enter the number)\n0.ID\n1.Insertion Time\n2.Name\n3.Address\n4.Phone Number\n5.Email\n"))
	cData = input(f"Please enter The current {headers[eField]} field\n")
	rowN = 0
	with open(f"./contacts/contactbook_{today}.csv",'r') as file:
		csvSearch = csv.reader(file, delimiter=',')
		# unfortunately every row can be read only once then be deleted from csvSearch, this is how csv work but you can solve it by converting csvSearch to list --> list(csvSearch)
		csvSearch = list(csvSearch)
		isFound = False
		for row in csvSearch:
			# We are searchin here for just only first match
			if cData.lower() in row[eField].lower():
				print(*row, sep=" / ")
				isFound = True
				break
			rowN+=1
			if row == csvSearch[-1]:
				print(f"the {headers[eField]} you entered doesn't exist")
				return [None,None,None]
		if isFound == True:
			return [today, csvSearch,rowN]



if __name__ == '__main__' :
	while True:
		print('*****************************************')
		print('Please select what you want to do:')
		print('1.create Contact')
		print('2.List All Contacts')
		print('3.Find First Match Contact')
		print('4.Edit First Match Contact')
		print('5.Delete First Match Contacts')
		i = input(f"6.Exit\n")
		if i == '1':
			createContact()
		elif i == '2':
			readCSVfile()
		elif i == '3':
			findContact()
		elif i == '4':
			editContact()
		elif i == '5':
			deleteContact()
		elif i == '6':
			break
		else:
			print('*****************************************')
			print('Please enter only one of mentioned Numbers')
	print('*****************************************')
	print('See You Later 👋👋👋')
	print('*****************************************')
