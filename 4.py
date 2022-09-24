year = input()

if year[-1] == '0' and year[-2] == '0':
    century = year[0:-2]
else:
    century = int(year[0:-2]) + 1
    
print(century)