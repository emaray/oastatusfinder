from tkinter import *
from tkinter import messagebox
import threading

window = Tk() 
 
window.title("OA Status Finder")
window.configure(background='white')
window.geometry('600x450')

main = Label(window, text='Welcome to OA Status Finder!',font = "Verdana 16 bold", bg="white",padx=112)
main.grid(column=0,row=0,columnspan=3)

mainLabel = Label(window, text='',font="Verdana 12 italic", bg="white")
mainLabel.grid(column=0,row=1)

logo = PhotoImage(file='oaLogo.gif')
logoDisplay = Label(window,image=logo,bg='white')
logoDisplay.grid(column=0,row=2,columnspan=3)

lfLabel = Label(window, text='Pre-processing: Regularizing the publications list',font = "Verdana 12 italic", bg="white")
part1Label = Label(window, text='Part 1: Querying Journal TOCs',font = "Verdana 12 italic", bg="white")
part2Label = Label(window, text='Part 2: Querying SherpaRomeo ',font = "Verdana 12 italic", bg="white")
part3Label = Label(window, text='Part 3: Creating lists for consulting librarians',font = "Verdana 12 italic", bg="white")


lflbl1 = Label(window, text="Enter the name of the faculty publications file.\n (Don't include the file extension.)")
lftxt1 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat")

jTOCslbl1 = Label(window, text="Enter your JournalTOCs username: \n", bg="white")
jTOCstxt1 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat") 

jTOCslbl2 = Label(window, text='Enter a name for the project folder. \n (No spaces or special characters):', bg="white")
jTOCstxt2 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat")

jTOCslbl3 = Label(window, text="Enter the name of the faculty publications file.\n (Don't include the file extension.)", bg="white")
jTOCstxt3 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat")

jTOCSlbl4 = Label(window, text="Next step: Manually search for ISSNs and/or eISSNs for titles in ambiguousTitles.csv. \n\n See workflow for details.", bg="white")

srlbl1 = Label(window, text="Enter the name of the project folder \n",bg='white')
srtxt1 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat") 

srlbl2 = Label(window, text='Enter your SherpaRomeo access key',bg='white')
srtxt2 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat")

allbl1 = Label(window, text='Enter the name of the project folder: \n',bg='white')
altxt1 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat")

allbl2 = Label(window, text='Do you have a list consulting areas by librarian? \n Answer "yes" or "no"',bg='white')
altxt2 = Entry(window,width=50,highlightcolor="orange",highlightthickness=1,relief="flat")

def cleanPubList(event=None):
	import listFormatter as lf 	
	lfButton.grid_remove()
	lfText.grid_remove()
	part1Button.grid_remove()
	part2Button.grid_remove()
	part3Button.grid_remove()
	part1Text.grid_remove()
	part2Text.grid_remove()
	part3Text.grid_remove()
	closeButton.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()

	backButtonLF.bind("<Return>",goBackLF)
	backButtonLF.grid(column=0, row=12, sticky=W, padx=20)

	lfLabel.grid(column=0,row=1,columnspan=3)
	logoPadding.grid(column=0, row=3)
	lflbl1.grid(column=0,row=4,sticky=E)
	lftxt1.grid(column=1,row=4,sticky=W)

	submitButtonLF.grid(column=0, row=10,columnspan=3)
	submitButtonLF.bind("<Return>", getInputsLF)


def part1(event=None):
	import jTOCsGUI as jTOCs
	lfButton.grid_remove()
	lfText.grid_remove()
	part1Button.grid_remove()
	part2Button.grid_remove()
	part3Button.grid_remove()
	part1Text.grid_remove()
	part2Text.grid_remove()
	part3Text.grid_remove()
	closeButton.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()

	part1Label.grid(column=0,row=1,columnspan=3)
	logoPadding.grid(column=0, row=3)
	jTOCslbl1.grid(column=0, row=4,sticky=E)
	jTOCstxt1.grid(column=1, row=4,sticky=W)
	jTOCslbl2.grid(column=0, row=6,sticky=E)
	jTOCstxt2.grid(column=1, row=6,sticky=W)
	jTOCslbl3.grid(column=0, row=8,sticky=E)
	jTOCstxt3.grid(column=1, row=8,sticky=W)
	blank1.grid(column=0,row=9)

	submitButton.grid(column=0, row=10,columnspan=3)
	submitButton.bind("<Return>", getInputs)

	blank2.grid(column=0,row=11)
	
	backButton.bind("<Return>",goBack)
	backButton.grid(column=0, row=12, sticky=W, padx=20)


