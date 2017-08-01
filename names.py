def printListofDictNames(arr):
    for name in arr:
        print "{} {}".format(name["first_name"],name["last_name"])

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
printListofDictNames(students)

def printDictofListofNames(obj):
    for key,arr in obj.iteritems():
        print key
        for num in range(0,len(arr)): #arr is an array
            first = arr[num]["first_name"]
            last = arr[num]["last_name"]
            namelength = (len(first) + len(last))
            print "{} - {} {} - {}".format((num+1),first,last,namelength)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
printDictofListofNames(users)
