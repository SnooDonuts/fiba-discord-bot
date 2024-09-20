
import random

def roulette(bets: list = None, even: bool = False, odd: bool = False, black: bool = False, red: bool = False, low: bool = False, high: bool = False, cum: bool = False, bet: int = 10):
    if False:
        num = random.randint(0, 38)
        payout = 0
        for bet in bets:
            if bet == num:
                payout += 18 * bet 
            else:
                payout -= bet
        return payout
    elif even or odd or low or high or black or red:
        if random.randint(0, 38) > 18:
            return bet
        else:
            return bet * -1
    
def maty(bet: int = 10):
    num = random.randint(1, 100)
    if num == 100:
        return 3 * bet
    elif num >= 90:
        return 2 * bet
    elif num >= 70:
        return 1.5 * bet
    else:
        return bet * -1

def working():
    return randint(0, 1) * 10
