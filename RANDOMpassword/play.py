import random 

class Password():
    def __init__(self, p0, a0):
        self.password = p0
        self.attept = 0
        self.attepts = a0
        self.entered = False

    def checkPass(self):
        if self.attept>=self.attepts:
            print("ВЫ ПРЕВЫСИЛИ ДОПУСТИМОЕ ЧИСЛО ПОПЫТОК! ДО СВИДАНИЯ!")
        else:
            checkPass = input("ВВЕДИТЕ ПАРОЛЬ ДЛЯ ВХОДА В ПРОГРАММУ : ")
            self.attept+=1
            if checkPass==self.password:
                self.entered = True
                print("ДОБРО ПОЖАЛОВАТЬ!")
            elif self.attept<self.attepts:
                print("ПАРОЛЬ НЕВЕРНЫЙ! ИСПОЛЬЗУЙТЕ ЕЩЕ ОДНУ ПОПЫТКУ")

main = Password(str(random.randint(1000, 9999)), 5)
while(main.entered==False):
    if main.attept>=main.attepts:
        print("Ответ: "+str(main.password))
        print("ВЫ ПРЕВЫСИЛИ ДОПУСТИМОЕ ЧИСЛО ПОПЫТОК! ДО СВИДАНИЯ!")
        break
    else:
        main.checkPass()
