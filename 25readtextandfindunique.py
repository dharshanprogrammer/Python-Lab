import string
def find_unique_words(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        content = content.lower()

        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        content = content.translate(translator)

        words = [word for word in content.split() if word]

        unique_words_set = set(words)

        sorted_unique_words = sorted(list(unique_words_set))

        print(f"--- Unique Words from '{filepath}' (Sorted) ---")
        for word in sorted_unique_words:
            print(word)

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
file_to_process = 'input.txt'
try:
    with open(file_to_process, 'w') as f:
        f.write("Hello world. This is a Test file. World is amazing. Test test.")
except:
    pass
find_unique_words(file_to_process)