if __name__ == '__main__':
    grade = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade.append([name, score])
        scoreList.append(score)
scoreList.sort(reverse=False)
newList = []
for item in scoreList:
    if not item in newList:
        newList.append(item)

n = newList[1]

outputList = []

for index in range(0, len(grade)):
    if grade[index][1]==n:
        outputList.append([grade[index][0]])

outputList.sort(reverse=False)

matris_value = [" ".join(map(str, row)) for row in outputList]
result_string = "\n".join(matris_value)
print(result_string)