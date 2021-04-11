from urllib import request
import re

# url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

# page = request.urlopen(url)

# contents = page.read()
# page.close()

# print(contents)

# link_start = "linkedlist"
# link_end = '"'

html = request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))