# game by Куса (k11sann), other games : https://github.com/k11sann/Python-Games/tree/main

import time, threading, sys, os

defaultSimbol = "∷ "
lineSimbol =    "█ "
arrowSimbol =   "▼ "
blockSimbol =   "Х "
borderSimbol =  " ◫ "
lineLowSimbol = "━ "
buttonSimbol =  "� "
speedUpSimbol = " ↯ "
reverseSimbol = " ☀ "
skipSimbol = "◐ "

lvls = [[11, 5, 0.5], # 1 - Размер по x [ рекомендуется не чётное ], 2 - размер по y, 3 - таймер обновления
        [9, 9, 0.3], #2
        [7, 11, 0.25], #3
        [9, 6, 0.5, # 4
            ["middle", 7, 3] # Смещение центра, x/y
        ],
        [11, 8, 0.45, #5
            ["middle", 7, 3], 
            ["middle", 3, 5]
        ],
        [9, 11, 0.35, #6
            ["middle", 2, 3], 
            ["middle", 7, 5], 
            ["middle", 5, 7], 
            ["middle", 2,9]
        ],
        [13, 6, 0.55, # 7
            ["middle", 9, 3],
            ["speedup", 0.2, 3], # Смена скорости
        ],
        [7, 8, 0.8, #8
            ["middle", 1, 3],
            ["speedup", 0.5, 4],
            ["middle", 2, 5],
            ["speedup", 0.3, 6]
        ],
        [11, 10, 0.4, # 9
            ["middle", 3, 3],
            ["speedup", 0.25, 3],
            ["middle", 7, 5],
            ["speedup", 0.15, 5],
            ["middle", 3, 7],
            ["speedup", 0.8, 7],
            ["middle", 8, 8],
            ["speedup", 0.25, 8],
        ],
        [9, 13, 0.4,  #10
            ["middle", 2, 3], 
            ["flipX", 3], 
            ["middle", 5, 5],
            ["flipX", 5], 
            ["middle", 2, 7], 
            ["flipX", 7], 
            ["speedup", 0.3, 7],
            ["middle", 5, 9], 
            ["flipX", 9], 
            ["speedup", 0.25, 9],
            ["middle", 2, 11],
            ["flipX", 11] 
        ],
        [9, 9, 0.4,  #11
            ["middle", 8, 1], 
            ["flipX", 3], 
            ["middle", 4, 3],
            ["flipX", 5], 
            ["middle", 2, 5], 
            ["flipX", 7], 
            ["middle", 4, 7]
        ],
        [11,10,0.45, #12
            ["middle", 1, 1],
            ["flipX", 1],
            ["middle", 3, 2],
            ["flipX", 2],
            ["middle", 5, 3],
            ["flipX", 3],
            ["middle", 7, 4],
            ["flipX", 4],
            ["middle", 5, 5],
            ["flipX", 5],
            ["speedup", 0.275, 4],
            ["middle", 7, 6],
            ["flipX", 6],
            ["middle", 5, 7],
            ["flipX", 7],
            ["middle", 3, 8],
            ["flipX", 8],
            ["middle", 1, 9],
            ["flipX", 9],
        ],
        [9, 6, 0.4, #13
            ["button", [6, 2], 3] # x1 кпнока ,x2 центр /y
        ],
        [13, 11, 0.4, #14
            ["button", [2, 8], 3],
            ["middle", 9, 5],
            ["flipX", 4],
            ["middle", 3, 6],
            ["flipX", 5],
            ["speedup", 0.3, 5],
            ["flipX", 6],
            ["button", [5, 9], 8],
        ],
        [9, 11, 0.4, #15
         ["skip", 2, 3],
         ["flipX", 5],
         ["middle", 3, 8],
         ["skip", 6, 7],
        ],
        [9, 7, 0.4, #15.5
         ["flipX", 1],
         ["skip", 6, 2],
        ],
        [20, 11, 0.4, #16
         ["skip", 2, 2],
         ["skip", 5, 2],
         ["skip", 9, 2],
        ],
        [13, 14, 0.4, #17
         ["skip", 1, 2],
         ["skip", 3, 2],
         ["skip", 5, 2],
        ],
        
        ]

