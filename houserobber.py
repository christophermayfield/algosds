#3 scenarios 
#1 - rob only the first house
#2 - skip the first house, rob the second, repeat
#3 - rob the first house, skip the second, repeat

def rob(houses):
    return max(houses[0], slide(houses[1:]), slide(houses[:-1]))

def slide(houses):
    prev_max = 0
    best_max = 0

    for house in houses:
        total = max(prev_max + house, best_max)
        prev_max = best_max
        best_max = total
        
        
    return best_max

houses = [2,3,5,1,3]

print(f"the most money we can make is {rob(houses)} bandos")