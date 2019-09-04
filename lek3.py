lösen = input('Lösen: ')
passCount = len(lösen)
#print(passCount)
if len(lösen) < 8:
    print('Under 3 karaktärer')
elif passCount > 20:
    print('För långt')
else:
    print('<o/')
