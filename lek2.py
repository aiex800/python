namn = input('namn: ')
age = input('ålder: ')

print('hej ' + namn + ' du är ' + str(age) + ' år gammal') 

if age > 17: 
    print('Du är 18 eller äldre')
elif age < 18: 
    print('Du är yngre en 17')