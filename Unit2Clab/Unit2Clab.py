numList=[2,4,6,8,10,12,14,16,18,20,22]
print(numList)

print(len(numList))

print(numList[0])
print(numList[10])

sublist1=numList[0:5]
print(sublist1)

sublist1.insert(0,44)
print(sublist1)

sublist1.append(69)
print(sublist1)

sublist2=sublist1+[8]
print(sublist2)

myclasses=['math','science','computer','history','english',"PE","python"]
print(myclasses)
myclasses.remove ('english')
print(myclasses)

favclass=myclasses.pop(5)
print(favclass)

print('my favorite class is '+ favclass)

