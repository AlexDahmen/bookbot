def open_book(book):
    with open(book) as f:
        return f.read()

def count_words(text):
   words = text.split()
   return len(words)

def instances_of_char(text):
   chars = {}
   for char in text:
       lower_char = char.lower()
       if lower_char in chars:
           chars[lower_char] += 1
       else:
           chars[lower_char] = 1
   return chars        

def sort_on(d):
    return d["num"]

def char_count_to_sorted(char_num_dict):
    sorted_chars = []
    for char in char_num_dict:
        sorted_chars.append({"char": char, "num": char_num_dict[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

def generate_report():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    book_word_count = count_words(book_text)
    char_count_dict = instances_of_char(book_text)
    char_count_sorted_list = char_count_to_sorted(char_count_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{book_word_count} words found in the document")
    print()
    for item in char_count_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character appeared {item['num']} times")
    print()
    print("--- End Report ---")

def main():
    generate_report()

main()
 