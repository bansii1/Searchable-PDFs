from PIL import Image
import argparse
import os
import pytesseract
import matplotlib.pyplot as plt
from PIL import ImageEnhance, ImageFilter
from convertPDFtojpg import convert_pdf_to_images, merge_pdfs
import sys
from wand.image import Image as WImage

PATH="/home/bansi/Accobots/Using tesseract onl/"
OPT_PATH="images/"

def get_from_pdf(pdf_name):
	
	convert_pdf_to_images(pdf_name)
	
	filelist= [file for file in os.listdir(OPT_PATH) if file.endswith('.jpg')]
	print(filelist)
	
	ct = 0
	for file in filelist:

		pdfopt = pytesseract.image_to_pdf_or_hocr(OPT_PATH+file, extension='pdf')
		file1 = open('temp.txt', 'wb')
		file1.write(pdfopt)
		file1.close()

		file2 = open(OPT_PATH+'optfile'+pdf_name.split(".")[0]+".pdf", 'a+b')
		for line in open('temp.txt', 'rb').readlines():
			file2.write(line)
		print("writing to "+OPT_PATH+'optfile'+pdf_name.split(".")[0]+str(ct)+".pdf")
		ct =ct+1
		
	#merge pdf has errors in it... NEEDS MODIFICATION
	#merge_pdfs(OPT_PATH)

def get_from_image(image_name):
	
	pdfopt = pytesseract.image_to_pdf_or_hocr(OPT_PATH+image_name, extension='pdf')
	file1 = open('temp.txt', 'wb')
	file1.write(pdfopt)
	file1.close()

	file2 = open(OPT_PATH+'optfile'+image_name.split(".")[0]+".pdf", 'a+b')
	for line in open('temp.txt', 'rb').readlines():
		file2.write(line)
	
	print("writing to "+OPT_PATH+'optfile'+image_name.split(".")[0]+".pdf")

if __name__=="__main__":	
	ap=argparse.ArgumentParser()
	ap.add_argument("-f","--filename", help="Path to input file-pdf/image ")
	args=vars(ap.parse_args())
	filename=args["filename"]

	if filename.split(".")[-1]=="pdf":
		get_from_pdf(filename)
	elif filename.split(".")[-1]=="jpg" or filename.split(".")[-1]=="jpeg" or filename.split(".")[-1]=="png":
		get_from_image(filename)
	else:
		print()
	print("Done")
																																																																																																																																																												
