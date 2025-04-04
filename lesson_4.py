def most_common_word(t):
    counts = {}
    for word in t.split():
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    most_common = max(counts, key=counts.get)
    return most_common



lines_count = 0
words_count = 0
unique_word_count = 0

unique_words = set()


f = open("files/text.txt", "r")
lines = f.readlines()
text = f.read()

for i in lines:
    lines_count += 1
    words_count += len(i.split())

    words_in_line = i.split()
    unique_words.update(word.lower() for word in words_in_line)


text = text.lower()

unique_word_count = len(unique_words)
most_common = most_common_word(' '.join(lines))
f.close()


print("ტექსტში არის " + str(lines_count) + " სტრიქონი")
print("ტექსტში არის " + str(words_count) + " სიტყვა")
print("ტექსტში არის " + str(unique_word_count) + " უნიკალური სიტყვა")
print("ტექსტში ყველაზე ხშირად გამოყენებული სიტყვა: " + most_common)
