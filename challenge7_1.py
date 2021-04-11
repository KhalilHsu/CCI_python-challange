import Image

oxygen - Image.open("oxygen.png")
size = width, height = 629, 95

y = 48
end = 607
step = 7

new_string = ""

to_change = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for item in to_change:
    new_string += chr(item)

print(new_string)