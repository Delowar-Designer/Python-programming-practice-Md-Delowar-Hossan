import pyttsx3
from pypdf import PdfReader

book = open('oop.pdf', 'rb')
pdfReader = PdfReader(book)
pages = len(pdfReader.pages)

speaker = pyttsx3.init()
for num in range(pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
