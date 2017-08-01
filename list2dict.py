def make_dict(arr1, arr2):
    new_dict = {}
    #Error Case: what is arrays are different length
    if len(arr1) >= len(arr2):
        keys = arr1
        data = arr2
    else:
        keys = arr2
        data = arr1
    for i in range(0,len(keys)):
        new_dict[keys[i]] = data[i]
        print "{}: {}".format(keys[i],data[i])
    return new_dict

# function input
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
print make_dict(name,favorite_animal)