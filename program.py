#start

#vakna upp
vaken = "n"
print("du sover djupt som björnen i ide...")
while vaken == "n":
    vaken = input("vaknar du? [y/n]: ").lower()

#duscha
print("Du masar dig upp och släpar dig till duschen.")
print("någon har lämnat in brödrost i din dusch")
duscha = input("Flyttar du på brödrosten? [y/n]: ").lower()
if duscha == "n":
    print("du får frisk vatten över dig")
    print("du känner en stark stöt genom din kropp")
    print("du dör")
    exit()
elif duscha ==("y"):
    print("Friskt vatten sköljer över dig och börjar äntligen vakna")
else:
    print("DOES NOT CONPUTE")

# årstid
season = False
while season == False:
    season = input("vilken årstid är det? [vår, vinter, sommar, höst]: ").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt och slask, fyfan, jag sjukanmäler mig")
        print("du klär på dig vinterpälsen...")
    elif season == "sommar":
        print("sommar! shorts och flip flops")
    else:
        season = False