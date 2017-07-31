def findChars(arr,chara):
    newList = []
    for i in arr:
        print i.find(chara)
        if i.find(chara) >= 0:
            newList.append(i)
    print newList

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChars(word_list,char)