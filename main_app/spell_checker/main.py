import os
from main_app.spell_checker.spell import is_banan_correctly
from main_app.spell_checker.spell import suggested_word

script_path = os.path.dirname(os.path.abspath(__file__))
list_path = os.path.join(script_path, 'list.txt')

class Main:
    def getResult(self, values):
        result = []
        for value in values.split(" "):
            if not is_banan_correctly(value):
                result.append({
                    'correct': False,
                    'query_word': value,
                    'correct_word': str(suggested_word(value))
                })
            else:
                result.append({
                    'correct': True,
                    'query_word': value,
                    'correct_word': value
                })
        return result
    
    
    def addNewWord(self, string):
        print(string)
        words = string.split(' ')
        result = []

        cur_list = set()

        with open(list_path, 'r', encoding="utf-8") as ww:
            for word in ww:
                cur_list.add(word.rstrip('\n'))

        with open(list_path, 'a', encoding="utf-8") as dictionary:
            for word in words:
                if word in cur_list:
                    result.append({
                        'correct': False,
                        'word': word,
                    })
                else:
                    result.append({
                        'correct': True,
                        'word': word,
                    })
                    dictionary.write(word+'\n')
        
        return result
    
    
    def getAllWords(self):
        cur_list = []

        with open(list_path, 'r', encoding="utf-8") as ww:
            for word in ww:
                cur_list.append(word.rstrip('\n'))
        
        return cur_list