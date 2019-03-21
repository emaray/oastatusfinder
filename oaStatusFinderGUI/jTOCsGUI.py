##imports necessary libraries
import re
import unidecode
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
import lxml
import csv
import os



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
print("        0000                            0") 
print("        0   0     0     000   00000   0 0")
print("        0000     0 0    0  0    0       0") 
print("        0       00000   000     0       0")
print("        0      0     0  0  0    0     00000")
print()

    # jtocsUser = input('Enter your JournalTOCs username:')
    # folderName = input('Enter a name for the project folder. (No spaces or special characters):')
    # publicationFile = input("Enter the name of the file containing faculty publications information. Don't include the file extension.")
    # createQuery(jtocsUser,folderName,publicationFile)
##READ AND TRANSFORM TITLES
##opens file containing journal titles; removes special characters, replaces spaces with +, changes newline to carriage return; creates csv file with query strings
def createQuery(jtocsUser,folderName,publicationFile):
    cwd = os.getcwd() 
    path = '%s/%s' %(cwd,folderName)
    ##define the access rights
    access_rights = 0o777
    ##create folder (path)
    os.mkdir(path, access_rights)


    ##reads publication file and stores values in variables
    with open('%s.csv' %(publicationFile), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        editedList = []
    ##creates output csv called processData
        os.chdir(path)
        with open('processData.csv','a',newline ='') as processData:
            fieldnames = ['pubID','journalTitle','editedTitle','queryString']
            processWriter = csv.DictWriter(processData,fieldnames=fieldnames)
            processWriter.writeheader()

            simplePubs = open('publicationsCleanSimple.csv','a',newline='')
            pubFieldnames = ['pubID','firstName','lastName','department','category','activityScope','journalTitle','month','issueNumber','pages','articleTitle','volume','year']
            simpleWriter = csv.DictWriter(simplePubs,fieldnames=pubFieldnames)
            simpleWriter.writeheader()

            for row in reader:
                pubID = (row['publicationID'])
                firstName = (row['firstName'])
                lastName = (row['lastName'])
                department = (row['department'])
                category = (row['category'])
                activityScope = (row['activityScope'])
                journalTitle = (row['journalTitle'])
                month = (row['month'])
                issueNumber = (row['issueNumber'])
                pages = (row['pages'])
                articleTitle = (row['articleTitle'])
                volume = (row['volume'])
                year = (row['year'])
                ##MOVED THIS TO THE PUBLICATION CLEANUP FILE
                ##transformations begin here
                # editedFirstName = unidecode.unidecode(firstName)
                # editedLastName = unidecode.unidecode(lastName)
                # editedTitle = unidecode.unidecode(journalTitle)
                # editedArticleTitle = unidecode.unidecode(articleTitle)
                
                ##writes these titles to a simplified publications list before removing spaces and punctuation to form queries
                simpleWriter.writerow({'pubID':pubID,'firstName':firstName,'lastName':lastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':journalTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':articleTitle,'volume':volume,'year':year})
                
                ##substitutes '' for non-alphanumeric characters in all Titles
                editedTitle = re.sub('[^\s\w]', '', journalTitle)

                ##replaces spaces, ampersands, and dashes with plus signs; replaces commas and colons with nothing; removes double plusses
                editedTitle = editedTitle.replace(' ','+').replace('-','+').replace('++','+').replace('\n','\r')
                editedList.append(editedTitle)

        ##CREATE QUERY STRINGS
                firstPart = 'http://www.journaltocs.ac.uk/api/journals/'
                lastPart = '?encoding=utf-8-sig&user=%s' %(jtocsUser)

                queryString = firstPart+editedTitle+lastPart


                processWriter.writerow({'pubID':pubID,'journalTitle':journalTitle,'editedTitle':editedTitle,'queryString':queryString})
                
    
    totalQueries = len(editedList)
    print("")
    print(totalQueries,"queries formed.")
    print("")
    runQuery1(totalQueries,folderName)

##QUERY JOURNALTOCS API & WRITE RESULTS TO XML
##opens file containing http requests
def runQuery1(totalQueries,folderName):
    print("Querying Journal TOCs Journal API...")
    print("")
    print("Now's a good time to grab a cup of coffee; this will take a bit.")
    sleep(2)
    print("")
    print("Really.")
    print("")
    sleep(1)
    print("                )     (")
    print("               (      )    )")
    print("                )    (    (")
    print("             ______________)__")
    print("            |                 |")
    print("         .--|                 |")
    print("        (  C|\/\/\/\/\/\/\/\/\|")
    print("         '--|\/\/\/\/\/\/\/\/\|")
    print("            |                 |")
    print("            '_________________'")
    print("             '---------------'")
    print("")
    with open('processData.csv','r') as processData:
        queryReader = csv.DictReader(processData,delimiter=',')
        fieldnames = ['pubID','journalTitle','editedTitle','queryString']

        errorCount = 0

        ##for each line in the file, sends request, saves response to xml file  
        for row in queryReader:
            qstring = row['queryString']
            pubID = row['pubID']
            journalTitle = row['journalTitle']

            try:
                response = urllib.request.urlopen(qstring,data=None,timeout=15)
                webContent = response.read()
                with open('%s.xml' %(pubID),'w',encoding='UTF-8') as f2:
                    f2.write(str(webContent))     

            except IOError:
                with open('queryErrors.csv', mode='a', newline='',encoding='UTF-8') as queryErrors: 
                    queryErrors_writer = csv.writer(queryErrors, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    queryErrors_writer.writerow([pubID, journalTitle, qstring])
                    errorCount = errorCount + 1                 
                pass
            except ValueError:
                pass             
            sleep(.0625)
        
    ##allows script to skip requests that time out instead of failing; prints url and the error message to screen
            # except IOError:
            #     if qstring != 'queryString':
            #         with open('queryErrors.csv', mode='a', newline='',encoding='UTF-8') as queryErrors: 
            #                         queryErrors_writer = csv.writer(queryErrors, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #                         queryErrors_writer.writerow([pubID, qstring])
            #     else:
            #         continue
            #     pass
        ##delays iterations to keep host from cutting me off!
        


    ##RETRY QUERY STRINGS THAT ERRORED OUT
    try:
        errorFile = csv.reader(open('queryErrors.csv', 'r'), delimiter = ',')
        for row in errorFile:
            try:
                response = urllib.request.urlopen(row[2],data=None,timeout=15)
                webContent = response.read()
                f2 = open('%s.xml' %(row[0]),'w',encoding='utf-8')
                f2.write(str(webContent))

            except IndexError:
                pass
            except IOError:
                with open('queryErrors_2.csv', mode='a', newline='',encoding='utf-8') as queryErrors2: 
                    queryErrors2_writer = csv.writer(queryErrors2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    queryErrors2_writer.writerow([row[0],row[1],row[2]])
                    queryErrors2.close()
                pass
            ##delays iterations to keep host from cutting me off!
            sleep(.0625)
    except FileNotFoundError:
        pass
    print("Of the",totalQueries,"queries,",errorCount,"timed out.")
    parseXML(folderName)
##PARSE XML & WRITE RELEVANT DATA TO CSV
##opens each xml file; finds all titles, issns, and eissns in the file; writes values to a csv file
##directory = os.getcwd()
def parseXML(folderName):    
    print("")
    print("Parsing XML")
    print("")

    path = os.getcwd()
    ##counts the number of files in the directory; imperfect solution because it counts non-xml files, but only 2-3
    fileCount = sum(1 for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f[0] != '.')

    fileNum = 0
    successfulQuery_count = 0
    failedQuery_count = 0
    ambiguousTitle_count = 0
    ambiTitles = open('ambiguousTitles.csv',mode = 'a',newline='',encoding='utf-8')
    fieldnames = ['pubID','title','issn','eissn']
    ambiWriter = csv.DictWriter(ambiTitles, fieldnames=fieldnames,delimiter=',')
    fieldnames2 = ['pubID','title']
    failedQueries = open('failedQueries.csv',mode = 'a',newline='',encoding='utf-8')
    failedQueryWriter = csv.DictWriter(failedQueries,fieldnames=fieldnames2,delimiter=',')
    failedQueryWriter.writeheader()

    ambiWriter.writeheader()

    with open('journalData.csv', mode='a', newline='',encoding='utf-8') as journalData:
        fieldnames = ['pubID','title','issn','printRights','eissn','eRights']
        writer = csv.DictWriter(journalData, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writeheader()

        while fileNum in range(0,fileCount):
            for file in path:
                fileNum = fileNum + 1
                #try-except block necessary because some file numbers are missing
                try:
                    file = BeautifulSoup((open('%s.xml' %(fileNum),'r')),features="lxml")
                    titles = file.find_all('title')
                    issns = file.find_all('prism:issn')
                    eissns = file.find_all('prism:eissn')

                    #try-except blocks necessary because not all titles have issns or eissns
                    titleLen = len(titles)
                    if titleLen == 2:
                        for i in range (1,titleLen):                  
                            title = str(titles[i])
                            title = re.sub('<.*?>','',title)
                            ##If the title in the xml file is "JournalTOCS API journals", this means the query produced 0 results; write data to failedQueries file for manual inspection.
                            if title == 'JournalTOCs API journals':
                                newTitle = file.item
                                newTitle = str(newTitle)
                                newTitle = re.sub('(.[A-z]{4}\s{1}[A-z]{3}.[A-z]{5}.{2}[A-z]{4}.{3}[A-z]{3}.[A-z]{11}.[A-z]{2}.[A-z]{2}.[A-z]{3}.[A-z]{8}.{1})','',newTitle)
                                newTitle = re.sub('(.{3}[a-z]{1}.{1}[a-z]\s{4}.+)','',newTitle)

                                with open('failedQueries.csv','a',newline='') as failedQueries:
                                    failedQueryWriter = csv.DictWriter(failedQueries,fieldnames=fieldnames,delimiter=',')
                                    failedQueryWriter.writerow({'pubID':fileNum,'title':newTitle})
                                    failedQuery_count = failedQuery_count + 1
                                # print('Ambi!')
                            ##If only 2 titles were found in the xml document AND the second title is not "Journal TOCS API journals," the query worked!; write data to journalData csv.
                            else:
                                try:
                                    issn = str(issns[i-1])
                                    issn = re.sub('<.*?>','',issn)
                                except IndexError:
                                    issn = ''
                                try:
                                    eissn = str(eissns[i-1])
                                    eissn = re.sub('<.*?>','',eissn)
                                except IndexError:
                                    eissn = ''

                                writer.writerow({'pubID':fileNum, 'title':title, 'issn':issn,'eissn':eissn})
                                successfulQuery_count = successfulQuery_count + 1
                    ##If the list of titles pulled from the xml file contains more than 3 titles, records data in the ambiguous titles file for manual inspection.
                    elif titleLen >= 3:
                        title = str(titles[0])
                        title = re.sub('<.*?>','',title)
                        title = re.sub('([A-z]{11}\s[A-Z]{3}\s.\s[A-z]{5}\s(\d{4}|\d{3}|\d{2}|\d{1})\s[a-z]{7}.\w.\s[a-z]{3}.\s)','', title)
                        with open('ambiguousTitles.csv',mode = 'a',newline='',encoding='utf-8') as ambiTitles:
                            fieldnames = ['pubID','title','issn','eissn']
                            ambiWriter = csv.DictWriter(ambiTitles, fieldnames=fieldnames,delimiter=',')
                            ambiWriter.writerow({'pubID':fileNum, 'title':title})
                            ambiguousTitle_count = ambiguousTitle_count + 1
                except:
                    break
    ##re-tries any queries that errored out. Records second failures in failedQueries document
    try:
    	with open('queryErrors_2.csv',newline='') as queryErrors:
    		errorReader = csv.reader(queryErrors, delimiter=',')
    		for row in errorReader:
    			failRow = [row[0],row[1]]
    			with open('failedQueries.csv','a',newline='') as failedQueries:
    				failWriter = csv.writer(failedQueries,delimiter=',')
    				failWriter.writerow(failRow)
    				failedQuery_count = failedQuery_count + 1
    except:
    	pass
    print("")
    print("Part 1: Results")
    print("________________")
    print("")
    print("   Successful queries:",successfulQuery_count)
    print("   Failed queries:",failedQuery_count)
    print("   Ambiguous results:",ambiguousTitle_count)
    print("")
    print("Next step: Manually search for ISSNs and/or eISSNs for titles in ambiguousTitles.csv. See workflow for details." )

##Commented this out for the GUI test; will not run without a call.
# createQuery()
