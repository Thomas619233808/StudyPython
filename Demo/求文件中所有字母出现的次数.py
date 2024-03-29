from collections import Counter

def count_letters(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            # 读取文件内容并将所有非字母字符替换为空格
            content = file.read().replace('\n', ' ').replace('\r', ' ')
            letters = [char.lower() for char in content if char.isalpha()]

            letters_counts = Counter(letters)
            for letter, count in letters_counts.items():
                print(f"{letter}: {count}")

    except FileNotFoundError:
        print("File Not Find")

    except Exception as e:
        print(e)

count_letters('./counts')
