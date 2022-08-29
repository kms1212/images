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
    mtsrc = MealText.from_json(data)
    mtrslt = []

    print(mtsrc.text)
    
    if '/' in mtsrc.text:
        for menu in mtsrc.text.split('/'):
            mtrslt.append(MealText(menu, mtsrc.label))
    elif '&' in mtsrc.text:
        for menu in mtsrc.text.split('&'):
            mtrslt.append(MealText(menu, mtsrc.label))
    else:
        mtrslt.append(MealText(mtsrc.text, mtsrc.label))

    

    for mt in mtrslt:
        wf.write(mt.to_json())

wf.seek(wf.tell() - 2, os.SEEK_SET)
wf.write('\n]')
wf.close()
    
    