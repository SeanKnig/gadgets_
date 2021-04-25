import os
with open('control-panel/tools/file.txt', 'r+') as f:
    
    file_source = f.read()
    replace_string = file_source.replace('NULL', '')
    #save output
    f.write(replace_string)