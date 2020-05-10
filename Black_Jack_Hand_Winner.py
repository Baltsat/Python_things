point = {str(j):j for j in range(0,11)}
point['K'] = point ['J'] = point['Q'] = 10
point['A'] = 11

def score(hand):
    score = 0
    countA = 0
    for card in hand:
        score += point[card]
        if card == 'A':
            countA +=1
    while (score >21) & (countA>0):
        score -= 10
        countA-= 1
    return score



def winner(points):
    max_point = -10
    max_index = -10
    
    for point in points:
        if (point<=21) and (point > max_point):
            max_point = point
            max_index = points.index(point)
    return max_index
        
        
def blackjack_hand_greater(hands):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    
    
    
    scores = []
    for i,hand in enumerate(hands):
        scores.append(score(hand))
        
    print('Winner is hand №{}'.format(winner(scores)+1))


#Example
blackjack_hand_greater([['K'], ['3', '4', 'A']])       
