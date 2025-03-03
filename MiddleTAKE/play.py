'''
 ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰
███╗   ███╗██╗██████╗ ██████╗ ██╗     ███████╗████████╗ █████╗ ██╗  ██╗███████╗
████╗ ████║██║██╔══██╗██╔══██╗██║     ██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██╔════╝
██╔████╔██║██║██║  ██║██║  ██║██║     █████╗     ██║   ███████║█████╔╝ █████╗  
██║╚██╔╝██║██║██║  ██║██║  ██║██║     ██╔══╝     ██║   ██╔══██║██╔═██╗ ██╔══╝  
██║ ╚═╝ ██║██║██████╔╝██████╔╝███████╗███████╗   ██║   ██║  ██║██║  ██╗███████╗
╚═╝     ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝v2.00
 ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰
        Если не запускается - поменяйте расскладку клавиатуры на Английский ! ! !
        Рекомендуется открыть терминал по-выше
 ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰
        Press F5 to PLAY, *required Python and VS [ в cmd не видны символы ]
 ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰
        game by Куса (k11sann), other games : https://github.com/k11sann/Python-Games/tree/main
''' #https://www.asciiart.eu/text-to-ascii-art font ansi shadow

import time, threading, sys, os

defaultSimbol = "∷ "
lineSimbol =    "█ "
arrowSimbol =   "▼ "
blockSimbol =   "Х "
borderSimbol =  " ◫ "
lineLowSimbol = "━ "
buttonSimbol =  "◈ "
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
        [9, 9, 0.4, #15
         ["skip", 2, 2],
         ["flipX", 3],
         ["speedup", 0.252, 4],
         ["skip", 6, 4],
         ["flipX", 6], 
         ["middle", 2, 6],
        ],
        [9, 7, 0.4, #16
         ["flipX", 1],
         ["skip", 6, 2],
         ["middle", 2, 3],
         ["flipX", 3],
         ["flipX", 4],
         ["skip", 6, 5],
         ["skip", 4, 5],
         ["flipX", 5],
        ],
        [21, 11, 0.4, #17
            ["skip", 1, 2],
            ["skip", 3, 2],
            ["skip", 5, 2],
            ["skip", 7, 2],

            ["flipX", 2],
            ["speedup", 0.375, 2],
            ["skip", 13, 3],
            ["skip", 15, 3],
            ["skip", 17, 3],
            ["skip", 19, 3],

            ["flipX", 3],
            ["skip", 1, 4],
            ["skip", 3, 4],
            ["skip", 5, 4],
            ["skip", 7, 4],

            ["flipX", 4],
            ["speedup", 0.35, 4],
            ["skip", 13, 5],
            ["skip", 15, 5],
            ["skip", 17, 5],
            ["skip", 19, 5],

            ["flipX", 5],
            ["skip", 1, 6],
            ["skip", 3, 6],
            ["skip", 5, 6],
            ["skip", 7, 6],

            ["flipX", 6],
            ["speedup", 0.325, 6],
            ["skip", 13, 7],
            ["skip", 15, 7],
            ["skip", 17, 7],
            ["skip", 19, 7],

            ["flipX", 7],
            ["skip", 1, 8],
            ["skip", 3, 8],
            ["skip", 5, 8],
            ["skip", 7, 8],

            ["flipX", 8],
            ["speedup", 0.3, 8],
            ["skip", 13, 9],
            ["skip", 15, 9],
            ["skip", 17, 9],
            ["skip", 19, 9],

            ["flipX", 9],   
            ["skip", 1, 10],
            ["skip", 3, 10],
            ["skip", 5, 10],
            ["skip", 7, 10],

        ],
        ]

