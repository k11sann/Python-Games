import random
# Загадывает число от 1 до 99

minNum = 1
maxNum = 100

class Game:
    def __init__(self):
        self.number = random.randint(minNum, maxNum)
        self.gameCancel = False

    def checkNumber(self, playerNum):
        try:
            playerNum = int(playerNum)
            if playerNum>self.number:
                if playerNum-self.number>int(maxNum*0.1):
                    return "Нужно очень меньше"
                else:
                    return "Нужно меньше"
            elif playerNum<self.number:
                if self.number-playerNum>int(maxNum*0.1):
                    return "Нужно очень больше"
                else:
                    return "Нужно больше"
            elif playerNum==self.number:
                self.gameCancel=True
                return f"ИГРА ОКОНЧЕНА / Число было : {self.number}"
        except ValueError:
            return "Нужно вводить число!!!"

game = Game()
while(game.gameCancel==False):
    inputNumber = input("\nВаше число : ")
    print(f"\n{game.checkNumber(inputNumber)}")
