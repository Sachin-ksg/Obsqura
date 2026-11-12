#ATM Pin Verification- provide a valid pin number ,get a pin from user and check validity

atmpin=1234
userpin=""
while (atmpin!=userpin):
    userpin=int(input("Enter correct PIN:"))
    if atmpin!=userpin:
        print("Invalid PIN")
print("You entered correct PIN")
