# Program to read all the lines in a file using readline() function
file = open("input.txt", "r")
left = []
right = []
sum = 0
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

for index in range(len(left)):
    sum = sum + abs(left[index] - right[index])
    # print(left[index], "=", right[index]," = ",abs(left[index]-right[index]))

# print(left)
# print(right)
print(sum)
