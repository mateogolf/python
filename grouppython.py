# STRING: capitalize, upper, lower, count, find, index, split, join, replace, format
#capitalize - arr[0] is capitalized and rest is lower
#counts # of times a substring appears in the string
words = "It's thanksgiving day. It's my birthday,too!"
sub = "day"
print words.count(sub[1])
print words.capitalize() 
print words.upper()
print words.lower()
print str(words.find(sub)) + " index of the substring(day)"
print str(words.index(sub)) + " should return index of substring's occurance"
print words.split(sub), "Above splits the string at substring(day), making an array at that spot, removing substring(day)"
firststr, secondstr = words[:len(words)/2], words[len(words)/2:]
print firststr
print secondstr
s = "-"
print "They're back together: " + s.join(firststr)
print words.replace(sub,"month") + "replaces old string with new string"
first_name,second_name = "Matt","Rod"
print "My name is {} {}".format(first_name,second_name)  #format


# LIST: len, max, min, index, append, pop, remove, insert, sort, reverse, (optional) extend, (optional) list
list1 = ['magical unicorns',19,'hello',98.98,'world',[1000,2,3],[1000,5]]
print list1
print len(list1)
print max(list1)
print min(list1)
print str(list1.index(19)) + " Outputs the index of 19 in array This should be 1"
list1.pop()
print list1
list1.append([1000,5])
print list1
list1.remove("hello")
print list1
list1.insert(2,"hello")
print list1
# sort,
list1.sort()
print list1
# reverse,
list1.reverse()
print list1
# (optional) extend, 
list2 = [2000,2017]
list1.extend(list2)
print list1
# (optional) list
tup1 = 'magical unicorns',19,'hello',98.98,'world',[1000,2,3],[1000,5]
print list(tup1)
