from tkinter import *
from tkinter import messagebox


class ToadsAndFrogs:

    def __init__(self, n, p):
        self.__size = n
        self.__p = p
        self.__board = self.initBoard()
        self.__whoPlay = 1
        self.__root = Tk()
        self.__root.title("Toads and frogs")
        self.__root.config(background="black")

        self.__canvas = Canvas(self.__root)
        self.__canvas.config(width=n * 50 + 1, height=51, highlightthickness=0, bd=0, bg="black")
        self.__canvas.pack(padx=150, pady=50)
        self.__canvas.bind('<Button-1>', self.gameTurn)
        self.__player = StringVar()
        self.__textPlayer = Label(self.__root, textvariable=self.__player, fg="white", font=("Courier", 15), bg="black")
        self.__textPlayer.pack()
        self.display()

        self.updateLabels()
        self.__root.mainloop()

    def initBoard(self):
        if self.__p >= self.__size // 2:
            self.__p = self.__size // 2 - 1
        return [1] * self.__p + [0] * (self.__size - 2 * self.__p) + [2] * self.__p

    def displayPawn(self, i):
        if self.__board[i] == 2:
            self.__canvas.create_oval(i * 50 + 5, 5, i * 50 + 45, 45, outline="", fill="#ff0000")
        elif self.__board[i] == 1:
            self.__canvas.create_oval(i * 50 + 5, 5, i * 50 + 45, 45, outline="", fill="#0000ff")

    def display(self):
        self.__canvas.delete("all")
        for i in range(0, self.__size):
            self.displayPawn(i)
            self.__canvas.create_rectangle(i * 50, 0, i * 50 + 50, 50, outline="white")
        self.__canvas.update()

    def updateLabels(self):
        self.__player.set("Player {}".format(self.__whoPlay))

    def possible(self, i):
        d = 1 if self.__whoPlay == 1 else -1
        return (0 <= i < self.__size and self.__board[i] == self.__whoPlay) and (
                (self.__size > i + d >= 0 == self.__board[i + d]) or (
                self.__size > i + 2 * d >= 0 == self.__board[i + 2 * d] and self.__board[i + d] == (
                self.__whoPlay % 2) + 1))

    def move(self, event):
        i = event.x // 50
        d = 1 if self.__whoPlay == 1 else -1
        self.__board[i] = 0
        if self.__board[i + d] == 0:
            self.__board[i + d] = self.__whoPlay
        else:
            self.__board[i + 2 * d] = self.__whoPlay

    def again(self):
        for i in range(self.__size):
            if self.possible(i):
                return True
        return False

    def gameTurn(self, event):
        self.move(event)
        self.__whoPlay = (self.__whoPlay % 2) + 1
        self.updateLabels()
        self.display()
        if not self.again():
            messagebox.showinfo(message="The winner is the player {}".format((self.__whoPlay % 2) + 1))
            restart = messagebox.askquestion(message="Do you want to restart ?", type="yesno")
            if restart == "yes":
                self.__canvas.delete("all")
                self.__board = self.initBoard()
                self.__whoPlay = 1
                self.updateLabels()
                self.display()
            else:
                self.__root.destroy()


tnf = ToadsAndFrogs(8, 3)
