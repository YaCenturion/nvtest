Arr = [1,2,3,4,1,2,3,1,2,1]

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

def counte(arr):
    # print(arr)
    count = 0
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    for x in arr:
        # print(x)
        if x == 4:
            temp4 += 1
        elif x == 3:
            temp3 += 1
        elif x == 2:
            temp2 += 1
        elif x == 1:
            temp1 += 1
        # Number  # 1 has 4 occurrences.
    return temp1, temp2, temp3, temp4


if __name__ == '__main__':
    temp1, temp2, temp3, temp4 = counte(Arr)
    print(f'Number #1 has {temp1} occurrences.')
    print(f'Number #2 has {temp2} occurrences.')
    print(f'Number #3 has {temp3} occurrences.')
    print(f'Number #4 has {temp4} occurrences.')