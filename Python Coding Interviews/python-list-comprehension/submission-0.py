from typing import List


def create_list_of_odds(n: int) -> List[int]:
    
    if n == 1:
        return [1]
    
    odds = []
    for i in range(1, n+1):

        if i%2 != 0:
            odds.append(i)
    
    return odds



# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
