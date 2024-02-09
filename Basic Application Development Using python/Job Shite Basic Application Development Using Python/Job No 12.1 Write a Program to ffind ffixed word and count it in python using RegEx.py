# Write a Program to ffind ffixed word and count it in python using RegEx
import re
dpi = "CST is a dream department. modern world leads CST"
x = re.findall("cst",dpi)
print(dpi)
print(x.count("CST"),"times found cst")

