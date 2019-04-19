from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import ( PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError)
import glob, os
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter

PATH="/home/bansi/Accobots/Using tesseract onl/"
OPT_PATH="images/"
	
def convert_pdf_to_images(filename):
	
	basename=filename.split(".")[0]
	image = convert_from_path(PATH+filename)
	ct=0
	for im in image:
		im.save(OPT_PATH+basename+str(ct)+".jpg", quality=100)
		ct=ct+1
		#image[0].save(str(i)+".jpg")
	print("done converting pdf to images")

def merge_pdfs(OPT_PATH):

	filelist= [file for file in os.listdir(OPT_PATH) if file.endswith('.pdf')]
	output = PdfFileWriter()
	#print(filelist)
	for file in filelist:
		pdfOne = PdfFileReader(open(OPT_PATH+file, "rb"))
		output.addPage(pdfOne.getPage(0))
		
	outputStream = open(r"output.pdf", "wb")
	output.write(outputStream)
	outputStream.close()
