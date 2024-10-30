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
#break loop if input error
    else:
        print("error")
        break
#print input error and value of valurables