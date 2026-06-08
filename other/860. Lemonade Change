class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0 
        tens = 0
        twenties = 0

        for bill in bills:

            if bill == 5:
                fives += 1
            
            elif bill == 10:
                if fives == 0:
                    return False
                tens += 1
                fives -= 1
            
            else:
                if fives > 0 and tens > 0:
                    fives -= 1
                    tens -= 1
                    twenties += 1

                elif fives >= 3:
                    fives -= 3
                    twenties += 1
                
                else:
                    return False
        
        return True
