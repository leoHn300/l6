def rot(num):
    desint = []
    num = str(num)
    for digit in num:
        desint.append(int(digit))
    for i in range(len(desint)):
        if desint[i] == 6:
            desint[i] = 9
            break
    return int(''.join(map(str, desint)))