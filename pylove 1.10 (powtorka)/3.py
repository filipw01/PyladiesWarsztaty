def my_hash(input):
    list = ""
    for i in range(len(input)):
        list+=chr(((ord(input[i])-96 )%26)+97)
    return list

print(my_hash("abcdefghijklmnoprstuwxyz"))