def get_book_text(file_path):
    with open(file_path) as f:
        file_content_string = f.read()
        return file_content_string
    

def words_count(file_content_string):
    Count = file_content_string.split()
    print(f"Found {len(Count)} total words")


def character_count(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(item):
    return item["num"]

def sorted_list(dict_of_caracteres):
    letters = [{"char": k, "num": v} for k, v in dict_of_caracteres.items()]
    letters.sort(reverse=True, key=sort_on)
    return letters
