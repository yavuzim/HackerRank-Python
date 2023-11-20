if __name__ == '__main__':
    N = int(input())
    arr = []
    for index in range(N):
        inputValue = input().split()
        if inputValue[0]=="insert":
            arr.insert(int(inputValue[1]),int(inputValue[2]))
        elif inputValue[0]=="print":
            print(arr)
        elif inputValue[0]=="remove":
            arr.remove(int(inputValue[1]))
        elif inputValue[0]=="append":
            arr.append(int(inputValue[1]))
        elif inputValue[0]=="sort":
            arr.sort()
        elif inputValue[0]=="pop":
            arr.pop()
        else:
            arr.reverse()