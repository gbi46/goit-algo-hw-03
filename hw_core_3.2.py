import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    
    randSet = set()

    while len(randSet) < quantity:
        randSet.add(random.randrange(int(min), int(max) + 1))

    return sorted(randSet)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