def part2(event=None):
	import sherpaRomeoGUI as sr
	lfButton.grid_remove()
	lfText.grid_remove()
	part1Button.grid_remove()
	part2Button.grid_remove()
	part3Button.grid_remove()
	part1Text.grid_remove()
	part2Text.grid_remove()
	part3Text.grid_remove()
	closeButton.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()

	part2Label.grid(column=0,row=1,columnspan=3)
	logoPadding.grid(column=0, row=3)
	srlbl1.grid(column=0, row=4)
	srtxt1.grid(column=1, row=4)
	srlbl2.grid(column=0, row=6)
	srtxt2.grid(column=1, row=6)
	blank2.grid(column=0,row=7)


	submitButton2.grid(column=0, row=8,columnspan=3)
	submitButton2.bind("<Return>",getInputs2)

	blank3.grid(column=0,row=9)

	backButton2.bind("<Return>",goBack2)
	backButton2.grid(column=0, row=11, sticky=W, padx=20)


def part3(event=None):
	print("")
	import assignLibrarianGUI as al
	lfButton.grid_remove()
	lfText.grid_remove()
	part1Button.grid_remove()
	part2Button.grid_remove()
	part3Button.grid_remove()
	part1Text.grid_remove()
	part2Text.grid_remove()
	part3Text.grid_remove()
	closeButton.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()

	part3Label.grid(column=0,row=1,columnspan=3)
	logoPadding.grid(column=0, row=3)
	allbl1.grid(column=0, row=4,sticky=E)
	altxt1.grid(column=1, row=4,sticky=W)
	allbl2.grid(column=0, row=6,sticky=E)
	altxt2.grid(column=1, row=6,sticky=W)
	blank2.grid(column=0,row=7)

	submitButton3.grid(column=0, row=8,columnspan=3)
	submitButton3.bind("<Return>",getInputs3)

	blank3.grid(column=0,row=9)

	backButton3.bind("<Return>",goBack3)
	backButton3.grid(column=0, row=11, sticky=W, padx=20)

def returnMenuLF():
	lfLabel.grid_remove()
	lflbl1.grid_remove()
	lftxt1.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()
	returnButtonLF.grid_remove()
	backButtonLF.grid_remove()
	submitButtonLF.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

def returnMenu():
	part1Label.grid_remove()
	jTOCslbl1.grid_remove()
	jTOCslbl2.grid_remove()
	jTOCslbl3.grid_remove()
	jTOCstxt1.grid_remove()
	jTOCstxt2.grid_remove()
	jTOCstxt3.grid_remove()
	jTOCSlbl4.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()
	returnButton.grid_remove()
	backButton.grid_remove()
	submitButton.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

def returnMenu2():
	part2Label.grid_remove()
	srlbl1.grid_remove()
	srlbl2.grid_remove()
	srtxt1.grid_remove()
	srtxt2.grid_remove()
	returnButton2.grid_remove()
	backButton2.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

def returnMenu3():
	part3Label.grid_remove()
	allbl1.grid_remove()
	allbl2.grid_remove()
	altxt1.grid_remove()
	altxt2.grid_remove()
	returnButton3.grid_remove()
	backButton3.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

returnButtonLF = Button(window, text="Return to menu", command=returnMenuLF)
returnButtonLF.bind("<Return>",returnMenuLF)
returnButton = Button(window, text="Return to menu", command=returnMenu)
returnButton.bind("<Return>",returnMenu)
returnButton2 = Button(window, text="Return to menu", command=returnMenu2)
returnButton2.bind("<Return>",returnMenu2)
returnButton3 = Button(window, text="Return to menu", command=returnMenu3)
returnButton3.bind("<Return>",returnMenu3)

blank1 = Label(window,text='',bg='white')
blank1.grid(column=0,row=4)

##LF things
lfText = Label(window,text="Pre-processing: Regularize the publications file",bg="white")
lfText.grid(column=0, row=5,stick=E)

lfButton = Button(window, text="Start", command=cleanPubList)
lfButton.grid(column=1, row=5,sticky=W)
lfButton.bind("<Return>",cleanPubList)

def getInputsLF():
	import listFormatter as lf
	def listFormatterThread():
		publicationsList = lftxt1.get()
		lf.listFormatter(publicationsList)
		submitButtonLF.grid_remove()
		# returnButton = Button(window, text="Return to menu", command=returnMenu)
		returnButtonLF.grid(column=0, row=10,columnspan=3)
	t = threading.Thread(target=listFormatterThread)
	t.start()	



submitButtonLF = Button(window, text="Submit", command=getInputsLF)

def goBackLF():
	lfLabel.grid_remove()
	lflbl1.grid_remove()
	lftxt1.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	blank3.grid_remove()
	returnButtonLF.grid_remove()
	backButtonLF.grid_remove()
	submitButtonLF.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

backButtonLF = Button(window, text="Back", command=goBackLF)


##Part 1 things
part1Text = Label(window,text="Part 1: Find ISSNs for the journals in the list of publications",bg="white")
part1Text.grid(column=0, row=6,sticky=E)

part1Button = Button(window, text="Start", command=part1)
part1Button.grid(column=1, row=6,sticky=W)
part1Button.bind("<Return>",part1)

