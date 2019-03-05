import re
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
import lxml
import csv
import os
import pandas
from tkinter import messagebox
from tkinter import simpledialog

print()
print()
print("                  00000000000")
print("                00000000000000")
print("               0000000000000000")
print("              0000          0000")
print("              0000           0000")
print("                             0000")
print("                   000000000 0000")
print("                 0000000000000000")
print("              000000       000000")
print("              0000           0000")
print("              0000   00000   0000")
print("              0000   00000   0000")
print("              0000   00000   0000")
print("              0000           0000")
print("               000000      000000")
print("                 00000000000000")
print("                   0000000000")
print()
print()
print("        0000                          000") 
print("        0   0     0     000   00000      0")
print("        0000     0 0    0  0    0      00") 
print("        0       00000   000     0        0")
print("        0      0     0  0  0    0     000")
print()

def consultingAreasList(folderName,haveList,window):
	# folderName = input('Enter the project folder name:')
	cwd = os.getcwd()
	path = '%s/%s' %(cwd,folderName)
	os.chdir(path)
	
	# haveList = input("Do you already have a .csv file of consulting areas by librarian? Answer 'yes' or 'no':")
	haveList_negative = ['no','n','NO','No','N','nope','Nope','NOPE','not a one']

	if haveList in haveList_negative:
		print("")
		print("Okay, we'll make a list now. For each department in the publications list, you'll enter the consulting librarian. If there isn't a consulting librarian, enter none.") 
		messagebox.showinfo("Part 3: Making the list","Okay, we'll make a list now. \n\nFor each department in the publications list, you'll enter the consulting librarian. If there isn't a consulting librarian, enter none.",parent=window)


		# question = "Okay"
		# part3.updateScreen(question)

		print("You'll only need to do this once.")
		print("")
		departmentList = []
		##CREATES A LIST OF CONSULTING AREAS BASED ON THE PUBLICATION FILE
		consultingAreas = open('consultingAreas.csv','w',newline='')
		fieldnames = ['department','librarianInitials']
		consultingAreasWriter = csv.DictWriter(consultingAreas,delimiter=',',fieldnames=fieldnames)
		consultingAreasWriter.writeheader()

		with open('oaStatus.csv','r') as oaStatus:
			oaStatusReader = csv.DictReader(oaStatus,delimiter=',')
			for row in oaStatusReader:
				department = row['department']
				if department not in departmentList:
					part1 = "Enter initials for the consulting librarian to"
					part2 = department
					initialsInput = part1+' '+part2+':'
					librarianInitials =  simpledialog.askstring("Part 3: Assigning librarians",initialsInput)
					departmentList.append(department)
					consultingAreasWriter.writerow({'department':department,'librarianInitials':librarianInitials})
					caList = 'consultingAreas'
				else:
					pass
		consultingAreas.close()

	else:
		caList = simpledialog.askstring("Part 3: Assigning librarians","Great! We'll use that. Make sure the list is in the project folder. \n\nEnter the name of the list file:") 
	makeMaster(caList)

