#Write  a program named count_word_occurrences that reads a text file names 'data_2.txt'.
#The program counts the occurrence of each unique word, then displays the number
#of occurrences of each word, and the word with the highest frequency.
#The content of data_2.txt file:
#"The quick brown fox jumps over the lazy dog.
# The dog was not lazy, but rather energetic.
# Foxes are quick and the dog is clever."

# import os

def count_word_occurrences():
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # file_name = os.path.join(script_dir, "data_2.txt")
    file_name = "data_2.txt"
    count_dic = {}
    with open(file_name, "r") as file:
        text = file.read().lower()
        text = text.replace(",", "")
        text = text.replace(".", "")
        words = text.split()
        for word in words:
            count_dic[word] = count_dic.get(word, 0) + 1
    return count_dic

def main():
    word_count = count_word_occurrences()
    for i, (word, count) in enumerate(word_count.items()):
        if i == len(word_count) - 1:
            print(f"{word}: {count}")
        else:
            print(f"{word}: {count}", end = ", ")

    # formatted_words = [f"{word}: {count}" for word, count in word_count.items()]
    # print(", ".join(formatted_words))

    most_frequent_word = max(word_count, key=word_count.get)
    most_frequent_count = word_count[most_frequent_word]
    print(f"The word with the most frequency is {most_frequent_word} which appears {most_frequent_count} times.")

main()