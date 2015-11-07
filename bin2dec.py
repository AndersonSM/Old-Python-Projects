num = '1101001'
num2 = 0

for i in range(len(num)):
    num2 += int(num[i]) * 2**((len(num))-1-i)

print num2