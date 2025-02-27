import time, threading, os

defaultSimbol = "✆ "
lineSimbol =    "█ "
arrowSimbol =   "▼ "
blockSimbol =   "✖ "
borderSimbol =  " ▞ "
lineLowSimbol = "━ "
buttonSimbol =  "� "
speedUpSimbol = " ➹ "

lvls = [[11, 5, 0.5], # 1 - Размер по x [ рекомендуется не чётное ], 2 - размер по y, 3 - таймер обновления
        [9, 9, 0.3],
        [7, 11, 0.25],
        [9, 6, 0.5, # 2акт
            [7, 3] # Смещение центра, x/y
        ],
        [11, 8, 0.45, 
            [7, 3], 
            [3, 5]
        ],
        [9, 15, 0.35, 
            [3, 3], 
            [7, 5], 
            [5, 8], 
            [2,12]
        ],
        [13, 6, 0.55, # 3акт
            [9, 3, ["speedup", 0.2]], # Смена скорости
        ],
        [7, 8, 0.8,
            [2, 3, ["speedup", 0.5]],
            [4, 5, ["speedup", 0.3]]
        ],
        [11, 10, 0.4,
            [4, 3, ["speedup", 0.25]],
            [5, 5, ["speedup", 0.15]],
            [3, 7, ["speedup", 0.8]],
            [8, 8, ["speedup", 0.25]]
        ],
        [9, 13, 0.4, 
            [2, 3], 
            [5, 5], 
            [2, 7], 
            [5,9], 
            [2,11]
        ]
        ]

class QuadroGame:
    def __init__(self):
        self.current_lvl = 10 # чит код по факту, писать уровни от 1 до ???
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
                self.quads[self.secondary_middles[i][0]][self.secondary_middles[i][1]-1] = lineSimbol
        self.gameEnd = False
        self.curX = 0
        self.curY = 0
        self.curMiddle = 0
        self.curNumMiddle = 0
        self.check = False
        self.died = False
        
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
                self.quads[self.secondary_middles[i][0]][self.secondary_middles[i][1]-1] = lineSimbol
        self.gameEnd = False
        self.curX = 0
        self.curY = 0
        self.curMiddle = 0
        self.curNumMiddle = 0
        self.check = False
        self.died = False
        self.startQuad()
        
    def gameResult(self, result):
        if result==True:
            print("◄  ЦЕНТР ВЗЯТ ☻  ")
            print("◣  "+str(" ▰"*int(mainGame.y+1)))
            if self.current_lvl>=len(lvls):
                self.current_lvl=0
            else:
                self.current_lvl+=1
            time.sleep(1)
        else:
            print("◄  ИГРА ПРОИГРАНА ☢ ")
            print("◣  "+str(" ▰"*int(mainGame.y+1)))
            time.sleep(1)
        
    def setQuad(self, x0, y0):
        if (self.diedCheck()==True):
            self.died=True    
        try:
            if self.quads[self.curX-1][self.curY]!=lineSimbol and self.quads[self.curX-1][self.curY]!=blockSimbol:
                self.quads[self.curX-1][self.curY] = defaultSimbol
        except ValueError:
            pass
        
        self.curX=0
        self.curY+=1
        try:
            if self.curNumMiddle <= len(self.secondary_middles) and self.curY == self.secondary_middles[self.curNumMiddle][1]:
                if self.secondary_middles[self.curNumMiddle][0]-x0>0:
                    for i in range(x0, self.secondary_middles[self.curNumMiddle][0]):
                        self.quads[i][y0] = lineLowSimbol
                elif self.secondary_middles[self.curNumMiddle][0]-x0<0:
                    for i in range(self.secondary_middles[self.curNumMiddle][0]+1, x0):
                        self.quads[i][y0] = lineLowSimbol

                for i in range(2, len(self.secondary_middles[self.curNumMiddle])): # speedup
                    if self.secondary_middles[self.curNumMiddle][i][0].lower()=="speedup" and self.secondary_middles[self.curNumMiddle][1]==self.curY:
                        self.time = self.secondary_middles[self.curNumMiddle][i][1]

                self.curMiddle=self.secondary_middles[self.curNumMiddle][0]
                self.curNumMiddle+=1
                self.quads[x0][y0] = blockSimbol
            else:
                self.quads[x0][y0] = lineSimbol
        except IndexError:
            self.quads[x0][y0] = lineSimbol
        
    def moveQuad(self):
        if self.curY <= self.x-2:
            try:
                if self.quads[self.curX][self.curY]!=lineSimbol and self.quads[self.curX][self.curY]!=lineSimbol:
                    self.quads[self.curX][self.curY] = arrowSimbol
            except ValueError:
                pass
            
            try:
                if self.quads[self.curX-1][self.curY]!=lineSimbol and self.quads[self.curX-1][self.curY]!=blockSimbol:
                    self.quads[self.curX-1][self.curY] = defaultSimbol
            except ValueError:
                pass
            self.curX+=1
        
        
    def startQuad(self):
        self.curMiddle = self.y//2
        self.setQuad(self.curMiddle, 0)
        
    def printQuad(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.curY<=self.x:
            fullPrint=""
            quadStr=""
            simbolPrint=borderSimbol
            fullPrint+="\n\n"
            fullPrint+="У-"+str(self.current_lvl+1)+str(" ▰"*int(self.y+1))
            fullPrint+="\n"
            for i in range(self.x-1):
                for j in range(self.y):
                    quadStr+=self.quads[j][i]

                if simbolPrint!=borderSimbol:
                    simbolPrint=borderSimbol

                for k in range(len(self.secondary_middles)): # speedup print
                    for l in range(2,len(self.secondary_middles[k])):
                        if self.secondary_middles[k][l][0]=="speedup" and self.secondary_middles[k][1]==i:
                            simbolPrint=speedUpSimbol

                if i+1<10:
                    quadStr=("0"+str(i+1)+simbolPrint+quadStr)
                else:
                    quadStr=(str(i+1)+simbolPrint+quadStr)
                fullPrint+=quadStr+"\n"
                quadStr=""
            fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))+"\n"
            fullPrint+="◄  НАЖИМАЙ ENTER  \n"
            if self.current_lvl==4:
                fullPrint+="◄ Сначала закончите первый стобец, а затем закончите второй [ "+blockSimbol+" символ законч. столбца ]\n"
            if self.current_lvl==8:
                fullPrint+="◄ Значок ["+speedUpSimbol+" ] меняет вашу текущую скорость, будьте осторожны\n"
            fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            print(fullPrint)
            
    def diedCheck(self, check0=None):
        if check0==True:
            self.check=check0
        
        if self.curX>self.curMiddle:
            self.curNumMiddle=0
            self.secondary_middles = []
            return True
        elif self.curX<self.curMiddle and self.check==True:
            self.curNumMiddle=0
            self.secondary_middles = []
            return True
        else:
            return False

