import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()
import xml.etree.ElementTree as ET


user_input = 'What is your name?'
instance='160'
message=user_input
message = message.replace(' ', '+')
user='mhowell95'
password='606744HMj'
applicationID='3087601344337415072'
#formatting our information into a URL
url = "http://www.botlibre.com/rest/botlibre/form-chat?instance=%s&message=%s$user=%s&password=%s&application=%s" % \
	(instance,message,user,password,applicationID)
#making the GET request with authorization
response = requests.get(url, auth=(user,password))

#calling an external library to parse the XML while accessing this parsed formate
root = ET.fromstring(response.text)
response_message = root[0].text

#printing the clean, parsed result
print response_message