class QuadroGame:
    def __init__(self):
        self.current_lvl = 12 # чит код по факту, писать уровни от 1 до ???
        self.current_lvl-=1
        self.x = lvls[self.current_lvl][1]
        self.y = lvls[self.current_lvl][0]
        self.time = lvls[self.current_lvl][2]
        self.quads = [[defaultSimbol]* self.x for i in range(self.y)]
        self.secondary_middles = []
        self.secondary_middles.clear()
        if len(lvls[self.current_lvl])>=3:
            for i in range(3, len(lvls[self.current_lvl])):
                self.secondary_middles.append(lvls[self.current_lvl][i])
            for i in range(0, len(self.secondary_middles)):
                if self.secondary_middles[i][0]=="skip":
                    self.quads[self.secondary_middles[i][1]][self.secondary_middles[i][2]-1] = skipSimbol
                if self.secondary_middles[i][0]=="middle":
                    self.quads[self.secondary_middles[i][1]][self.secondary_middles[i][2]-1] = lineSimbol
                if self.secondary_middles[i][0]=="button":
                    self.quads[self.secondary_middles[i][1][0]][self.secondary_middles[i][2]-1] = blockSimbol
                    self.quads[self.secondary_middles[i][1][1]][self.secondary_middles[i][2]-1] = buttonSimbol
        self.gameEnd = False
        self.curX = 0
        self.curY = 0
        self.curMiddle = 0
        self.check = False
        self.flipX = False
        self.buttonPress = False
        self.game_status = "title"
        self.attempt = 0
        
    def setUp(self):
        self.x = lvls[self.current_lvl][1]
        self.y = lvls[self.current_lvl][0]
        self.time = lvls[self.current_lvl][2]
        self.quads = [[defaultSimbol]* self.x for i in range(self.y)]
        self.secondary_middles.clear()
        if len(lvls[self.current_lvl])>=3:
            for i in range(3, len(lvls[self.current_lvl])):
                self.secondary_middles.append(lvls[self.current_lvl][i])
            for i in range(0, len(self.secondary_middles)):
                if self.secondary_middles[i][0]=="skip":
                    self.quads[self.secondary_middles[i][1]][self.secondary_middles[i][2]-1] = skipSimbol
                if self.secondary_middles[i][0]=="middle":
                    self.quads[self.secondary_middles[i][1]][self.secondary_middles[i][2]-1] = lineSimbol
                if self.secondary_middles[i][0]=="button":
                    self.quads[self.secondary_middles[i][1][0]][self.secondary_middles[i][2]-1] = blockSimbol
                    self.quads[self.secondary_middles[i][1][1]][self.secondary_middles[i][2]-1] = buttonSimbol
        self.gameEnd = False
        self.curX = 0
        self.curY = 0
        self.curMiddle = 0
        self.check = False
        self.flipX = False
        self.game_status = "inGame"
        self.startQuad()
        
    def gameResult(self, result):
        if result==True:
            print("◄\n    ЦЕНТР ВЗЯТ ☻  ")
            print("◄    ПОПЫТКА : "+str(self.attempt))
            print("◣  "+str(" ▰"*int(self.y+1)))
            if self.current_lvl>=len(lvls):
                self.current_lvl=0
            else:
                self.current_lvl+=1
            self.attempt=0
            time.sleep(1)
        else:
            self.attempt+=1
            print("\n◄    ИГРА ПРОИГРАНА ☢ ")
            print("◄    ПОПЫТКА : "+str(self.attempt))
            print("◣  "+str(" ▰"*int(self.y+1)))
            time.sleep(1)
        
    def setQuad(self, x0, y0):
        if self.diedCheck()==True:
            self.game_status="died"    

        changingX=False
        editX = 0
        try:
            if self.flipX==False:
                if self.quads[self.curX-1][self.curY]!=lineSimbol and self.quads[self.curX-1][self.curY]!=blockSimbol and self.quads[self.curX-1][self.curY]!=buttonSimbol and self.quads[self.curX-1][self.curY]!=skipSimbol:
                    self.quads[self.curX-1][self.curY] = defaultSimbol
            else:
                if self.quads[self.curX+1][self.curY]!=lineSimbol and self.quads[self.curX+1][self.curY]!=blockSimbol and self.quads[self.curX+1][self.curY]!=buttonSimbol and self.quads[self.curX+1][self.curY]!=skipSimbol:
                    self.quads[self.curX+1][self.curY] = defaultSimbol
        except ValueError:
            pass
        
        if self.flipX==False:
            if self.quads[self.curX][self.curY]!=skipSimbol:
                self.curY+=1
            else:
                editX=self.curX+1
        else:
            if self.quads[self.curX][self.curY]!=skipSimbol:
                self.curY+=1
            else:
                editX=self.curX-1
                print(editX)

        if self.quads[x0][y0-1]!=lineLowSimbol and self.quads[x0][y0-1]!=blockSimbol and self.quads[x0][y0-1]!=buttonSimbol and self.quads[x0][y0-1]!=skipSimbol and self.quads[x0][y0]!=skipSimbol:
            self.quads[x0][y0] = lineSimbol
            
        try:

            for i in range(0, len(self.secondary_middles)): # event checker
                nameEvent = str(self.secondary_middles[i][0]).lower()
                if nameEvent=="speedup" and self.secondary_middles[i][2]==self.curY:
                    self.time = self.secondary_middles[i][1]
                if nameEvent=="middle" and self.secondary_middles[i][2]==self.curY:
                    self.curMiddle = self.secondary_middles[i][1]
                    self.quads[x0][y0] = blockSimbol
                    if self.secondary_middles[i][1]-x0>0:
                        for i in range(x0+1, self.secondary_middles[i][1]):
                            self.quads[i][y0] = lineLowSimbol
                    elif self.secondary_middles[i][1]-x0<0:
                        for i in range(self.secondary_middles[i][1]+1, x0):
                            self.quads[i][y0] = lineLowSimbol
                if nameEvent=="button" and (self.secondary_middles[i][2]==self.curY or self.secondary_middles[i][2]==self.curY-1):
                    if self.buttonPress==True and self.curMiddle==self.secondary_middles[i][1][1]:
                        changingX=True
                        self.buttonPress=False
                        if self.flipX==True:
                            self.flipX=False
                        else:
                            self.flipX=True

                        self.curMiddle = self.secondary_middles[i][1][0]
                        self.quads[self.curMiddle][self.curY-2] = lineSimbol
                        self.curY-=1
                    elif self.buttonPress==False and self.curMiddle!=self.secondary_middles[i][1][0]:
                        changingX=True
                        self.quads[x0][y0] = blockSimbol
                        self.curMiddle = self.secondary_middles[i][1][1]
                        self.buttonPress=True
                        if self.secondary_middles[i][1][1]-self.secondary_middles[i][1][0]>0:
                            for i in range(self.secondary_middles[i][1][0]+1, self.secondary_middles[i][1][1]):
                                if self.quads[i][y0]!=blockSimbol and self.quads[i][y0]!=buttonSimbol and self.quads[i][y0]!=lineSimbol:
                                    self.quads[i][y0] = lineLowSimbol
                        elif self.secondary_middles[i][1][1]-self.secondary_middles[i][1][0]<0:
                            if self.flipX==True:
                                self.flipX=False
                            else:
                                self.flipX=True
                            for i in range(self.secondary_middles[i][1][1], self.secondary_middles[i][1][0]+1):
                                if self.quads[i][y0]!=blockSimbol and self.quads[i][y0]!=buttonSimbol and self.quads[i][y0]!=lineSimbol:
                                    self.quads[i][y0] = lineLowSimbol
                if nameEvent=="flipx" and self.secondary_middles[i][1]==self.curY:
                    if self.flipX==True:
                        self.flipX=False
                    else:
                        self.flipX=True
        except IndexError:
            self.quads[x0][y0] = lineSimbol

        if changingX==False: # auto x
            if self.flipX==True:
                if self.buttonPress==True:
                    self.curX=x0
                else:
                    self.curX=self.y-1
            else:
                if self.buttonPress==True:
                    self.curX=x0
                else:
                    self.curX=editX
        
    def moveQuad(self):
        if self.curY <= self.x-2 and self.curX!=self.y and self.curX!=-1 and self.game_status!="died":
            try:
                if self.quads[self.curX][self.curY]!=lineSimbol and self.quads[self.curX][self.curY]!=blockSimbol and self.quads[self.curX][self.curY]!=buttonSimbol and self.quads[self.curX][self.curY]!=skipSimbol:
                    self.quads[self.curX][self.curY] = arrowSimbol
            except ValueError:
                pass
            
            try:
                if self.flipX==False:
                    try:
                        if self.quads[self.curX-1][self.curY]!=lineSimbol and self.quads[self.curX-1][self.curY]!=blockSimbol and self.quads[self.curX-1][self.curY]!=buttonSimbol and self.quads[self.curX-1][self.curY]!=skipSimbol:
                            self.quads[self.curX-1][self.curY] = defaultSimbol
                    except IndexError:
                        pass
                else:
                    try:
                        if self.quads[self.curX+1][self.curY]!=lineSimbol and self.quads[self.curX+1][self.curY]!=blockSimbol and self.quads[self.curX+1][self.curY]!=buttonSimbol and self.quads[self.curX+1][self.curY]!=skipSimbol:
                            self.quads[self.curX+1][self.curY] = defaultSimbol
                    except IndexError:
                        pass
            except ValueError:
                pass

            if self.quads[self.curX][self.curY]==skipSimbol:
                self.game_status="died"

            if self.flipX==False: # проверка на реверс
                self.curX+=1
            else:
                self.curX-=1
        
        
    def startQuad(self):
        self.curMiddle = self.getMiddle()
        self.setQuad(self.curMiddle, 0)
        
    def getMiddle(self):
        return self.y//2
        
    def printQuad(self):
        if self.curY<=self.x:
            fullPrint=""
            quadStr=""
            simbolPrint1=borderSimbol
            simbolPrint2=borderSimbol
            fullPrint+="\n"*30
            fullPrint+="У-"+str(self.current_lvl+1)+str(" ▰"*int(self.y+1))
            fullPrint+="\n"
            for i in range(self.x-1):
                for j in range(self.y):
                    quadStr+=self.quads[j][i]

                if simbolPrint1!=borderSimbol or simbolPrint2!=borderSimbol:
                    simbolPrint1=borderSimbol
                    simbolPrint2=borderSimbol

                for k in range(len(self.secondary_middles)): # speedup print
                    eventName = str(self.secondary_middles[k][0]).lower()
                    if eventName=="speedup" and self.secondary_middles[k][2]==i:
                        simbolPrint1=speedUpSimbol
                    if eventName=="flipx" and self.secondary_middles[k][1]==i:
                        simbolPrint2=reverseSimbol    

                if i+1<10:
                    quadStr=("0"+str(i+1)+simbolPrint1+" "+quadStr)+simbolPrint2
                else:
                    quadStr=(str(i+1)+simbolPrint1+" "+quadStr)+simbolPrint2
                fullPrint+=quadStr+"\n"
                quadStr=""
            fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))+"\n"
            fullPrint+="◄    НАЖИМАЙ ENTER  \n"
            if self.current_lvl==3:
                fullPrint+="◄ Сначала закончите первый стобец, а затем закончите второй [ "+blockSimbol+" символ законч. столбца ]\n"
            if self.current_lvl==6:
                fullPrint+="◄ Значок ["+speedUpSimbol+" ] меняет вашу текущую скорость, будьте осторожны\n"
            if self.current_lvl==9:
                fullPrint+="◄ Значок ["+reverseSimbol+" ] меняет направление движения\n"
            if self.current_lvl==12:
                fullPrint+="◄ Перед разблокировкой столбца вам нужно нажать [ "+buttonSimbol+" ]\n"
                fullPrint+="◄ Затем крестик [ "+blockSimbol+"] разблокируется\n"
                fullPrint+="◄ ?*? Вариативно изменяется направление движения от текущей позиции\n"
            fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            sys.stdout.write(fullPrint)
            
    def diedCheck(self, check0=None, die=None):
        if check0==True:
            self.check=check0
        if self.flipX==False:
            if self.curX>self.curMiddle:
                try:
                    if self.quads[self.curX][self.curY]!=skipSimbol:
                        self.secondary_middles = []
                        self.buttonPress=False
                        self.game_status="showHint"
                        return True
                    else:
                        return False
                except IndexError:
                    return True
            elif self.curX<self.curMiddle and self.check==True:
                try:
                    if self.quads[self.curX][self.curY]!=skipSimbol:
                        self.secondary_middles = []
                        self.buttonPress=False
                        #print("THIS DIED")
                        self.game_status="showHint"
                        return True
                    else:
                        return False
                except IndexError:
                    return True
            else:
                return False
        else:
            if self.curX<self.curMiddle:
                if self.quads[self.curX][self.curY]!=skipSimbol:
                    self.secondary_middles = []
                    self.buttonPress=False
                    self.game_status="showHint"
                    return True
                else:
                    return False
            elif self.curX>self.curMiddle and self.check==True:
                if self.quads[self.curX][self.curY]!=skipSimbol:
                    self.secondary_middles = []
                    self.buttonPress=False
                    self.game_status="showHint"
                    return True
                else:
                    return False
            else:
                return False
            
    def showHint(self):
        fullPrint=""
        fullPrint+="У-"+str(self.current_lvl+1)+str(" ▰"*int(self.y+1))
        fullPrint+="\n ПОПЫТКА : "+str(self.attempt)+"\n"
        fullPrint+="У-"+str(self.current_lvl+1)+str(" ▰"*int(self.y+1))
        print(fullPrint)

