import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# File1.xlsx წაკითხვა
df = pd.read_excel("data.xlsx")

# მოდით ვივარაუდოთ, რომ გვინდა პროგნოზი სახელზე დაყრდნობით — არასწორია.
# ამიტომ ვაგებთ მაგალითურად რეგრესიას: ასაკი → ქულა (random)

# ასაკი (X)
X = df[["age"]]

# ქულა (Y) - გენერირდება რენდომად (მაგალითად, ტესტის ქულები)
np.random.seed(0)
df["ქულა"] = df["age"] + np.random.randint(-10, 10, size=len(df))
y = df["ქულა"]

# მოდელის შექმნა და სწავლება
model = LinearRegression()
model.fit(X, y)

# პროგნოზი (გადავატაროთ იგივე ასაკებს)
y_pred = model.predict(X)

# ვიზუალიზაცია
plt.scatter(X, y, color="blue", label="რეალური მონაცემები")
plt.plot(X, y_pred, color="red", label="რეგრესიული ხაზი")
plt.xlabel("ასაკი")
plt.ylabel("ქულა")
plt.title("წრფივი რეგრესია: ასაკი vs ქულა")
plt.legend()
plt.grid(True)
plt.show()

# დაბეჭდე slope და intercept
print("Slope (დახრილობა):", model.coef_[0])
print("Intercept (გადაკვეთა):", model.intercept_)
