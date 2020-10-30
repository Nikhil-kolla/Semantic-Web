#import required libraries
from extruct.jsonld import JsonLdExtractor
import pprint
pp = pprint.PrettyPrinter(indent=2)
import urllib.request
# For open url connection
fp = urllib.request.urlopen("https://www.debenhams.com/sale")
# Read the content available on the url
mybytes = fp.read()
#  Decode the content
mystr = mybytes.decode("utf8")
# close the connection
fp.close()
# print(mystr)
print("###########################")
# Using extruct parse the HTML string
data = JsonLdExtractor().extract(mystr)
pp.pprint(data)
