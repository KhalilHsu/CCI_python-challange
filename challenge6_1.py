import zipfile
import re

nth = "90052"
pattern = re.compile("Next nothing is (\d+)")
file = zipfile.ZipFile("channel.zip", "r")

comments = []
while True:
    content = file.read(nth+'.txt').decode('utf-8')
    print(content)
    comments.append(file.getinfo(nth+'.txt').comment.decode('utf-8'))
    match = pattern.search(content)
    if match == None:
        break
    nth = match.group(1)

print(''.join(comments))