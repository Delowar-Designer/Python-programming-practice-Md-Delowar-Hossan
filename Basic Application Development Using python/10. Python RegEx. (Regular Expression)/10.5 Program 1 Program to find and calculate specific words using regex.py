# Program to find and calculate specific words using regex
import re
txt = """The rain in Spain The rain in Spain
The rain in Spain The rain in Spain
The rain in Spain The rain in Spain"""
x = re.findall("ai",txt)
print("countiing word:\n",txt)
print(x.count("ai"),"ai Found")
