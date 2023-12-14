from tkinter import *
from tkinter import messagebox


class Dawson:

    def __init__(self, n):
        self.__size = n
        self.__board = self.newBoard()
        self.__whoPlay = 1
        self.__root = Tk()
        self.__root.title("Dawson Chess")
        self.__root.config(background="black")

        self.__canvas = Canvas(self.__root)
        self.__canvas.config(width=n*50+1, height=51, highlightthickness=0, bd=0, bg="black")
        self.__canvas.pack(padx=150, pady=50)
        self.__canvas.bind('<Button-1>', self.gameTurn)
        self.__player = StringVar()
        self.__textPlayer = Label(self.__root, textvariable=self.__player, fg="white", font=("Courier", 15), bg="black")
        self.__textPlayer.pack()
        self.display()

        self.updateLabels()
        self.__root.mainloop()

    def newBoard(self):
        return [0 for _ in range(self.__size)]

    def displayPawn(self, i):
        if self.__board[i] == 1:
            self.__canvas.create_oval(i*50+5, 5, i*50+45, 45, outline="", fill="#ff0000")
        elif self.__board[i] == -1:
            self.__canvas.create_oval(i*50+5, 5, i*50+45, 45, outline="", fill="#ffa500")

    def display(self):
        self.__canvas.delete("all")
        for i in range(0, self.__size):
            self.displayPawn(i)
            self.__canvas.create_rectangle(i*50, 0, i*50+50, 50, outline="white")
        self.__canvas.update()

    def updateLabels(self):
        self.__player.set("Player {}".format(self.__whoPlay))

    def possible(self, i):
        return not 1 > i > self.__size and self.__board[i] == 0

    def put(self, event):
        i = event.x // 50
        if self.possible(i):
            self.__board[i] = 1
            if i > 0:
                self.__board[i - 1] = -1
            if i < self.__size - 1:
                self.__board[i + 1] = -1

    def again(self):
        return 0 in self.__board

    def gameTurn(self, event):
        self.put(event)
        self.__whoPlay = (self.__whoPlay % 2) + 1
        self.updateLabels()
        self.display()
        if not self.again():
            messagebox.showinfo(message="The winner is the player {}".format((self.__whoPlay % 2) + 1))
            restart = messagebox.askquestion(message="Do you want to restart ?", type="yesno")
            if restart == "yes":
                self.__canvas.delete("all")
                self.__board = self.newBoard()
                self.__whoPlay = 1
                self.updateLabels()
                self.display()
            else:
                self.__root.destroy()


dawsonChess = Dawson(12)

