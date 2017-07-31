# def odd_even():
#     for i in range(2001):
#         if i%2==0:
#             oddEven = "even"
#         else:
#             oddEven = "odd"
#         print "Number is {}. This is an {} number.".format(i,oddEven)

# odd_even()

def multiply(arr,val):
    for i in range(0,len(arr)):
        arr[i] *= val
    return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):#=multiply()):
    # print arr
    new_array = []
    for outidx in range(0,len(arr)): #outer for that adds array to newList[outidx]
        # length = arr[outidx]
        innerList = []
        for inner in range(0,arr[outidx]):
            innerList.append(1)
        new_array.append(innerList)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
# >>>[6,12,15]
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]