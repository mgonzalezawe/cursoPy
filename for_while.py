"""#Enumerate
for i, char in enumerate('Hola'):
    print(i, char)
    
jk = [1,2,3,4]
print(list(enumerate(jk)))

for i, num in enumerate(list(range(50))):
    print(i,num)
    if(num == 10):
        print(f'index of {i} es: {i}')"""
        
#For y While
list = [1, 2, 3]
for i in list:
    print(i)
    
i = 1
while i<= len(list):
    print(i)
    i+=1
    
