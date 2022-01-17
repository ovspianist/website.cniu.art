import os

def getArtworkNames():
	filestr = ""
	files = os.listdir("D:/Website.cniu.art/img/artwork/paintings/")
	for file in files:
		filestr += f"\"{file}\","
		
	print(filestr)

getArtworkNames()
