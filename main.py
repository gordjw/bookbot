def main():
    title = "frankenstein"
    text = read_book(title)
    words = get_words_in_book(text)

    print(f"There are {len(words)} words in {title}")

    chars = get_sorted_chars(words)
    for item in chars:
        print(f"The character {item['char']} was found {item['num']} times")

    print("----- End of report -----")


def read_book(title):
    with open(f"books/{title}.txt") as f:
        file_contents = f.read()

    return file_contents


def get_words_in_book(text):
    return text.split()


def get_sorted_chars(words):
    chars = {}
    for word in words:
        for char in word:
            if not char.isalpha():
                continue

            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    sorted_chars = []
    for c in sorted(chars):
        sorted_chars.append({ "char": c, "num": chars[c] })

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars


def sort_on(d):
    return d["num"]

main()