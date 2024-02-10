line = str(input()).upper()
array = [0]*26
for letter in line:
    array[ord(letter)-ord('A')] = array[ord(letter)-ord('A')]+1
num_odd = 0
for num in array:
    if num%2!=0:
        num_odd= num_odd+1
if(num_odd>1):
    print('NO SOLUTION')
else:
    string = ''
    if(num_odd==0):
        for num in range(26):
            string = string + chr(ord('A')+num)*(int(array[num]/2))
        print(string + string[::-1])
    else:
        for num in range(26):
            if array[num]%2!=0:
                a = chr(ord('A')+num)
            string = string + chr(ord('A')+num)*(int(array[num]/2))
        print(string + a+string[::-1])
            