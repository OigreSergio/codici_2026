
def calcolo_media(): 

    person1 = int(input("Chose your favorite number :   "))
    
    person2 = int(input("Chose your favorite number :   "))
    
    person3 = int(input("Chose your favorite number :   "))

    media = sum(person1 , person2 , person3) / len(person1,person3,person2)

    print (media)


calcolo_media()