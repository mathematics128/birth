# 警告：以下代码仅为示例，可以运行，请随意尝试！

from classmates import LC
from random import randint
from datetime import datetime

def happy_birthday(person):
    sentenses = ['生日快乐！', '天天开心！', '时来运转！', '长命百岁！', '你可爱死我了知道不']
    sentense = person + '，' + sentenses[randint(0, 4)]
    return sentense

date = datetime.now().strftime('%m-%d')
if date == LC.birthday:
    for i in range(52):
        print(happy_birthday(LC.name))

