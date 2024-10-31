number_range = {
    "0-10" : 0,
    "11-20" : 0,
    "21-30" : 0,
    "31-40" : 0,
    "41-50" : 0
}

#loop for user input

while True:
    user_input = int(input("Give a number ranging from 0-50: "))
    
#add value to variable to count
    if user_input >= 0 and user_input <= 50:
        if 0 <= user_input <= 10:
            number_range["0-10"] += 1
            print("+1 count to 0-10")
        if 11 <= user_input <= 20:
            number_range["11-20"] += 1
            print("+1 count to 11-20")
        if 21 <= user_input <= 30:
            number_range["21-30"] += 1
            print("+1 count to 21-30")
        if 31 <= user_input <= 40:
            number_range["31-40"] += 1
            print("+1 count to 31-40")
        if 41 <= user_input <= 50:
            number_range["41-50"] += 1
            print("+1 count to 41-50")
#break loop if input error
    else:
        print("error")
        break
#print input error and value of valurables