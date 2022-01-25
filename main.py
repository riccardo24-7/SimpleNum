while True:
    simple_str = "this number isn't simple"
    number_input = int(input("Please enter a number: "))


    list_of_del = [i for i in range(number_input, 1, -1) if number_input % i == 0]
    list_of_del.append(1)
    list_of_del.sort()

    if len(list_of_del) == 2:
        for dels in list_of_del:
            if number_input % dels == 0:
                simple_str = "this number is simple"
                continue
                
    print(simple_str)