def makeMaster(caList):
	csv1 =pandas.read_csv('oaStatus.csv')
	csv2 = pandas.read_csv('%s.csv' %(caList))

	merged = csv1.merge(csv2,left_on='department',right_on='department',how='inner')
	merged.to_csv('oaMaster.csv',index=False)

	separateLists = messagebox.askyesno("Part 3: Separate lists", "Would you like a list separated by consulting librarian? Answer 'yes' or 'no':")
	# separateLists_negative = ['no','n','NO','No','N','nope','Nope','NOPE','not a one']
	# if separateLists not in separateLists_negative:
	if separateLists == True:
	##READS LIST, CREATES ONE CSV FILE PER LIBRARIAN, WRITES PUBLICATION INFORMATION TO EACH FILE	
		librarianInitials_list = []

		with open('oaMaster.csv','r') as oaMaster:
			oaMasterReader = csv.DictReader(oaMaster,delimiter=',')
			for row in oaMasterReader:
				pubID = row['pubID']
				firstName = row['firstName']
				lastName = row['lastName']
				department = row['department']
				category = row['category']
				activityScope = row['activityScope']
				journalTitle = row['journalTitle']
				month = row['month']
				issueNumber = row['issueNumber']
				pages = row['pages']
				articleTitle = row['articleTitle']
				volume = row['volume']
				year = row['year']
				issn = row['issn']
				prearchiving = row['prearchiving']
				postarchiving = row['postarchiving']
				prerestriction = row['prerestriction']
				postrestriction = row['postrestriction']
				pdfversion = row['pdfversion']
				conditions = row['conditions']
				eissn = row['eissn']
				eprearchiving = row['prearchiving']
				epostarchiving = row['epostarchiving']
				eprerestriction = row['eprerestriction']
				epostrestriction = row['epostrestriction']
				epdfversion = row['epdfversion']
				econditions = row['econditions']
				librarianInitials = row['librarianInitials']

				with open('%s.csv' %(librarianInitials + '_' + 'publications'),'a',newline='') as librarianPublicationList:
					fieldnames = ['pubID','firstName','lastName','department','category','activityScope','journalTitle','month','issueNumber','pages','articleTitle','volume','year','issn','prearchiving','postarchiving','prerestriction','postrestriction','pdfversion','conditions','eissn','eprearchiving','epostarchiving','eprerestriction','epostrestriction','epdfversion','econditions']
					librarianPublicationList_writer = csv.DictWriter(librarianPublicationList,delimiter=',',fieldnames=fieldnames)
					
					##CREATES ONE FILE PER LIBRARIAN AND WRITES THE FIRST PUBLICATION ASSIGNED TO A LIBRARIAN TO THE FILE.
					##for each publication after the first, it skips this step and appends the existing file.
					if librarianInitials not in librarianInitials_list:
						librarianInitials_list.append(librarianInitials)							

						librarianPublicationList_writer.writeheader()
						librarianPublicationList_writer.writerow({'pubID':pubID,'firstName':firstName,'lastName':lastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':journalTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':articleTitle,'volume':volume,'year':year,'issn':issn,'eissn':eissn,'prearchiving':prearchiving,'postarchiving':postarchiving,'prerestriction':prerestriction,'postrestriction':postrestriction,'pdfversion':pdfversion,'conditions':conditions,'eprearchiving':eprearchiving,'epostarchiving':epostarchiving,'eprerestriction':eprerestriction,'epostrestriction':epostrestriction,'epdfversion':epdfversion,'econditions':econditions})
					##WRITES PUBLICATIONS TO FILES BY LIBRARIAN						
					else:
						librarianPublicationList_writer.writerow({'pubID':pubID,'firstName':firstName,'lastName':lastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':journalTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':articleTitle,'volume':volume,'year':year,'issn':issn,'eissn':eissn,'prearchiving':prearchiving,'postarchiving':postarchiving,'prerestriction':prerestriction,'postrestriction':postrestriction,'pdfversion':pdfversion,'conditions':conditions,'eprearchiving':eprearchiving,'epostarchiving':epostarchiving,'eprerestriction':eprerestriction,'epostrestriction':epostrestriction,'epdfversion':epdfversion,'econditions':econditions})					
		messagebox.showinfo("Part 3: Lists made!","The project folder now contains one master list and lists separated by librarian.")
	else:
		messagebox.showinfo("Part 3: List made!","Okay! masterOA.csv has all the information you need.")
		pass




## This all works
# csv1 =pandas.read_csv('oaStatus.csv')
# csv2 = pandas.read_csv('consultingAreas.csv')

# merged = csv1.merge(csv2,left_on='department',right_on='department',how='inner')
# merged.to_csv('oaMaster.csv',index=False)
# # for row in merged:
# # 	librarianInitials = row['librarianInitials']
# # 	row.to_csv('%s.csv' %(librarianInitials))