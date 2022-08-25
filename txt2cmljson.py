import os
import re

path = './images/'
currentpath = path

for sccode in os.listdir(currentpath):
    currentpath = os.path.join(path, sccode)
    for term in os.listdir(currentpath):
        currentpath = os.path.join(path, sccode, term)

        try:
            os.mkdir('result')
        except:
            pass
        
        resultfile = open('result/' + term + '.txt', 'w')

        resultfile.write('[\n')
        for filenm in os.listdir(currentpath):
            if not filenm.startswith(".") and filenm.endswith(".txt"):
                print(os.path.join(currentpath, filenm))
                with open(os.path.join(path, sccode, term, filenm), 'r') as f:
                    lines = f.readlines()

                    for line in lines:
                        lrndbrktidx = line.find('(')
                        string = ''
                        if lrndbrktidx != -1:
                            string = line[:lrndbrktidx]
                        else:
                            for idx, char in enumerate(line):
                                if char.isdigit():
                                    string = line[:idx]
                                    break
                            if string == '':
                                string = line

                        if string[0] == '\t':
                            string = string[1:]

                        if string[-1] == '\n':
                            string = string[:-1]
                        
                        while True:
                            if string.endswith(' '):
                                string = string[:-1]
                            else:
                                break

                        resultfile.write('    {\n')
                        resultfile.write('        "text": "' + string + '"\n')
                        resultfile.write('        "label": ""\n')
                        resultfile.write('    },\n')

        resultfile.write(']\n')