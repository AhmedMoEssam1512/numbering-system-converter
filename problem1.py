#Ahmed Mohamed Essam Ahmed   20236012
#Sherif Abdulmaged Ahmed 20236051

def DecToBin(number) : # decimal to binary
    number2 = int(number)
    binary= str()
    while(number2 > 0) :
        if((number2) % 2 == 1) : binary = str(1) + binary
        elif((number2) % 2 == 0) : binary = str(0) + binary
        number2 = number2//2
    return binary

def DecToOct(number) : # decimal to octa
    number2 = int(number)
    octa = str()
    while(number2 != 0) :
        octa = str(number2 % 8) + octa
        number2 = number2//8
    return octa

def DecToHex(number) : # decimal to hexadecimal
    number2 = int(number)
    hexa = str()
    while(number2 != 0) :
        rem = number2 % 16
        if(rem > 9) :
            test = 15 - rem 
            char = chr(70 - test)
            hexa = str(char) + hexa
            number2 = number2 // 16
        else :
            hexa = str(rem) + hexa
            number2 = number2 // 16
    return hexa

def BinToDec(number) : # binary to decimal
    dec = 0
    for i in range(len(number)) :
        dec = (2**i) * int(number[len(number) - 1 - i]) + dec
    return dec

def OctToDec(number) : # octa to decimal
    number = int(number)
    dec=0
    i=0
    while number>0:
        r = number%10
        sum = r*(8**i)
        dec = dec + sum
        number = number//10
        i = i + 1
    return dec

def HexToDec(number) : # hexadecimal to decimal
    decimal = 0
    for digit in number:
        if '0' <= digit <= '9':
            decimal = decimal * 16 + int(digit)
        elif 'A' <= digit <= 'F':
            decimal = decimal * 16 + ord(digit) - 55 
    return decimal

def BinToOct(number) : # binary to octa
    num2=BinToDec(number)
    octa=DecToOct(num2)
    return octa
    
def BinToHex(number) : # binary to hexadecimal
    num2=BinToDec(number)
    hexa=DecToHex(num2)
    return hexa

def OctToBin(number) : # octa to binary
    num2=OctToDec(number)
    binary=DecToBin(num2)
    return binary

def OctToHex(number) : # octa to hexadecimal
    num2=OctToDec(number)
    hexa=DecToHex(num2)
    return hexa

def HexToBin(number) : # hexadecimal to binary
    num2=HexToDec(number)
    binary=DecToBin(num2)
    return binary

def HexToOct(number) : # hexadecimal to octa
    num2=HexToDec(number)
    octa=DecToOct(num2)
    return octa

print("Numbering Converter")
while (1):
    # first menue
    print("press A to enter")
    print("press B to exit")
    SE=input()
    if SE == "A":
        print("please enter your number")
        number=input()
        #seconde menue
        print(""" ** Please select the base you want to convert a number from **
    A) Decimal
    B) Binary
    C) Octal
    D) Hexadecimal""")
        op1=input()
        print(""" ** Please select the base you want to convert a number to **
    A) Decimal
    B) Binary
    C) Octal
    D) Hexadecimal""")
        op2=input()
        if op1 == op2:
            print(number)
        else:
            if op1 == "A": # from decimal
                if op2 == "B":
                       print(DecToBin(number))
                elif op2 =="C":
                       print(DecToOct(number))
                elif op2 == "D":
                        print(DecToHex(number))
                else:
                        print("INVALID")
                    
            elif op1 == "B": # from binary
                if op2 == "A":
                        print(BinToDec(number))
                elif op2 =="C":
                        print(BinToOct(number))
                elif op2 == "D":
                        print(BinToHex(number))
                else:
                        print("INVALID")
             
            elif op1 == "C": # from octa              
                if op2 == "A":
                        print(OctToDec(number))
                elif op2 =="B":
                        print(OctToBin(number))
                elif op2 == "D":
                        print(OctToHex(number))
                else:
                        print("INVALID")
            
            elif op1 == "D": # from hexadecimal
                if op2 == "A":
                        print(HexToDec(number))
                elif op2 =="B":
                        print(HexToBin(number))
                elif op2 == "C":
                        print(HexToOct(number))
                else:
                        print("INVALID")
     
    elif SE =="B":
        print("thank you")
        break
    else:
        print("invalid , please try again")
    

