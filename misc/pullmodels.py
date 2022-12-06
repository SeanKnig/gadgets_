import os,sys,re


with open('models.py') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    #re.search(r'Part 1\.(.*?)Part 3', s).group(1)
    #print(lines)
    
    for line in lines:
        #Fetching class name
        #field = re.search(r'\t(.*)', str(line), re.DOTALL).group(1)
        
        if line.startswith('class'):
            #print(line)
            class_name = re.search(r'class (.*)', str(line), re.DOTALL).group(1)
            clean_name = class_name.replace('(models.Model):', '')
            print(clean_name)
        if line.startswith('    '):
            field = re.search(r'    (.*)', str(line), re.DOTALL).group(1)
            field = field.split(" ", 1)
            print(field[0])
