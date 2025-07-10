import matplotlib.pyplot as plt

# ხაზოვანი დიაგრამა
# # მონაცემები
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]
#
# # ხაზოვანი გრაფიკი
# plt.plot(x, y)
#
# # სათაური და ღერძები
# plt.title("ხაზოვანი გრაფიკი")
# plt.xlabel("X ღერძი")
# plt.ylabel("Y ღერძი")
#
# # გრაფიკის ჩვენება
# plt.show()

#####################################
# ბარ ჩართი
# categories = ["A", "B", "C", "D"]
# values = [10, 24, 36, 18]
#
# plt.bar(categories, values)
# plt.title("ბარის გრაფიკი")
# plt.xlabel("კატეგორიები")
# plt.ylabel("მნიშვნელობები")
# plt.show()


#########################
# წერტილოვანი გრაფიკი (Scatter Plot)
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("x ღერძი")
plt.ylabel("y ღერძი")
plt.show()


