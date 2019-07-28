# Searchable-PDFs
This repository contains code to create searchable pdf from scanned pdfs or images. For multi pages pdf, pdfs for individual pages are stored which can be merged as per need. For good quality images/scanned pdfs, accuracy is close to 98%.

# Tesseract as OCR engine
I have used Tesseract by Google to perform OCR as it is open sourced and frequently maintained library. For python implementation, there is library called "pytesseract".

For installation steps,[click there]( https://github.com/madmaze/pytesseract)

Apart from pytesseract, other important libraries used are,
* PIL
* matplotlib
* wand
* pyPDF2

# Improvements
* Merging pdfs can be included
* Support for poor quality images and auto cropping pages similar to Camscanner can be implemented
* Entire project can be put on server 
