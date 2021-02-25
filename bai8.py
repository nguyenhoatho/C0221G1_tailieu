import shutil, os
import string
def timphantulonnhatvàinragiatri():
    with open(file='E:\pythonProject4/baitapvenha/baibao.txt',mode='r',encoding='utf-8') as f:
        a=f.read()
        stra=str(a)
        stra=stra.replace('.','')
        stra=stra.replace(',','')
        stra=stra.replace('"','')
        stra=stra.replace('-','')
        mangstra=stra.split()
        mangstra=sorted(mangstra,reverse=0)
        count={}
        a=[]

        for x in mangstra:
            if x in count:
               count[x] += 1
            else:
                    count[x] = 1
        a=max(count.items(),key=lambda k:k[1])
        print(a )
        for i in count:
            print(i, count[i])

print(timphantulonnhatvàinragiatri())




















