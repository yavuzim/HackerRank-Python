if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    index = arr.index(arr[len(arr)-1])
    print(arr[index - 1])
