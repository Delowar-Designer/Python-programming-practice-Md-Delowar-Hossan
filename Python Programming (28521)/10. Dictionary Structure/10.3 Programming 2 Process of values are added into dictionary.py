# Process of values are added into dictionary
CountryCodeDict = {"India":91,"UK":44,"USA":1,"Spain":34}
print("Primary Dictionary is: ")
print(CountryCodeDict)
# Adding single key value pairs
CountryCodeDict.update({'Germany':49})
print("Adding Germany:")
print(CountryCodeDict)

# Adding multiple key value pairs
CountryCodeDict.update([('Austria',43),('Delowar',7)])
print("Adding Austria and Russia: ")
print(CountryCodeDict)
