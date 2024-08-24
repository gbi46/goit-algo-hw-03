import random

def get_numbers_ticket(min, max, quantity):
    if 1 <= min <= max <= 1000 and (max - min) >= quantity - 1:
        randSet = set()

        while len(randSet) < quantity:
            randSet.add(random.randrange(int(min), int(max) + 1))

        return sorted(randSet)
    else:
        return []
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
