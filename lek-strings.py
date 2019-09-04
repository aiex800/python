firstName = "Alexander"
middleName = "Johan"
lastName = "Häggström"

nickName = "<o/"
mail = "@elev.ga.ntig.se"

# för.efternam
# alexander.häggström

#print(f"{firstName[0:3].lower()}{lastName[0:3].lower()}19")
userName = firstName[0:3].lower()
userName += lastName[0:3].lower()
userName += "19"
print(userName)






print(lastName.capitalize())







tecken = """() parenteser
[] hakparanteser
{} måsvingar
: kolol
; semikolon
, komma
\" dubbelfnutt
\' enkelfnutt"""

print(tecken[13:37])



print(firstName.lower() + "." + lastName.lower() + mail.lower())