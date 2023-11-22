def count_substring(string, sub_string):
    count = 0
    start_index = 0
    while True:
        index = string.find(sub_string, start_index)
        if index==-1:
            break
        count+=1
        start_index=index+1
    return count  