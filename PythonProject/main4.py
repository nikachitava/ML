import numpy as np
from scipy import stats

# ფაილის წაკითხვა და გარდაქმნა რიცხვებად
with open("numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f.readlines()]

# numpy array
arr = np.array(numbers)

# გამოთვლები
total = np.sum(arr)
mean = np.mean(arr)
mode = stats.mode(arr, keepdims=True).mode[0]
std_dev = np.std(arr)

# შედეგების დაბეჭდვა
print("🔢 რიცხვები:", numbers)
print("📌 ჯამი:", total)
print("📌 საშუალო:", mean)
print("📌 მოდა:", mode)
print("📌 სტანდარტული გადახრა:", std_dev)
