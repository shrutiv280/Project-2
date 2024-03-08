def count_words(text):
    return len(text.split())

def main():
    user_input = input("Enter a sentence or paragraph: ")
    word_count = count_words(user_input)
    print("Word count:", word_count)

if __name__ == "__main__":
    main()
