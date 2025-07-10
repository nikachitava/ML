import random

# რენდომ რიცხვების გენერაცია
numbers = [random.randint(10, 99) for _ in range(20)]

# ჩაწერა ფაილში
with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")

print("რიცხვები ჩაიწერა numbers.txt ფაილში")