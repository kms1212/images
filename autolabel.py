import json
import os

filename = "result/2022-01-l.json"

class MealText:
    def __init__(self, text, label):
        self.text = text
        self.label = label

    @staticmethod
    def from_json(json_dct):
      return MealText(json_dct['text'], json_dct['label'])

    def to_json(self):
        return '    {\n        "text": "%s",\n        "label": "%s"\n    },\n' % (self.text, self.label)

    def __str__(self):
        return self.text + ' ' + self.label

f = open(filename, 'r')
jsdata = json.load(f)
f.close()

wf = open(filename, 'w')
wf.write('[\n')
for data in jsdata:
    mealtext = MealText.from_json(data)
    
    if '국' in mealtext.text:
        mealtext.label = 'soup'
    elif '밥' in mealtext.text:
        mealtext.label = 'rice'
    elif '라이스' in mealtext.text:
        mealtext.label = 'rice'
    elif '필라프' in mealtext.text:
        mealtext.label = 'rice'
    elif '국수' in mealtext.text:
        mealtext.label = 'noodle'
    elif '멘' in mealtext.text:
        mealtext.label = 'noodle'
    elif '국' in mealtext.text:
        mealtext.label = 'soup'
    elif '찌개' in mealtext.text:
        mealtext.label = 'soup'
    elif '개장' in mealtext.text:
        mealtext.label = 'soup'
    elif '요거' in mealtext.text:
        mealtext.label = 'processed'
    elif '요구르트' in mealtext.text:
        mealtext.label = 'processed'
    elif '쿨피스' in mealtext.text:
        mealtext.label = 'processed'
    elif '푸딩' in mealtext.text:
        mealtext.label = 'processed'
    elif '탕' in mealtext.text:
        if '탕수' not in mealtext.text and '탕평채' not in mealtext.text:
            mealtext.label = 'soup'
        else:
            mealtext.label = ''
    elif '스프' in mealtext.text:
        mealtext.label = 'soup'
    elif '수제비' in mealtext.text:
        mealtext.label = 'soup'
    elif '수프' in mealtext.text:
        mealtext.label = 'soup'
    elif '주스' in mealtext.text:
        mealtext.label = 'processed'
    elif '짜계치' in mealtext.text:
        mealtext.label = 'noodle'
    elif '죽' in mealtext.text:
        mealtext.label = 'porridge'
    elif '면' in mealtext.text:
        mealtext.label = 'noodle'
    elif '우동' in mealtext.text:
        mealtext.label = 'noodle'
    elif '파이' in mealtext.text:
        mealtext.label = 'bread'
    elif '파스타' in mealtext.text:
        mealtext.label = 'noodle'
    elif '스파게티' in mealtext.text:
        mealtext.label = 'noodle'
    elif '떡' in mealtext.text:
        if '떡볶이' not in mealtext.text and '떡갈비' not in mealtext.text and '소떡' not in mealtext.text:
            mealtext.label = 'rice_cake'
        else:
            mealtext.label = ''
    elif '설기' in mealtext.text:
        mealtext.label = 'rice_cake'
    elif '빵' in mealtext.text:
        mealtext.label = 'bread'
    elif '피자' in mealtext.text:
        mealtext.label = 'bread'
    elif '샌드위치' in mealtext.text:
        mealtext.label = 'bread'
    elif '버거' in mealtext.text:
        mealtext.label = 'bread'
    elif '브레드' in mealtext.text:
        mealtext.label = 'bread'
    elif '케이크' in mealtext.text:
        mealtext.label = 'bread'
    elif '케익' in mealtext.text:
        mealtext.label = 'bread'
    elif '케잌' in mealtext.text:
        mealtext.label = 'bread'
    elif '오렌지' in mealtext.text:
        mealtext.label = 'fruit'
    elif '파인애플' in mealtext.text:
        mealtext.label = 'fruit'
    elif '메론' in mealtext.text:
        mealtext.label = 'fruit'
    elif '멜론' in mealtext.text:
        mealtext.label = 'fruit'
    elif '수박' in mealtext.text:
        mealtext.label = 'fruit'
    elif '사과' in mealtext.text:
        mealtext.label = 'fruit'
    elif '바나나' in mealtext.text:
        mealtext.label = 'fruit'
    elif '딸기' in mealtext.text:
        mealtext.label = 'fruit'
    elif '소스' in mealtext.text:
        mealtext.label = ''
    else:
        mealtext.label = ''

    wf.write(mealtext.to_json())
wf.seek(wf.tell() - 2, os.SEEK_SET)
wf.write('\n]')
wf.close()
    
    