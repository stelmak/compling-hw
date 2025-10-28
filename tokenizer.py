#загружаем все, ранне установленные, библиотеки
import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
import spacy

class TextTokenizer: # специальный класс, внутри которого будут находиться все необходимые функции
    def __init__(self):
        pass

    def simple_tokenize(self, text): #простой токенайзер с помощую регулярного выражения, не находит знаки припенания
        try: #пробуем воспроизвести код, если библиотека не установлена, будет выведена ошибка

            tokens = re.findall(r"\w+", text) #находим все повторяющиеся символы слова(_, буквы разных алфовитов, цифры), до первого символа не являющегося символом слова (например пробелом)
        except:
            return('Ошибка')
        
        if len(tokens) == 0: #если на вход был введён текст не сождержащий символов
            return 'Ошибка'
        else:
            return tokens

    def nltk_tokenize(self, text): #токенизирует текст с помощью библиотеки nltk

        try:#пробуем воспроизвести код, если библиотека не установлена, будет выведена ошибка
            tokens = nltk.word_tokenize(text)#используем команду word_tokenize, чтобы вывести каждый токен
        except:
            return "Ошибка"
    
        if len(tokens) == 0: #если на вход был введён текст не сождержащий символов
            return "Ошибка"
        else:
            return tokens

    def spacy_tokenize(self, text): #токенизирует текст с помощью библиотеки spaСy

        try:#пробуем воспроизвести код, если библиотека не установлена, будет выведена ошибка
            nlp = spacy.load("ru_core_news_sm") #загружаем пайплан для токенизации, в нашем случае он русский
            doc = nlp(text) #проводим токенизацию
            tokens = [] #список для сохранения строчек после преобразования из хаш-значений

            for t in doc: #выводим отдельно каждый токен как строку и сохраняем в список
                tokens.append(t.text)
        except:
            return 'Ошибка'

        if len(tokens) == 0: #если на вход был введён текст не сождержащий символов
            return "Ошибка"
        else:
            return tokens

    def tokenize_all(self, text): #функция для одновременного проведения всех видов токенизации

        t_1 = self.simple_tokenize(text)
        t_2 = self.nltk_tokenize(text)
        t_3 = self.spacy_tokenize(text)
        
        all = {'simple': t_1, #сохраняем полученнные результаты в словарь
               'nltk': t_2,
               'spaCy': t_3}
        
        return all

def demo(): #необходима для тестирования внутри модуля
    tokenizer = TextTokenizer()

    sample_text = "Hello, world! This is a test sentence. How are you today?"

    results = tokenizer.tokenize_all(sample_text)

    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    demo()