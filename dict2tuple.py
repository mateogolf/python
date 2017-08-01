def dict2Tuple(obj):
    arr = []
    for key,data in obj.iteritems():
        temp = (key,data)
        arr.append(temp)
    return arr

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
print dict2Tuple(my_dict)
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]