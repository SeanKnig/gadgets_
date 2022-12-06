txt_ = []

def listToString(x):
    str1 = ""
    for ele in x:
        str1 += ele
    return str1

with open('./tether_v0.py', 'r+') as file_to_edit:
    for line in file_to_edit:
        #print(line)
        if "build_app_flag = False" in line:
            print('inline')
            line = "    build_app_flag = True"
            txt_.append(line)
        elif "build_app_flag = True" in line:
            print('inline')
            line = "    build_app_flag = False"
            txt_.append(line)
        elif "build_app_arch = True" in line:
            print('inline')
            line = "    build_app_arch = False"
            txt_.append('\n'+line+'\n')
        elif "build_app_arch = False" in line:
            print('inline')
            line = "    build_app_arch = True"
            txt_.append('\n'+line +'\n')
        else:
            txt_.append(line)

with open('./tether_v0_testout.py', 'w') as file_to_write:
    file_to_write.write(listToString(txt_))
