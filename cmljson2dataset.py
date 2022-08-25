import json
import os
import shutil

curmealid = 0

shutil.rmtree('dataset')

class MealText:
    def __init__(self, text, label):
        self.text = text
        self.label = label

    @staticmethod
    def from_json(json_dct):
      return MealText(json_dct['text'], json_dct['label'])

    def __str__(self):
        return self.text + ' ' + self.label

for filename in os.listdir('result'):
    f = open(os.path.join('result', filename), 'r')
    jsdata = json.load(f)

    try:
        os.mkdir('dataset')
    except:
        pass
    
    for data in jsdata:
        mealtext = MealText.from_json(data)
        if mealtext.label == '':
            mealtext.label = 'none'
        
        try:
            os.mkdir(os.path.join('dataset', mealtext.label))
        except:
            pass

        wf = open(os.path.join('dataset', mealtext.label, 'meal_' + str(curmealid) + '.txt'), 'w')
        wf.write(mealtext.text)
        curmealid += 1
    