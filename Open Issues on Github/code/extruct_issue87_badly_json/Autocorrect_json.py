#import required libraries
import string
import json
# This is a invalid sample json for testing
jsonld="""
{
{
  "@context": "http://schema.org",
        "@type": "Product",
                "name": "Black 'Clint' FT0511 cat eye sunglasses",
                "image": "https://debenhams.scene7.com/is/image/Debenhams/60742_1515029001",
		"brand": {{
                  "@type": "Thing",
                  "name": "Tom Ford"
                },
                "offers": {
                	"@type": "Offer",
                	"priceCurrency": "GBP",
                	"price": "285.00",
                	"itemCondition": "http://schema.org/NewCondition",
                	"availability": "http://schema.org/InStock"
                }}
    }
}
}
"""
y=""
print("Testing Json.....")
def debugg_json(jsonld):
    count1=jsonld.count('{')
    count2 = jsonld.count('}')
    if(count1<count2):
        jsonld=jsonld[:-1]
    else:
        jsonld = jsonld[1:]
    return jsonld

########################################################

i=0
jsonld=jsonld.translate({ord(c): None for c in (string.whitespace )})
# loop for checking whether issues resolved or not after making each change
while 1:
    # try to parse the json-ld string each time if it is parsable than it becomes valid
    try:
        y=json.loads(jsonld)

        print("Now Json is valid")
        print(y)
        break
    # if json-ld string is not parsable than exception occurs and flow comes to exception block
    except:
        jsonld_list=list(jsonld)
        for k in range (len(jsonld_list)-1):
            if(jsonld_list[k]=='{' and jsonld_list[k+1]=='{'):
                jsonld_list[k+1]=""
        jsonld="".join(jsonld_list)
        # print(jsonld)
        # this function makes changes in json-ld string each time
        jsonld=debugg_json(jsonld)
        i+=1
        if(i==10):
            print("Invalid json ")
            break
        # print(".",end="")
        continue