class QuadroGame:
    def __init__(self):
        self.current_lvl = 1 # чит код по факту, писать уровни от 1 до ???
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
        self.maxAttempts = 7
        self.dif = "classic"
        
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
            print("\n◄    ЦЕНТР ВЗЯТ ☻  ")
            print("◄    ПОПЫТКА : "+str(self.attempt))
            print("◣  "+str(" ▰"*int(self.y+1)))
            if self.current_lvl>=len(lvls):
                self.current_lvl=0
            else:
                self.current_lvl+=1
            self.attempt=0
            time.sleep(1.25)
        else:
            self.attempt+=1
            print("◄    ИГРА ПРОИГРАНА ☢ ")
            if self.dif=="attempts":
                secondPrint=""
                if self.attempt>=self.maxAttempts:
                    secondPrint=" [-3]"
                print("◄    ПОПЫТКА : "+str(self.attempt)+"/"+str(self.maxAttempts)+secondPrint)
                if self.attempt>=self.maxAttempts:
                    self.attempt=0
                    self.current_lvl-=3
                    if self.current_lvl<0:
                        self.current_lvl=0
            else:
                print("◄    ПОПЫТКА : "+str(self.attempt))
            print("◣  "+str(" ▰"*int(self.y+1)))
            time.sleep(1.1)
        
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

            if self.flipX==False:
                if self.quads[self.curX][self.curY]!=skipSimbol:
                    self.curY+=1
                else:
                    editX=self.curX+1
                    print(self.flipX)
            else:
                if self.quads[self.curX][self.curY]!=skipSimbol:
                    self.curY+=1
                else:
                    editX=self.curX-1

            if self.quads[x0][y0-1]!=lineLowSimbol and self.quads[x0][y0-1]!=blockSimbol and self.quads[x0][y0-1]!=buttonSimbol and self.quads[x0][y0-1]!=skipSimbol and self.quads[x0][y0]!=skipSimbol:
                self.quads[x0][y0] = lineSimbol
        except IndexError:
            pass
            
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
                        if self.flipX==True:
                            if self.secondary_middles[i][1][0]-self.secondary_middles[i][1][1]>0:
                                self.flipX=False
                        else:
                            if self.secondary_middles[i][1][0]-self.secondary_middles[i][1][1]<0:
                                self.flipX=True
                        self.buttonPress=False
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
                                if self.secondary_middles[i][1][0]-self.secondary_middles[i][1][1]<0:
                                    self.flipX=False
                            else:
                                if self.secondary_middles[i][1][0]-self.secondary_middles[i][1][1]>0:
                                    self.flipX=True
                            for i in range(self.secondary_middles[i][1][1], self.secondary_middles[i][1][0]+1):
                                if self.quads[i][y0]!=blockSimbol and self.quads[i][y0]!=buttonSimbol and self.quads[i][y0]!=lineSimbol:
                                    self.quads[i][y0] = lineLowSimbol
                if nameEvent=="flipx" and self.secondary_middles[i][1]==self.curY and self.quads[self.curX][self.curY]!=skipSimbol:
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
                    if editX>0:
                        self.curX=editX
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
            if self.current_lvl==0:
                fullPrint+="◄    НАЖИМАЙ ENTER  \n"
                fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            if self.current_lvl==3:
                fullPrint+="◄    Сначала закончите первый стобец,\n◄    а затем закончите второй [ "+blockSimbol+" символ законч. столбца ]\n"
                fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            if self.current_lvl==6:
                fullPrint+="◄    Значок ["+speedUpSimbol+" ] меняет вашу текущую скорость, будьте осторожны\n"
                fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            if self.current_lvl==9:
                fullPrint+="◄    Значок ["+reverseSimbol+" ] меняет направление движения\n"
                fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            if self.current_lvl==12:
                fullPrint+="◄    Перед разблокировкой столбца вам нужно нажать [ "+buttonSimbol+" ]\n"
                fullPrint+="◄    Затем крестик [ "+blockSimbol+"] разблокируется\n"
                fullPrint+="◄    ?*? Вариативно изменяется направление движения от текущей позиции\n"
                fullPrint+="i- "+str(" ▰"*int(mainGame.y+1))
            if self.current_lvl==14:
                fullPrint+="◄    Нажимайте перед минами [ "+skipSimbol+" ] клавишу ENTER,\n"
                fullPrint+="◄    Чтобы не взорваться\n"
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

    def setDiff(self, num=1):
        match num:
            case 1:
                self.dif="classic"
            case 2:
                self.dif="attempts"
            case 3: 
                self.dif="timer"

print("◤ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
print("   Правила игры\n")
print(" Используйте ENTER, чтобы поставить стрелочку\nНажимайте клавишу заранее на 1 клетку до центральной линии\nВсего в игре "+str(len(lvls))+" уровней\n")
print("◤ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
print("   РЕЖИМ ИГРЫ \n")
print(" 1. Обычный\n    Ничего трудного, стандартный режим")
print(" 2. Попытки\n    На каждый уровень даётся 7 попыток, когда попыток будет равно 0,\n    то вас перекидывает на 3 уровня назад")
print(" 3. Таймер [ НЕДОСТУПНО ]\n    Нужно пройти игру менее чем за ??? минут")
print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
mainGame = QuadroGame()
while(True):
    choose = input("Введите режим игры : ")
    try:
        if int(choose)<3 and int(choose)>0:
            mainGame.setDiff(int(choose))
            break
        else:
            print("Введено неправильное значение")
    except ValueError:
        print("Введено неправильное значение")
    
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
                #print("flipX "+str(mainGame.flipX))
                #print("cur xe "+str(mainGame.curX))
                    
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
