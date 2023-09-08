from translate import Translator

translator = Translator(from_lang='en', to_lang='ru')
originalWords: list[str]
translatedWords: list[str] = []
length: int
with open('../data/input.txt') as file:
    originalWords = file.readlines()
length = len(originalWords)
for i in range(length):
    originalWords[i] = result = ''.join(char for char in originalWords[i] if not char.isdigit())
    originalWords[i] = originalWords[i][1:len(originalWords[i]) - 1]
    result = translator.translate(originalWords[i])
    translatedWords.append(result)
with open('../data/output.txt', 'w') as file:
    for i in range(length):
        file.write(f'{i + 1}. {originalWords[i]} - {translatedWords[i]}\n')
