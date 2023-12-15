# Convart Text to Handwritteng pythone
#import pywhatkit as pw

#text = """A paragraph develops ONE main idea through a series of related sentences. 
#This main idea is usually introduced in the first sentence of the paragraph, 
#called the topic sentence. The idea is then developed further through the sentences that follow."""

#pw.text_to_handwriting(text, 'demo1.png', [0, 0, 1, 138])
#print("END")

import pywhatkit as pw

text = """A paragraph develops ONE main idea through a series of related sentences. 
This main idea is usually introduced in the first sentence of the paragraph"""

# Convert text to handwriting
pw.text_to_handwriting(text, '1111.png', rgb=[0, 0, 0, 255])
print("END")
