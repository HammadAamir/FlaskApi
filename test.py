from random import randint
def twoDice():
    firstNum = randint(1, 6)
    secondNum = randint(1, 6)
    
    return firstNum + secondNum

def main():
    totalRolls = 1000
    occurences = {}
    
    for i in range(totalRolls):
        result = twoDice()
        if result in occurences:
            occurences[result] += 1 
        else:
            occurences[result] = 1
            
    print("Total".ljust(15) + "Stimulated Percent".ljust(20))
    print("====   ==========")
    for dice in occurences:
        percent = occurences[dice] / totalRolls
        
        print((dice + "").ljust(15) + (percent + "").ljust(20))
        