print(" ▰ ▰ ▰  MiddleTAKE ▰ ▰ ▰\n\nРекомендуется открыть консоль повыше\n")
print("◤ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
print("   Правила игры\n")
print("Используйте ENTER, чтобы поставить стрелочку\nНажимайте клавишу заранее на 1 клетку до центральной линии\nВсего в игре "+str(len(lvls))+" уровней\n")
print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
choose = input("Вы хотите начать играть? [Нажмите ENTER]")

mainGame = QuadroGame()
    
def gameLoop():
    while(True):
        if mainGame.current_lvl>=len(lvls):
            print("\n◄  ИГРА УСПЕШНО ПРОЙДЕНА")
            print("◄    СПАСИБО ЗА ИГРУ !")
            print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
            mainGame.current_lvl=0
            quit()
        mainGame.gameEnd=False
        if mainGame.gameEnd==False:
            mainGame.setUp()
            while(mainGame.gameEnd==False):
                if mainGame.diedCheck()==True or mainGame.game_status=="died": #проигрыш
                    mainGame.gameEnd==True
                    mainGame.gameResult(False)
                    mainGame.game_status=="showHint"
                    #if os.name == 'nt':
                    #    os.system('cls')  # для Windows
                    #else:
                    #    os.system('clear')  # для macOS и Linux
                    break
                
                if mainGame.curY == mainGame.x-1: # победа
                    mainGame.gameEnd==True
                    mainGame.gameResult(True)
                    mainGame.game_status="win"
                    break
                
                time.sleep(mainGame.time)
                if choose!=None:
                    sys.stdout.flush()
                    
                if mainGame.game_status=="inGame":
                    mainGame.check=False
                    mainGame.moveQuad()
                    mainGame.printQuad()
                #print("\ncur Middle "+str(mainGame.curMiddle))
                #print("\ncur xe "+str(mainGame.curX))
                    
def checkEnter():
    while(mainGame.gameEnd==False):
        enterKey = None
        try:
            enterKey = input("")
            if enterKey != None:
                mainGame.diedCheck(True)
                mainGame.setQuad(mainGame.curX, mainGame.curY)
        except ValueError:
            pass
            
gameThread = threading.Thread(target=gameLoop)
checkThread = threading.Thread(target=checkEnter)

gameThread.start()
checkThread.start()

gameThread.join()
checkThread.join()


# СПИСОК ИДЕЙ:
# 1. Блок первых полей чтобы кубик начинал к примеру с 3 клетки
# 2. Движущающий центр
# 3. Мина (почти реализовал)
# 4. Попытки прохождения (от 5 до 10) Если попыток 0, то -5 уровней
