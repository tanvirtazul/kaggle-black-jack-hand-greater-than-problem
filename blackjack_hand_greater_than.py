def blackjack_hand_greater_than(hand_1, hand_2):
    size_hand_1 = len(hand_1)
    size_hand_2 = len(hand_2)

    # print(size_hand_1)
    # print(size_hand_2)

    values = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10, 
        'J': 10,
        'Q': 10,
        'K': 10, 
    }

    # print(values['9'])

    sum_hand_1 = 0
    sum_hand_2 = 0

    count_A = 0

    # Hand 1
    for item in hand_1:
        # print(item)
        # print(values[item])
        if item == 'A':
            count_A = count_A + 1
            print(count_A)
        else:
            sum_hand_1 = sum_hand_1 + values[item]
            print(sum_hand_1)

    # Value  of A can be 11 just once at max. Other than that, it has to be counted as 1 to make sure the sum is not >21.
    if count_A > 1: 
        sum_hand_1 = sum_hand_1 + ((count_A-1)*1)
        print(sum_hand_1)
        temp = sum_hand_1 + 11
        if temp <= 21:
            sum_hand_1 = temp
            print(sum_hand_1)
        else:
            sum_hand_1 = sum_hand_1 + 1
            print(sum_hand_1)
    
    elif count_A == 1:
        temp = sum_hand_1 + 11
        if temp <= 21:
            sum_hand_1 = temp
            print(sum_hand_1)
        else:
            sum_hand_1 = sum_hand_1 + 1
            print(sum_hand_1)

    # end of calculation for Hand 1

    
    
    # start of calculation for Hand 2

    count_A = 0
    
    # Hand 2
    for item in hand_2:
        if item == 'A':
            count_A = count_A + 1
        else:
            sum_hand_2 = sum_hand_2 + values[item]

    
    if count_A > 1:
        sum_hand_2 = sum_hand_2 + ((count_A-1)*1)
        temp = sum_hand_2 + 11
        if temp <= 21:
            sum_hand_2 = temp
        else:
            sum_hand_2 = sum_hand_2 + 1

    elif count_A == 1:
        temp = sum_hand_2 + 11
        if temp <= 21:
            sum_hand_2 = temp
        else:
            sum_hand_2 = sum_hand_2 + 1

            
#     print("sum of hand 1 = ",sum_hand_1,"\nsum of hand 2 = ", sum_hand_2)

    if sum_hand_1 > 21 or sum_hand_1 == sum_hand_2:
        return False
    
    if sum_hand_1 > sum_hand_2 or sum_hand_2 > 21:
        return True
    
    if sum_hand_1 < sum_hand_2:
        return False






# print(blackjack_hand_greater_than(['K'], ['3', '4']))


# print(blackjack_hand_greater_than(['K'], ['10']))


# print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))


# print(blackjack_hand_greater_than(['2', 'A', 'A', '6'], ['6', '3']))

print(blackjack_hand_greater_than(['8'], ['2', 'K']))