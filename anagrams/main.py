def filereader(file_path):
    with open(file_path, 'r') as txtfile:
        read_data = txtfile.read()
    return read_data

def parse_word(word):
    if word.endswith('.'):
        return word.replace('.', '')
    if word.endswith(','):
        return word.replace(',', '')
    if word.endswith('?'):
        return word.replace('?', '')
    if word.endswith('!'):
        return word.replace('!', '')
    return word.lower()

def main():
    data = filereader('text.txt')
    words = []
    for word in data.replace('\n', ' ').split(" "):
        words.append(parse_word(word))

    anagrams = {}
    for word in words:
        if tuple(sorted(word)) in anagrams:
            if not word in anagrams[tuple(sorted(word))]:
                anagrams[tuple(sorted(word))] += [word]
        else:
            anagrams[tuple(sorted(word))] = [word]

    for anagram in anagrams.values():
        if len(anagram) > 1:
            print(anagram)

main()