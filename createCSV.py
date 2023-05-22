import csv

def createCSVfile():
		records = [
				{'id':'1', 'fName':'Ahmed', 'lName': 'Bakr'},
				{'id':'2', 'fName':'Shiko', 'lName': 'Toty'},
				{'id':'3', 'fName':'Liko', 'lName': 'Mody'},
				{'id':'4', 'fName':'Loky', 'lName': 'Ascencsio'},
		]
		with open('record.csv','w') as file:
			csvWriter = csv.writer(file, delimiter=',')
			csvWriter.writerow(['ID','First Name','Last Name'])
			for record in records:
					csvWriter.writerow([record['id'],record['fName'],record['lName']])

def readCSVfile():
	with open('record.csv','r') as file:
		for row in csv.reader(file, delimiter=','):
			if len(row)>0:
				print(f'{row[0]} {row[1]} {row[2]}')

def appendCSVfile():
	with open('record.csv','a') as file:
		csvWriter = csv.writer(file, delimiter=',')
		csvWriter.writerow(['5', 'Emee', 'Diaa'])

def searchCSVfile():
	fName = input(f"please enter first contact name\n")
	with open('record.csv','r') as file:
		csvSearch = csv.reader(file, delimiter=',')
		for row in csvSearch:
			if row[1].lower() == fName.lower():
				x = input(f"please enter the new first name").capitalize()
				csvWriter = csv.writer(file, delimiter=',')
				csvWriter.writerow([row[0], x, row[2]])



if __name__ == '__main__' :
	searchCSVfile()