print(" ▰ ▰ ▰  MiddleTAKE ▰ ▰ ▰\n\nРекомендуется открыть консоль повыше\n")
choose = input("Хотите ли вы узнать правила игры? [Y/N] \nВаш Ответ: ")

if str(choose).lower()=="y":
    print("◤ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
    print("   Правила игры\n")
    print("Используйте ENTER, чтобы поставить стрелочку\nНажимайте клавишу заранее на 1 клетку до центральной линии\nВсего в игре "+str(len(lvls))+" уровней\n")
    print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
    choose = input("Вы хотите начать играть? [Нажмите ENTER]")

mainGame = QuadroGame()
    
def gameLoop():
    while(True):
        if mainGame.current_lvl>=len(lvls):
            print("◄  ИГРА УСПЕШНО ПРОЙДЕНА")
            print("◄    СПАСИБО ЗА ИГРУ !")
            print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
            mainGame.current_lvl=0
            quit()
        mainGame.gameEnd=False
        if mainGame.gameEnd==False:
            mainGame.setUp()
            while(mainGame.gameEnd==False):
                if mainGame.diedCheck()==True or mainGame.died==True: #проигрыш
                    mainGame.gameEnd==True
                    mainGame.gameResult(False)
                    break
                
                if mainGame.curY == mainGame.x-1: # победа
                    mainGame.gameEnd==True
                    mainGame.gameResult(True)
                    break
                
                time.sleep(mainGame.time)
                mainGame.check=False
                mainGame.moveQuad()
                mainGame.printQuad()
                #print("curY = "+str(mainGame.curY)+"; Y = "+str(mainGame.x-1)+"; NEW MIDDLE = "+str(mainGame.curMiddle))
                    
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
