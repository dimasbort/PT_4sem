from statistics import median


def toFixed(number, digits=0):
    return f"{number:.{digits}f}"

def text_info(text): #testing strings testing for sorting sorting testing. Second sentence and now. Third one.
    words_list = text\
        .replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('(', '').replace(')', '')\
        .split()
    words_dict = {words_list[word]: 0 for word in range(len(words_list))}
    for word in range(len(words_list)):
        words_dict[words_list[word]] += 1
    words_dict = {k: words_dict[k] for k in sorted(words_dict, key=words_dict.get, reverse=True)}
    for word in words_dict:
        number = str(words_dict[word])
        sharps_number = int(toFixed(words_dict[word] / len(words_list) / 0.1)) + 1
        sharps = '#' * sharps_number + '-' * (10 - sharps_number)
        print("{:<10} {:<5} {:<12} ".format(word, number, '[' + sharps + ']'))

def sentence_info(text):
    sentence_list = text\
        .replace(',', '').replace('(', '').replace(')', '')\
        .replace('!', '.').replace('?', '.')\
        .split('.')
    if sentence_list[len(sentence_list) - 1] == '':
        sentence_list.pop()
    word_count = 0
    sentence_count = 0
    for sentence in sentence_list:
        word_count += len(sentence.split())
        sentence_count += 1
    print(f'Кол-во слов: {str(word_count)} и среднее количество слов в предложении: '
          f' {str(toFixed(word_count/sentence_count, 3))}')

def gramms_info(text, k = 5, n = 3):
    words_list = text.replace('.', '').replace(',', '').split()
    arr = list()
    for index in range(len(words_list) - n + 1):
        words = ''
        for ind in range(n):
            words += words_list[index + ind] + ' '
        arr.append(words)
    arr.sort(key=len, reverse=True)
    for index in range(k):
        print(arr[index])

if __name__ == '__main__':
    text = input()
    print('Информация про кол-во употреблений слов в тексте:')
    text_info(text)
    print('Информация про среднее кол-во слов в предложении: ')
    sentence_info(text)
    print('Информация про медианное количество слов в предлложении')
    print('What is median')
    print('Информация про ТОП-k N-граммов:')
    print('Введите k: ')
    k = int(input())
    print('Введите n: ')
    n = int(input())
    gramms_info(text, k, n)
