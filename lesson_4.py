lines_count = 0
words_count = 0

f = open("files/text.txt", "r")
lines = f.readlines()
for i in lines:
    lines_count += 1
    words_count += len(i.split())
f.close()


print("ტექსტში არის " + str(lines_count) + " სტრიქონი")
print("ტექსტში არის " + str(words_count) + " სიტყვა")