def getInputs(event=None):
	def getInputsThread():
		import jTOCsGUI as jTOCs
		jtocsUser = jTOCstxt1.get()
		folderName = jTOCstxt2.get()
		publicationFile = jTOCstxt3.get()
		jTOCs.createQuery(jtocsUser,folderName,publicationFile)
		part1Label.grid_remove()
		jTOCslbl1.grid_remove()
		jTOCslbl2.grid_remove()
		jTOCslbl3.grid_remove()
		jTOCstxt1.grid_remove()
		jTOCstxt2.grid_remove()
		jTOCstxt3.grid_remove()
		blank1.grid_remove()
		# blank2.grid_remove()
		# blank3.grid_remove()

		jTOCSlbl4.grid(column=0, row=5,columnspan=3)
		submitButton.grid_remove()
		returnButton.grid(column=0, row=10,columnspan=3)

	t = threading.Thread(target=getInputsThread)
	t.start()	


submitButton = Button(window, text="Submit", command=getInputs)

def goBack():
	part1Label.grid_remove()
	jTOCslbl1.grid_remove()
	jTOCslbl2.grid_remove()
	jTOCslbl3.grid_remove()
	jTOCstxt1.grid_remove()
	jTOCstxt2.grid_remove()
	jTOCstxt3.grid_remove()
	returnButton.grid_remove()
	backButton.grid_remove()
	submitButton.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

backButton = Button(window, text="Back", command=goBack)


##Part 2 things
part2Text = Label(window,text="Part 2: Find OA status for publications by querying SherpaRomeo",bg="white")
part2Text.grid(column=0, row=7,sticky=E)

part2Button = Button(window, text="Start", command = part2)
part2Button.grid(column=1, row = 7, sticky=W)
part2Button.bind("<Return>",part2)

def getInputs2(event=None):
	import sherpaRomeoGUI as sr
	def getInputs2Thread():
		folderName = srtxt1.get()
		sherpaRomeoAK = srtxt2.get()
		sr.sherpaRomeo(folderName, sherpaRomeoAK)

		submitButton2.grid_remove()
		returnButton2.grid(column=0, row=8,columnspan=3)
	t = threading.Thread(target=getInputs2Thread)
	t.start()



submitButton2 = Button(window, text="Submit", command=getInputs2)

def goBack2():
	part2Label.grid_remove()
	srlbl1.grid_remove()
	srlbl2.grid_remove()
	srtxt1.grid_remove()
	srtxt2.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	returnButton2.grid_remove()
	backButton2.grid_remove()
	submitButton2.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

backButton2 = Button(window, text="Back", command=goBack2)

##Part 3 things
part3Text = Label(window,text="Part 3: Assign publications to liaison librarians by department",bg="white")
part3Text.grid(column=0, row=8,sticky=E)

part3Button = Button(window, text="Start", command= part3)
part3Button.grid(column=1, row=8,sticky=W)
part3Button.bind("<Return>",part3)

blank2 = Label(window,text='',bg='white')
blank2.grid(column=0,row=9)

closeButton = Button(window, text="Close", command=window.destroy)
closeButton.grid(column=0, row=10,columnspan=3)
closeButton.bind("<Return>",window.destroy)

blank3 = Label(window,text='',bg='white')
blank3.grid(column=0, row=11)

def getInputs3(event=None):
	import assignLibrarianGUI as al
	def getInputs3Threaded():
		folderName = altxt1.get()
		haveList = altxt2.get()
		al.consultingAreasList(folderName, haveList,window)

		submitButton3.grid_remove()
		returnButton3.grid(column=0, row=8,columnspan=3)
	
	t = threading.Thread(target=getInputs3Thread)
	t.start()



submitButton3 = Button(window, text="Submit", command=getInputs3)

def goBack3():
	part3Label.grid_remove()
	allbl1.grid_remove()
	allbl2.grid_remove()
	altxt1.grid_remove()
	altxt2.grid_remove()
	blank1.grid_remove()
	blank2.grid_remove()
	returnButton3.grid_remove()
	backButton3.grid_remove()
	submitButton3.grid_remove()

	blank1.grid(column=0,row=4)
	lfText.grid(column=0, row=5,sticky=E)
	lfButton.grid(column=1, row=5,sticky=W)
	part1Button.grid(column=1, row=6,sticky=W)
	part2Button.grid(column=1, row = 7,sticky=W)
	part3Button.grid(column=1, row=8,sticky=W)
	part1Text.grid(column=0,row=6,sticky=E)
	part2Text.grid(column=0,row=7,sticky=E)
	part3Text.grid(column=0,row=8,sticky=E)
	blank2.grid(column=0,row=9)
	closeButton.grid(column=0, row=10)

backButton3 = Button(window, text="Back", command=goBack3)

logoPadding = Label(window,text='',bg='white')

 
window.mainloop()