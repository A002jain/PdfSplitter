from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import random
import os

class PdfFile:

	def __init__(self,inputFileName,outputFileName,startPage,lastPage):
		self.inputFileName = inputFileName
		self.outputFileName = outputFileName
		self.startPage = startPage
		self.lastPage = lastPage
		self.totalPage = 0

	def logData(self):
		print("Source FileName:"+self.inputFileName)
		print("TotalPage:"+str(self.totalPage))
		print("Output FileName:"+self.outputFileName)
		print("StartPage FileName:"+str(self.startPage))
		print("LastPage FileName:"+str(self.lastPage))


	def split(self,startPage,lastPage):
		pdf_file = PdfFileReader(self.inputFileName)
		pdfWriter = PdfFileWriter()
		for i in range(startPage-1,lastPage):
			print(i)
			pdfWriter.addPage(pdf_File.getPage(i))
		outputPdf = open(self.outputFileName,mode ='wb')
		pdfWriter.write(outputPdf)
		outputPdf.close()


class PdfSplitCLi:
	
	def __init__(self,pdfObj):
		self.pdfObj = pdfObj
		self.flaf : int

	def split(self):
		pdf_file = PdfFileReader(self.pdfObj.inputFileName)
		pdfWriter = PdfFileWriter()
		startPage = self.pdfObj.startPage -1
		lastPage = self.pdfObj.lastPage
		for i in range(startPage,lastPage):
			pdfWriter.addPage(pdf_file.getPage(i))
		outputPdf = open(self.pdfObj.outputFileName,mode ='wb')
		pdfWriter.write(outputPdf)
		outputPdf.close()
		


class CLIWrapper:

	def argsInput(self,options):
		optionsSize = len(options)
		outputFileName = ""
		if optionsSize == 1 and options[0] =="-help" :
			self.helpUser()
		elif optionsSize%2 == 0:
			
			if optionsSize == 4:
				if options[2] == "-des":
					outputFileName = self.setOutputFilePath(options[3])  # path of src pdf file 
				else:
					self.helpUser()
					
			if options[0] == "-src":
				 # setting input file path
				inputFileName,basePath = self.setInputFilePath(options[1])

				if outputFileName !="" and basePath !="" and options[3].find("/") !=0:
					outputFileName = basePath+"/"+options[3]
				if basePath =="":
					basePath =os.getcwd()
				if outputFileName =="":
					outputFileName = basePath+"/pdfSplited"+str(random.randint(1,1000))+".pdf"
				self.callSplitter(inputFileName,outputFileName)
			else:
				self.helpUser()
		else:
			self.helpUser()

	def getBasepath(self,filepath):
		a = filepath.split("/")
		a = a[1:-1]
		basePath =""
		for i in a:
			basePath=basePath+"/"+i
		return basePath

	def setInputFilePath(self,filepath):
		if filepath.find("/") == 0:
			return filepath,self.getBasepath(filepath)
		else:
			return os.getcwd()+"/"+filepath,""

	def setOutputFilePath(self,filepath):
		if filepath.find("/") == 0:
			return filepath
		else:
			return os.getcwd()+"/"+filepath

	def helpUser(self):
		print("*"*20+"Pdf Splitter"+"*"*20)
		print("usage -->  pdfSplitter -src  <PDF Name>  -des <output Pdf Name>")
		print("-src  Mandatory")
		print("-des  Optional")
		print("-help check basic usage")	

	def manualInput(self):
		inputFileName = input("Enter Pdf Path:")
		outputFileName = os.getcwd()+"/"+input("Enter Output File Name:")
		self.callSplitter(inputFileName,outputFileName)
	
	def callSplitter(self,inputFileName,outputFileName):
		startPage = int(input("Start Page No.:"))
		lastPage = int(input("Last Page No.:"))
		pdf_File = PdfFile(inputFileName,outputFileName,startPage,lastPage)
		pdfSplitter = PdfSplitCLi(pdf_File)
		pdfSplitter.split()		
		print("PDF splited from page No. " +str(startPage)+"-"+str(lastPage)+"\nOutput FilePath: "+outputFileName)	

def main():
	print(os.getcwd())
	cli = CLIWrapper()
	if len(sys.argv) > 1:
		cli.argsInput(sys.argv[1:])
	else:
		cli.manualInput()

if __name__ == '__main__':
	main()
