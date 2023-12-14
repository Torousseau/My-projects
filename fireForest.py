
import random
import copy
from tkinter import *


class Tree:

    def __init__(self, status: int = 0):
        self._status = status

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

    def getIcon(self):
        if self._status == 0:
            return '.'
        elif self._status == 1:
            return 'A'
        elif self._status == 2:
            return 'F'
        elif self._status == 3:
            return 'C'

    def getColor(self):
        if self._status == 0:
            return '#ffffff'
        elif self._status == 1:
            return '#008000'
        elif self._status == 2:
            return '#e60012'
        elif self._status == 3:
            return '#8a8a8a'

    def updateStatus(self, burn):
        if burn and self._status == 1:
            self._status = 2
        elif self._status == 2:
            self._status = 3


def stop():
    return False


class Forest(Tree):

    def __init__(self, nbLines, nbColumns, proba):
        super().__init__()
        self.__x = nbLines // 2
        self.__y = nbColumns // 2
        self._nbLines = nbLines
        self._nbColumns = nbColumns
        self._grid = [
            [Tree(1) if proba >= round(random.random(), 2) else Tree(0) for _ in range(self._nbColumns)] for _
            in range(self._nbLines)]
        self.__run = False
        self.__gen = 0
        self.__root = Tk()
        self.__root.title("Forest Fires")

        self.__frame1 = Frame(self.__root)
        self.__frame1.grid(row=0, column=0, rowspan=3)
        self.__frame1.config(height=self._nbLines * 20, width=self._nbColumns * 20, relief=RIDGE)
        self.__canvas = Canvas(self.__frame1)
        self.__canvas.config(width=nbColumns * 10 + 1, height=nbLines * 10 + 1, highlightthickness=0, bd=0, bg="white")
        self.__canvas.place(x=50, y=50)
        self.__canvas.bind('<Button-1>', self.pop)
        self.displayFrame()
        self.__canvas.pack(padx=50, pady=50)

        self.__frame2 = Frame(self.__root)
        self.__frame2.grid(row=0, column=1)
        self.__buttonRandomFire = Button(self.__frame2, text='Random Fire', command=self.startFire)
        self.__buttonRandomFire.pack()
        self.__key = IntVar()
        self.__buttonPutFire = Checkbutton(self.__frame2, text='Put Fire', variable=self.__key)
        self.__buttonPutFire.pack()

        self.__frame3 = Frame(self.__root)
        self.__frame3.grid(row=1, column=1)
        self.__buttonStart = Button(self.__frame3, text='Start', command=self.start)
        self.__buttonStart.pack()
        self.__buttonStop = Button(self.__frame3, text='Stop', command=self.stop)
        self.__buttonStop.pack()
        self.__buttonNext = Button(self.__frame3, text='Next', command=self.updateStep)
        self.__buttonNext.pack()

        self.__frame4 = Frame(self.__root)
        self.__frame4.grid(row=2, column=1)
        self.__generation = StringVar()
        self.__textGeneration = Label(self.__frame4, textvariable=self.__generation)
        self.__textGeneration.pack(padx=10)
        self.__proportion = StringVar()
        self.__textProportion = Label(self.__frame4, textvariable=self.__proportion)
        self.__textProportion.pack(padx=10)

        self.updateLabels()
        self.__root.mainloop()

    def updateStep(self):
        self.spread()
        self.__gen += 1
        self.updateLabels()
        self.displayFrame()

    def stop(self):
        self.__run = False

    def start(self):
        self.__run = True
        while self.__run:
            self.updateStep()

    def updateLabels(self):
        self.__proportion.set("Proportion of trees : {} %".format(self.proportion()))
        self.__generation.set("Generation : {}".format(self.__gen))

    def pop(self, event):
        self.__x = event.x
        self.__y = event.y
        if self._grid[self.__x // 10][self.__y // 10].getStatus() == 1 and self.__key.get() == 1:
            self._grid[self.__x // 10][self.__y // 10].setStatus(2)
        self.displayFrame()

    def startFire(self):
        wrong = True
        while wrong:
            random_i = random.randint(0, self._nbLines - 1)
            random_j = random.randint(0, self._nbColumns - 1)
            if self._grid[random_i][random_j].getStatus() == 1:
                self._grid[random_i][random_j].setStatus(2)
                wrong = False
        self.displayFrame()

    def getGrid(self):
        return self._grid

    def displayGrid(self):
        for i in range(self._nbLines):
            for j in range(self._nbColumns):
                print(self._grid[i][j].getIcon(), end="  ")
            print("\n", end="")
        print("\n", end="")

    def displayFrame(self):
        self.__canvas.delete("all")
        for i in range(0, self._nbLines):
            for j in range(0, self._nbColumns):
                color = self._grid[i][j].getColor()
                self.__canvas.create_rectangle(i * 10, j * 10, i * 10 + 10, j * 10 + 10, fill=color)
        self.__canvas.update()

    def isBurned(self, x, y):
        positions = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        for (k, l) in positions:
            if (k >= 0) and (k < self._nbLines) and (l >= 0) and (l < self._nbColumns) and (
                    self._grid[k][l].getStatus() == 2):
                return True
        return False

    def spread(self):
        tempo = copy.deepcopy(self._grid)
        for i in range(0, len(tempo)):
            for j in range(0, len(tempo[i])):
                tempo[i][j].updateStatus(self.isBurned(i, j))
        self._grid = copy.deepcopy(tempo)

    def proportion(self):
        sain = 0
        for i in range(self._nbLines):
            for j in range(self._nbColumns):
                if self._grid[i][j].getStatus() == 1:
                    sain += 1
        return round((sain / (self._nbLines * self._nbColumns)) * 100, 2)

    def fireForest(self, x):
        for i in range(x):
            print("Génération", i + 1, ":")
            self.displayGrid()
            print("Proportion of trees : {} %".format(self.proportion()))
            print()
            self.spread()


forest = Forest(50, 50, 0.7)
