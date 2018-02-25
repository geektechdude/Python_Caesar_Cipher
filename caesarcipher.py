#Caesar Cipher
#GeekTechStuff

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypt=input("Do you want to encrypt a message? (Y/N):")
encrypt=encrypt.upper()

if encrypt == "Y":
    stringtoencrypt=input("Please enter A-Z characters to encrypt:")
    stringtoencrypt=stringtoencrypt.upper()
    ciphershift=input("Please enter a number between 1 and 25 to be your cipher key: ")
    ciphershift=int(ciphershift)
    stringencrypted=""
    for character in stringtoencrypt:
        position = letters.find(character)
        newposition = position+ciphershift
        if character in letters:
            stringencrypted = stringencrypted + letters[newposition]
        else:
            stringencrypted = stringencrypted + character
            
    ciphershift=str(ciphershift)
    print("You used a cipher shift of "+ciphershift)
    print("Your encrypted message reads:")
    print(stringencrypted)
    
    
if encrypt == "N":
    stringtodecrypt=input("Please enter A-Z characters to dencrypt:")
    stringtodecrypt=stringtodecrypt.upper()
    ciphershift=input("Please enter a number between 1 and 25 to be your cipher key: ")
    ciphershift=int(ciphershift)
    stringdecrypted=""
    for character in stringtodecrypt:
        position = letters.find(character)
        newposition = position-ciphershift
        if character in letters:
            stringdecrypted = stringdecrypted + letters[newposition]
        else:
            stringdecrypted = stringdecrypted + character
            
    ciphershift=str(ciphershift)
    print("You used a cipher shift of "+ciphershift)
    print("Your decrypted message reads:")
    print(stringdecrypted)
    
    
else:
    print("Ending Caesar Cipher")
