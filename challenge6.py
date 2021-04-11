import zipfile

file = zipfile.ZipFile("channel.zip")

comments = []

def next_nothing(filename):
    text = file.read(filename)
    next = text.split()[-1]

    if (next != "comments."):
        next_nothing(next + ".txt")
        comments.append(file.getinfo(next + ".txt").comment)

next_nothing( "90052.txt" )

for comment in reversed(comments):
    print(comment)