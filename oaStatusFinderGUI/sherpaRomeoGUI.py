import re
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
import lxml
import csv
import os
import pandas
import shutil

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
print("        0000                           00") 
print("        0   0     0     000   00000   0  0")
print("        0000     0 0    0  0    0       0") 
print("        0       00000   000     0      0")
print("        0      0     0  0  0    0     0000")
print()


# folderName = input('Enter the project folder name:')
# sherpaRomeoAK = input('Enter your SherpaRomeo access key:')

print("")
print("Querying SherpaRomeo API...")
print("")
print("This one won't take as long, but a little coffee is still nice.")
print("")
print("                      )    )")
print("                     (    (")
print("                 _________)___")
print("              .-|             |")
print("             ( C|\*/\*/\*/\*/\|")
print("              '-|             |")
print("                |             |")
print("                '_____________'")
print("                 '-----------'")
print("")

def sherpaRomeo(folderName,sherpaRomeoAK):
	firstPart2 = 'http://www.sherpa.ac.uk/romeo/api29.php?jtitle='
	lastPart2 = '&ak=' + sherpaRomeoAK

	cwd = os.getcwd()
	path = '%s/%s' %(cwd,folderName)
	os.chdir(path)

	##setting up some csv readers and writers
	journalData = open('journalData.csv','r',newline = '')
	csv_reader = csv.DictReader(journalData,delimiter=',')

	disambiguatedTitles = open('disambiguatedTitles.csv','r',newline='')
	disambiguated_reader = csv.DictReader(disambiguatedTitles,delimiter=',')
	failedQueries = open('failedQueries.csv','r',newline = '')

	retry_reader = csv.DictReader(failedQueries,delimiter=',')
	fieldnames = ['pubID','title']

	ultimateFail = open('ultimateFail.csv','a',newline='')
	fieldnames3 = ['pubID','title']
	ultimateFail_writer = csv.DictWriter(ultimateFail,delimiter=',',fieldnames=fieldnames3)
	ultimateFail_writer.writeheader()

	##setting up some counters
	totalTitles = 0
	ultimateFail_count = 0

	##creates output file for the Sherpa Romeo data
	with open('sherpaRomeo.csv','a',newline='') as sherpaRomeo:
		fieldnames2 = ['pubID','issn','prearchiving','postarchiving','prerestriction','postrestriction','pdfversion','conditions','eissn','eprearchiving','epostarchiving','eprerestriction','epostrestriction','epdfversion','econditions']
		writer = csv.DictWriter(sherpaRomeo, fieldnames=fieldnames2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		writer.writeheader()

		##iterates over the journalData.csv to query Sherpa Romeo for publication rights
		for row in csv_reader:
			jID = row['pubID']
			title = row['title']
			issn = row['issn']
			eissn = row['eissn']

			##if there is an issn, uses that to make a query
			if issn != '':
				qstring2 = firstPart2 + issn + lastPart2
				response = urllib.request.urlopen(qstring2,data=None,timeout=15)
				webContent = response.read()
				with open('%s.xml' %(jID + '_' + 'SR'), 'w') as f3:
					f3.write(str(webContent))
					f3.close()
				with open('%s.xml' %(jID + '_' + 'SR'),'r') as file:
					file = BeautifulSoup(file,features='lxml')
					try:
						prearchiving = file.publisher.prearchiving.string
					except:
						prearchiving = ''
					try:
						postarchiving = file.publisher.postarchiving.string
					except:
						postarchiving = ''
					try:
						prerestriction = file.publisher.prerestriction.string
					except:
						prerestriction = ''
					try:
						postrestriction = file.publisher.postrestriction.string
						if '<num>' in postrestriction:
							postrestriction = re.sub('<.*?>','',postrestriction)
						else:
							postrestriction = postrestriction.string
					except:
						postrestriction = ''
					try:
						pdfversion = file.publisher.pdfversion.string
					except:
						pdfversion = ''
					##making the conditions much more human-readable; for now, uses a workaround for encoding problems
					try:
						conditions = file.find_all("condition")
						conditions = str(conditions)
						conditions = re.sub('\[','',conditions)
						conditions = re.sub('\]','',conditions)
						conditions = re.sub('<.*?>','',conditions)
						conditions = re.sub('&lt;num&gt;','',conditions)
						conditions = re.sub('&lt;/num&gt;','',conditions)
						conditions = re.sub('&lt;period units="month"&gt;','',conditions)
						conditions = re.sub('&lt;/period&gt;','',conditions)
						conditions = re.sub("(?<=rs)\W{2}","'",conditions)
						conditions = re.sub("\W{2}(?=s)","'",conditions)
					except:
						conditions = ''
			else:
				prearchiving = ''
				prerestriction = ''
				postrestriction = ''
				postarchiving = ''
				pdfversion = ''
				conditions = ''

			##if there is an eissn, uses that to make a query
			if eissn != '':
				qstring3 = firstPart2 + eissn + lastPart2
				response = urllib.request.urlopen(qstring3,data=None,timeout=15)
				webContent = response.read()
				with open('%s.xml' %(jID + '_' + 'SRE'), 'w') as f3:
					f3.write(str(webContent))
					f3.close()
				with open('%s.xml' %(jID + '_' + 'SRE'),'r') as file:
					file = BeautifulSoup(file,features='lxml')

					try:
						eprearchiving = file.publisher.prearchiving.string
					except:
						eprearchiving = ''
					try:
						epostarchiving = file.publisher.postarchiving.string
					except:
						epostarchiving = ''
					try:
						eprerestriction = file.publisher.prerestriction.string
					except:
						eprerestriction = ''
					try:
						epostrestriction = file.publisher.postrestriction.string
						if '<num>' in epostrestriction:
							epostrestriction = re.sub('<.*?>','',postrestriction)
						else:
							epostrestriction = postrestriction.string
					except:
						epostrestriction = ''
					try:
						epdfversion = file.publisher.pdfversion.string
					except:
						epdfversion = ''
					try:
						econditions = file.find_all("condition")
						econditions = str(econditions)
						econditions = re.sub('\[','',econditions)
						econditions = re.sub('\]','',econditions)
						econditions = re.sub('<.*?>','',econditions)
						econditions = re.sub('&lt;num&gt;','',econditions)
						econditions = re.sub('&lt;/num&gt;','',econditions)
						econditions = re.sub('&lt;period units="month"&gt;','',econditions)
						econditions = re.sub('&lt;/period&gt;','',econditions)
						econditions = re.sub("(?<=rs)\W{2}","'",econditions)
						econditions = re.sub("\W{2}(?=s)","'",econditions)
					except:
						econditions = ''

			else:
				eprearchiving = ''
				eprerestriction = ''
				epostrestriction = ''
				epostarchiving = ''
				epdfversion = ''
				econditions = ''
			writer.writerow({'pubID':jID,'issn':issn,'eissn':eissn,'prearchiving':prearchiving,'postarchiving':postarchiving,'prerestriction':prerestriction,'postrestriction':postrestriction,'pdfversion':pdfversion,'conditions':conditions,'eprearchiving':eprearchiving,'epostarchiving':epostarchiving,'eprerestriction':eprerestriction,'epostrestriction':epostrestriction,'epdfversion':epdfversion,'econditions':econditions})
			totalTitles = totalTitles + 1

		##iterates over the disambiguatedTitles.csv to query Sherpa Romeo for publication rights
		for row in disambiguated_reader:
			jID = row['pubID']
			title = row['title']
			issn = row['issn']
			eissn = row['eissn']

			if issn != '':
				qstring2 = firstPart2 + issn + lastPart2
				response = urllib.request.urlopen(qstring2,data=None,timeout=15)
				webContent = response.read()
				with open('%s.xml' %(jID + '_' + 'SR'), 'w') as f3:
					f3.write(str(webContent))
					f3.close()
				with open('%s.xml' %(jID + '_' + 'SR'),'r') as file:
					file = BeautifulSoup(file,features='lxml')
					try:
						prearchiving = file.publisher.prearchiving.string
					except:
						prearchiving = ''
					try:
						postarchiving = file.publisher.postarchiving.string
					except:
						postarchiving = ''
					try:
						prerestriction = file.publisher.prerestriction.string
					except:
						prerestriction = ''
					try:
						postrestriction = file.publisher.postrestriction.string
						if '<num>' in postrestriction:
							postrestriction = re.sub('<.*?>','',postrestriction)
						else:
							postrestriction = postrestriction.string
					except:
						postrestriction = ''
					try:
						pdfversion = file.publisher.pdfversion.string
					except:
						pdfversion = ''
					try:
						conditions = file.find_all("condition")
						conditions = str(conditions)
						conditions = re.sub('\[','',conditions)
						conditions = re.sub('\]','',conditions)
						conditions = re.sub('<.*?>','',conditions)
						conditions = re.sub('&lt;num&gt;','',conditions)
						conditions = re.sub('&lt;/num&gt;','',conditions)
						conditions = re.sub('&lt;period units="month"&gt;','',conditions)
						conditions = re.sub('&lt;/period&gt;','',conditions)
						conditions = re.sub("(?<=rs)\W{2}","'",conditions)
						conditions = re.sub("\W{2}(?=s)","'",conditions)
					except:
						conditions = ''
			else:
				prearchiving = ''
				prerestriction = ''
				postrestriction = ''
				postarchiving = ''
				pdfversion = ''
				conditions = ''


			if eissn != '':
				qstring3 = firstPart2 + eissn + lastPart2
				response = urllib.request.urlopen(qstring3,data=None,timeout=15)
				webContent = response.read()
				# with open('%s.xml' %(jID + '_' + 'SRE'),'w') as f3:
				# 	f3.write(str(webContent))
				# 	f3.close()
				# file = BeautifulSoup(open('%s.xml' %(jID + '_' + 'SRE'), 'r'))
				try:
					f3 = open('%s.xml' %(jID + '_' + 'SRE'),'w')
					f3.write(str(webContent))
					f3.close()
				except UnicodeEncodeError:
					pass
				try:
					eprearchiving = file.publisher.prearchiving.string
				except:
					eprearchiving = ''
				try:
					epostarchiving = file.publisher.postarchiving.string
				except:
					epostarchiving = ''
				try:
					eprerestriction = file.publisher.prerestriction.string
				except:
					eprerestriction = ''
				try:
					epostrestriction = file.publisher.postrestriction.string
					if '<num>' in epostrestriction:
						epostrestriction = re.sub('<.*?>','',postrestriction)
					else:
						epostrestriction = postrestriction.string
				except:
					epostrestriction = ''
				try:
					epdfversion = file.publisher.pdfversion.string
				except:
					epdfversion = ''
				try:
					econditions = file.find_all("condition")
					econditions = str(econditions)
					econditions = re.sub('\[','',econditions)
					econditions = re.sub('\]','',econditions)
					econditions = re.sub('<.*?>','',econditions)
					econditions = re.sub('&lt;num&gt;','',econditions)
					econditions = re.sub('&lt;/num&gt;','',econditions)
					econditions = re.sub('&lt;period units="month"&gt;','',econditions)
					econditions = re.sub('&lt;/period&gt;','',econditions)
					econditions = re.sub("(?<=rs)\W{2}","'",econditions)
					econditions = re.sub("\W{2}(?=s)","'",econditions)
				except:
					econditions = ''

			else:
				eprearchiving = ''
				eprerestriction = ''
				epostrestriction = ''
				epostarchiving = ''
				epdfversion = ''
				econditions = ''
			writer.writerow({'pubID':jID,'issn':issn,'eissn':eissn,'prearchiving':prearchiving,'postarchiving':postarchiving,'prerestriction':prerestriction,'postrestriction':postrestriction,'pdfversion':pdfversion,'conditions':conditions,'eprearchiving':eprearchiving,'epostarchiving':epostarchiving,'eprerestriction':eprerestriction,'epostrestriction':epostrestriction,'epdfversion':epdfversion,'econditions':econditions})
			totalTitles = totalTitles + 1

		##iterates over the failedQueries.csv to query Sherpa Romeo for publication rights and issn; without issns from Journal TOCs, this uses the SherpaRomeo journal title search
		for row in retry_reader:
			jID = row['pubID']
			title = row['title']
			title = title.replace(' ','%20')
			qstring2 = firstPart2 + title + lastPart2
			
			response = urllib.request.urlopen(qstring2)
			webContent = response.read()
			with open('%s.xml' %(jID + '_' + 'SRISSN'), 'w') as f3:
				f3.write(str(webContent))
				f3.close()

			with open('%s.xml' %(jID + '_' + 'SRISSN'),'r') as file:
				file = BeautifulSoup(file,features='lxml')
				resultsCheck = file.numhits.string
				resultsCheck = int(resultsCheck)

				if resultsCheck == 0:
					ultimateFail_writer.writerow({'pubID':jID,'title':title})
					ultimateFail_count = ultimateFail_count + 1
					pass

				elif resultsCheck == 1:
					title = title.replace('%20',' ')
					try:
						issn = file.journal.issn
						issn = string(issn)
					except:
						issn = ''
					try:
						prearchiving = file.publisher.prearchiving.string
					except:
						prearchiving = ''
					try:
						postarchiving = file.publisher.postarchiving.string
					except:
						postarchiving = ''
					try:
						prerestriction = file.publisher.prerestriction.string
					except:
						prerestriction = ''
					try:
						postrestriction = file.publisher.postrestriction.string
						if '<num>' in postrestriction:
							postrestriction = re.sub('<.*?>','',postrestriction)
						else:
							postrestriction = postrestriction.string
					except:
						postrestriction = ''
					try:
						pdfversion = file.publisher.pdfversion.string
					except:
						pdfversion = ''
					try:
						conditions = file.find_all("condition")
						conditions = str(conditions)
						conditions = re.sub('\[','',conditions)
						conditions = re.sub('\]','',conditions)
						conditions = re.sub('<.*?>','',conditions)
						conditions = re.sub('&lt;num&gt;','',conditions)
						conditions = re.sub('&lt;/num&gt;','',conditions)
						conditions = re.sub('&lt;period units="month"&gt;','',conditions)
						conditions = re.sub('&lt;/period&gt;','',conditions)
						conditions = re.sub("(?<=rs)\W{2}","'",conditions)
						conditions = re.sub("\W{2}(?=s)","'",conditions)
					except:
						conditions = ''

			writer.writerow({'pubID':jID,'issn':issn,'prearchiving':prearchiving,'postarchiving':postarchiving,'prerestriction':prerestriction,'postrestriction':postrestriction,'pdfversion':pdfversion,'conditions':conditions,'eprearchiving':eprearchiving,'epostarchiving':epostarchiving,'eprerestriction':eprerestriction,'epostrestriction':epostrestriction,'epdfversion':epdfversion,'econditions':econditions})
			totalTitles = totalTitles + 1
	totalTitles = totalTitles - ultimateFail_count
	disambiguatedTitles.close()
	failedQueries.close()
	journalData.close()
	ultimateFail.close()

	print("")
	print('Part 2: Results')
	print('_____________________')
	print('OA status found for',totalTitles,'publications')
	print('No data for',ultimateFail_count,'publications')

	print("")
	print("Merging csv files...")
	print("")
	
	##MERGING CSVs WITH PANDAS
	##Merging the simplified publications list with the open access status list
	csv1 =pandas.read_csv('publicationsCleanSimple.csv')
	csv2 = pandas.read_csv('sherpaRomeo.csv')

	##Inner merge on pubID key
	merged = csv1.merge(csv2,left_on='pubID',right_on='pubID',how='inner')
	##Index set to false because pandas defaults to producing a 0-X index column
	merged.to_csv('oaStatus.csv',index=False)
	
	print("Faculty publications list with OA status details ready. See oaStatus.csv file.")
	print("")
	print("Cleaning up the project folder.")
	cleanup(path)
def cleanup(path):
	cwd = os.getcwd()
	path2 = '%s/xml_Files' %(cwd)
	##define the access rights
	access_rights = 0o777
	##create folder (path)
	os.mkdir(path2, access_rights)

	path3 = '%s/processData_Files' %(cwd)
	##define the access rights
	access_rights = 0o777
	##create folder (path)
	os.mkdir(path3, access_rights)

	##MOVING PROCESS FILES TO SUBFOLDERS

	##runs through files in the project folder and moves them to folders files based on file type and name

	for (dirname,dirs,files) in os.walk(cwd, topdown=False):
		for file in files:
			if file.endswith('.xml'):
				file = os.path.join(dirname,file)
				shutil.move(file,'%s/xml_Files' %(cwd))
			# elif file in fileNames:
			# 	file = os.path.join(dirname,file)
			# 	shutil.move(file,'%s/processData_Files' %(cwd))
			elif file.endswith('.csv') and file.startswith('oaStatus') == False:
				file = os.path.join(dirname,file)
				shutil.move(file,'%s/processData_Files' %(cwd))

# sherpaRomeo()