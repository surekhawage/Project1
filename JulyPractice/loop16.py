while True:

    print("\nEnter any range from where to where to see their cubes")
    start = int(input("\nstart :"))
    end= int(input("end :"))

    cube = {}
    for i in range(start,end+1):
        x= i*i*i
        cube[x]=i
        i = +1

    for key, value in cube.items():
        print(f"{value} - {key}")
    
    response = str(input("\nWant to do it again type y/n\n").strip().lower())
    
    if response == "n" :
        break
    elif response != "y" :
        print("Please enter y/n only")


