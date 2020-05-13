#To add new elements in the list at the end
list1 = ['Biology','Physics','Maths']
list1.append('Chemistry')
print(list1)
#To assign new element to a list at a particular Index
list2 = ['Geography','History']
list2.insert(0,'Economics')
print(list2)

#To access elements from a tuple using indexes
myTuple = ('Biostat','Biochem','Microbio','Animal Science')
Tuple1 = (20,30,40,50,60,70,80)
print("The subject is: ", myTuple[2])
print("The numbers are: ", Tuple1[2:6])

#To delete different Dictinary Elements
myDict = {"Sad":"Happy","Bad":"Good","Above":"Below","Warm":"Cool","Fat":"Thin","Fall":"Rise"}
print(myDict)
#Using del function:
del myDict["Above"]
print(myDict)
#Using pop function:
myDict.pop("Sad")
print(myDict)
