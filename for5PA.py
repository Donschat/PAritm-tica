num=(int(input('digite o número: ')))
tot=0
for c in range(1, num+1):
    if num%c==0:
        tot+=1
        print
    print('{}'.format(c))
if tot==2:
    print ('o número {} é primo'.format(num))
else:
     print('ele não é primo')
print('o número {} foi divisível {} vezes'.format(num, tot))
