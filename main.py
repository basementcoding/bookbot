def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(
                f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")


def get_word_count(text):
    words = text.split()
    return len(words)


def sort_on(dict):
    return dict["count"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "count": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_characters(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
