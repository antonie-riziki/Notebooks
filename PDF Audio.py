import pyttsx3
import PyPDF2
from tkinter.filedialog import *


############ MAKE PDF READER WITH AUDIO ##############
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for i in range (0, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speech = pyttsx3.init()
    speech.say(text)
    speech.runAndWait()
    
