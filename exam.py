n = int(input())
myAnswer = input()
friendAnswer = input()

match = 0
for i in range(len(myAnswer)):
    if myAnswer[i] == friendAnswer[i]:
        match+=1
if match > n:
    print(n+len(myAnswer)-match)
else:
    print(match+len(myAnswer)-n)





