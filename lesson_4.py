# f = open("files/text.txt", "w")
# f.write("test string")
# f.close()

lines_count = 0
f = open("files/text.txt", "r")
lines = f.readlines()
for i in lines:
    lines_count += 1
f.close()


print("ტექსტში არის " + str(lines_count) + " სტრიქონი")