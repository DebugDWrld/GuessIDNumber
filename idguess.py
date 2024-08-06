weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
code = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]

def check(input_id):

    sum = 0
   
    for i in range(18):

        cx = input_id[i].upper()

        if cx == 'X' and i == 17:
            n = int(10)

        else:
            n = int(input_id[i])
            
        sum += n * weight[i]

    right_check_code = sum % 11

    return right_check_code == 1

def guess_dates(input_id):

    all_possible_days = []
 
    year = int(input_id[6:10])
    month = int(input_id[10:12])
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ( year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        day[1] = 29

    for j in range(1, int(day[month-1]+1)):

        id = input_id[:12] + str(j).zfill(2) + input_id[14:]

        if check(id):
            all_possible_days.append(id)

    return all_possible_days
    

while True:

    input_id = input("What's your ID number? Replace the unknown parts with '?': ")

    if len(input_id) != 18:

        print("18 characters only!")

        continue

    if len(input_id) == 18:

        #if input_id[-1].upper() == 'X':

        if input_id[12:14] == '??':

            possible_days = guess_dates(input_id.replace('??', '00'))

            if possible_days:
                print("All possible ID numbers are:", possible_days)

            else:
                print("There're not any possible data.")

        else:

            if check(input_id):
                print("The ID number you input is correct.")

            else:
                print("The ID number you input is incorrect.")

        break

    
