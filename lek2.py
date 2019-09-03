namn = input('namn: ')
age = int(input('ålder: '))

print('hej ' + namn + ' du är ' + str(age) + ' år gammal') 

if age > 18: 
    print('Du är 18 eller äldre')
elif age < 18:
    print('Du är yngre en 17')
else: 
    print('du är 18')