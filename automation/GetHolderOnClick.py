def GetHolderOnClick(holderNum):
    storeArr =[]
    initial = 1
    initial2 = 1
    start = '''
        } else if (holder instanceof Ribbon%sHolder) {
    RibbonItem currentItem = (RibbonItem) mRibbonList.get(position);
    '''%(holderNum)
    storeArr.append(start)
    for i in range(holderNum):
        mid = "((Ribbon%sHolder) holder).mImageView%s.setImageResource(currentItem.getImageResource%s());"%(holderNum, i+1, i+1)
        final = '''
                    ((Ribbon%sHolder) holder).mImageView%s.setOnClickListener(new View.OnClickListener() {
                        public void onClick(View view) {
                            showPopup(view, oaks, %s);
                }
            });
            '''%(holderNum, i+1, i)
        storeArr.append(mid)
        storeArr.append(final)
    listToStrList = ' '.join([(elem) for elem in storeArr]) 
    print(listToStrList)
    file1 = open("this.txt","a")  
    file1.writelines(listToStrList)
for i in range(1,50):
    GetHolderOnClick(i)
