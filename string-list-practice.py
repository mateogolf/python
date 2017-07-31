words = "It's thanksgiving day. It's my birthday,too!"
def find(words):
    print words.find("day")
def replace(words):
    #Replace "day" with "month"
    # arr = words.split("day")
    # replaced = ""
    # for i in range(0,len(arr)-1):
    #     replaced += arr[i] + "month"
    # replaced += arr[len(arr)-1]
    # print replaced
    print words.replace("day","month")

find(words)
replace(words)

x = [2,54,-2,7,12,98]

def printMin(arr):
    # arrMin = arr[0]
    # for i in range(1,len(arr)):
    #     if arrMin > arr[i]:
    #         arrMin = arr[i]
    # print arrMin
    print min(arr)

def printMax(arr):
    # arrMax = arr[0]
    # for i in range(1,len(arr)):
    #     if arrMax < arr[i]:
    #         arrMax = arr[i]
    # print arrMax
    print max(arr)

printMin(x)
printMax(x)

x = [19,2,54,-2,7,12,98,32,10,-3,6]
def sort(arr):
    #sort list
    arr = sorted(arr)
    #split in half
    firstpart, secondpart = arr[:len(arr)/2], arr[len(arr)/2:]
    #first arr to 0 of second half
    secondpart.insert(0,firstpart)
    print secondpart

sort(x)
