

while True: 
    try:
        exemple0_1 = int(input("Chose a Number, and i will tell you if is odd or not    "))
        break
    except ValueError: 
        print("I can't rate it if it's not a number")

if exemple0_1 % 2 == 0 : 
    print ("Is Even")
else:
    print("Is odd")

exemple0_2 = int(input("Chose"), input("Three"), input("number's"))

media = sum(input) / len(input)
