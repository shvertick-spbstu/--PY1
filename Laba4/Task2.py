def get_count_char(str_):
    str_ = str_.lower()
    list_str = str_.split(" ")
    str_ = "".join(list_str)
    dict_ ={}
    for i in str_:
        if i.isalpha():
            if i not in dict_:
                dict_[i] = 0
            if i in dict_:
                dict_[i] += 1
    return dict_


def get_percent(d):
    sum_ = 0
    for i in d:
        sum_ += d[i]
    for i in d:
        d[i] /= sum_
        d[i] = round(d[i], 2)
    return d


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

result = get_count_char(main_str)
print(result)

result1 = get_percent(result)
print(result1)