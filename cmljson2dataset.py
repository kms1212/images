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

csvf = open('dataset.csv', 'w')

for filename in os.listdir('datasetprep'):
    f = open(os.path.join('datasetprep', filename), 'r')
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
        csvf.write(mealtext.text + ',' + mealtext.label + '\n')
        curmealid += 1
        wf.close()
    f.close()
csvf.close()