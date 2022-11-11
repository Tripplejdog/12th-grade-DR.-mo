def  LeafFall(p):
    print("your leaves are falling!")
    num = 0
    while num <= p:
        print(num, "leaves fell!")
        num += 10
        
shakes = int(input("enter the number of times you shake the tree? "))
LeafFall(shakes)