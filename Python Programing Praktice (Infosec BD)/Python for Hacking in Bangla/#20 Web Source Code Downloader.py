#20 Web Source Code Downloader
import urllib.request as u
#urllib.parse, urllib.error
website_name = input("Enter your targer website: ")
source = u.urlopen(website_name)
source_read = source.read()
print(source_read)

