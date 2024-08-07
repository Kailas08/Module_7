class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(punct, '')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        words_dict = self.get_all_words()
        result = {}
        for file_name, words in words_dict.items():
            try:
                position = words.index(word)
                result[file_name] = position
            except ValueError:
                result[file_name] = -1  # Если слово не найдено
        return result

    def count(self, word):
        word = word.lower()
        words_dict = self.get_all_words()
        result = {}
        for file_name, words in words_dict.items():
            count = words.count(word)
            result[file_name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиция первого слова 'text'
print(finder2.count('teXT'))  # Количество слов 'text'