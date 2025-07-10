import string
import random
import pandas as pd

def random_string(lenght=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenght))

data = []

for _ in range(10):
    name = random_string()
    surname = random_string()
    age = random.randint(18, 65)
    data.append({"name: ": name, "surname": surname, "age": age})

df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)

print("Finish")
