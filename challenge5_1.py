import pickle
from urllib.request import urlopen

raw = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

data = pickle.load(raw)

for item in data:
    for thing in item:
        print(thing[0] * thing[1])
    print("")
