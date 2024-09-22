import re


class WordsFinder:

    def __init__(self, *file_names: list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            words = []
            with open(file, encoding='utf-8') as file_now:
                for line in file_now:
                    parts = re.split(r'[ \n,.=!?;:-]', line)
                    words.extend(filter(None,parts))
            all_words[file] = words
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            find_words = {}
            i = 1
            for w in words:
                if w.lower() == word.lower():
                    find_words[name] = i
                    return find_words
                    break
                i += 1

    def count(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            i = 0
            for w in words:
                if w.lower() == word.lower():
                    i += 1
            find_words[name] = i
        return find_words




finder2 = WordsFinder('test_file.txt','test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
