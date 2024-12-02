# Program to read all the lines in a file using readline() function
file = open("input.txt", "r")
left = []
right = []
ldict = {}
sum = 0
similarity = 0
while True:
    content = file.readline()
    if not content:
        break
    elif any(element.isdigit() for element in content):
        ltmp, rtmp = content.split()
        left.append(int(ltmp))
        right.append(int(rtmp))
file.close()

left.sort()
right.sort()

for index in iter(set(left)):
    ldict[index] = 0

for element in left:
    count = right.count(element)
    if count > 0:
        similarity += element * count

# print(left)
# print(right)
print(similarity)
