import json
import os

filename = "result/2021-02-lㄹ.json"

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
    
    if '밥' in mealtext.text:
        mealtext.label = 'rice'
    elif '라이스' in mealtext.text:
        mealtext.label = 'rice'
    elif '국' in mealtext.text:
        mealtext.label = 'soup'
    elif '찌개' in mealtext.text:
        mealtext.label = 'soup'
    elif '탕' in mealtext.text:
        mealtext.label = 'soup'
    elif '스프' in mealtext.text:
        mealtext.label = 'soup'
    elif '수프' in mealtext.text:
        mealtext.label = 'soup'
    elif '죽' in mealtext.text:
        mealtext.label = 'porridge'
    elif '면' in mealtext.text:
        mealtext.label = 'noodle'
    elif '파스타' in mealtext.text:
        mealtext.label = 'noodle'
    elif '국수' in mealtext.text:
        mealtext.label = 'noodle'
    elif '떡' in mealtext.text:
        mealtext.label = 'rice_cake'
    elif '설기' in mealtext.text:
        mealtext.label = 'rice_cake'
    elif '빵' in mealtext.text:
        mealtext.label = 'bread'
    elif '케이크' in mealtext.text:
        mealtext.label = 'bread'
    elif '케익' in mealtext.text:
        mealtext.label = 'bread'
    elif '케잌' in mealtext.text:
        mealtext.label = 'bread'
    else:
        mealtext.label = ''

    wf.write(mealtext.to_json())
wf.seek(wf.tell() - 2, os.SEEK_SET)
wf.write('\n]')
wf.close()
    
    