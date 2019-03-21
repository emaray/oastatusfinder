import re
import unidecode
import csv
import os
import pandas
import shutil

def listFormatter(publicationsList):
	with open('%s.csv' %(publicationsList),'r',newline='') as pubList:
		reader = csv.DictReader(pubList)
		with open('publicationsCleaned.csv','a',newline='') as pubCleaned:
			publicationID = 0
			fieldnames = ['publicationID','firstName','lastName','department','category','activityScope','journalTitle','month','issueNumber','pages','articleTitle','volume','year']
			cleanWriter = csv.DictWriter(pubCleaned,fieldnames=fieldnames,delimiter=",")
			cleanWriter.writeheader()
			for row in reader:
				firstName = (row['Name-First'])
				lastName = (row['Name-Last'])
				department = (row['Department'])
				category = (row['Category'])
				activityScope = (row['Activity/Scope'])
				journalTitle = (row['Journal / Conference Name'])
				month = (row['Month'])
				issueNumber = (row['Number'])
				pages = (row['Pages'])
				articleTitle = (row['Title'])
				volume = (row['Volume'])
				year = (row['Year-Published (Cal)'])
				#transformations begin here
				editedFirstName = unidecode.unidecode(firstName)
				editedLastName = unidecode.unidecode(lastName)
				editedTitle = unidecode.unidecode(journalTitle)
				editedArticleTitle = unidecode.unidecode(articleTitle)

				##writes these titles to a simplified publications list before removing spaces and punctuation to form queries
				if "Article" in category:
					if "Journal: Academic" in activityScope:
						publicationID = publicationID + 1
						cleanWriter.writerow({'publicationID':publicationID,'firstName':editedFirstName,'lastName':editedLastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':editedTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':editedArticleTitle,'volume':volume,'year':year})
						
					elif "Creative Writing" in activityScope:
						publicationID = publicationID + 1
						cleanWriter.writerow({'publicationID':publicationID,'firstName':editedFirstName,'lastName':editedLastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':editedTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':editedArticleTitle,'volume':volume,'year':year})
					
					else:
						pass
				else:
					pass	


# with open('sedona.csv','r',newline='') as pubList:
# 	reader = csv.DictReader(pubList)
# 	with open('publicationsCleaned.csv','a',newline='') as pubCleaned:
# 		publicationID = 0
# 		fieldnames = ['publicationID','firstName','lastName','department','category','activityScope','journalTitle','month','issueNumber','pages','articleTitle','volume','year']
# 		cleanWriter = csv.DictWriter(pubCleaned,fieldnames=fieldnames,delimiter=",")
# 		cleanWriter.writeheader()
# 		for row in reader:
# 			firstName = (row['Name-First'])
# 			lastName = (row['Name-Last'])
# 			department = (row['Department'])
# 			category = (row['Category'])
# 			activityScope = (row['Activity/Scope'])
# 			journalTitle = (row['Journal / Conference Name'])
# 			month = (row['Month'])
# 			issueNumber = (row['Number'])
# 			pages = (row['Pages'])
# 			articleTitle = (row['Title'])
# 			volume = (row['Volume'])
# 			year = (row['Year-Published (Cal)'])
# 			#transformations begin here
# 			editedFirstName = unidecode.unidecode(firstName)
# 			editedLastName = unidecode.unidecode(lastName)
# 			editedTitle = unidecode.unidecode(journalTitle)
# 			editedArticleTitle = unidecode.unidecode(articleTitle)

# 			##writes these titles to a simplified publications list before removing spaces and punctuation to form queries
# 			if "Article" in category:
# 				if "Journal: Academic" in activityScope:
# 					publicationID = publicationID + 1
# 					cleanWriter.writerow({'publicationID':publicationID,'firstName':firstName,'lastName':lastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':journalTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':articleTitle,'volume':volume,'year':year})
					
# 				elif "Creative Writing" in activityScope:
# 					publicationID = publicationID + 1
# 					cleanWriter.writerow({'publicationID':publicationID,'firstName':firstName,'lastName':lastName,'department':department,'category':category,'activityScope':activityScope,'journalTitle':journalTitle,'month':month,'issueNumber':issueNumber,'pages':pages,'articleTitle':articleTitle,'volume':volume,'year':year})
				
# 				else:
# 					pass
# 			else:
# 				pass	