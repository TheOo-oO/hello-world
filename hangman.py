import random 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from string import ascii_uppercase
# Creates a playground for Tk
hangman = Tk() 
hangman.title("Yao Shen's Hangman Game ;)")

# Randomises the words
city_list = ['moscow', 'paris', 'sydney', 'london', 'rome', 'toronto', 'seoul', 'dubai',]
word = random.choice(city_list).upper()
print(word)
count_fails = 0 

def display():
# Displays underscores on the screen
    global display 
    display = []
    display.extend(word)
    for i in range(len(display)):
        display[i] = '_'
    Label(hangman, textvariable=label_word, font=("bold", 80)).grid(row=0, column=4, columnspan=5, rowspan=2)
    label_word.set(" ".join(display))
    
def wrong_word():
    global wrong_letter
    wrong_letter = []

def guess(letter):
    global count_fails
    if word.count(letter)>0:
        for i in range(len(word)):
            if word[i] in letter:
                display[i] = letter
                label_word.set(" ".join(display))
                if list(word) == display:
                    print('YOU ARE AMAZING')

    else:
        wrong_letter.extend(letter)
        if count_fails < 11:
            wrong_words.set("  ".join(wrong_letter))

        count_fails += 1
        if count_fails == 1:
            move1()
        elif count_fails == 2:
            move2()
        elif count_fails == 3:
            move3()
        elif count_fails == 4:
            move4()
        elif count_fails == 5:
            move5()
        elif count_fails == 6:
            move6()
        elif count_fails == 7:
            move7()
        elif count_fails == 8:
            move8()
        elif count_fails == 9:
            move9()
        elif count_fails == 10:
            move10()
        elif count_fails == 11:
            move11()
     

def buttons():
    n = 0 
    for letter in ascii_uppercase:
        ttk.Button(
        hangman, 
        text=letter, width=8,
        command=lambda letter=letter: guess(letter)).grid(row=2+n//9, column=n%9)
        n+=1 
    ttk.Button(hangman, text='QUIT', width=8, command=quits).grid(row=4,column=8)

def style():
    global label_word
    global top_bit
    global wrong_words
    global heading 
    wrong_words = StringVar()
    Label(hangman, textvariable=wrong_words, font=('bold', 30), fg='red', 
    highlightthickness=3).grid(row=1,column=4,columnspan=5)
    heading = Canvas(hangman, width=800, height=10,)
    heading.grid(row=0 , column=0, columnspan=10)
    heading.create_text(400,25, text="", font=('bold', 30))
    label_word=StringVar()
    top_bit = Canvas(hangman, width=400, height=400)
    top_bit.grid(row = 0, column=0, columnspan=5, rowspan=2)
    right_bit = Canvas(hangman, width=500, height=50)
    right_bit.grid(row = 0, column=4, columnspan=5)
    # right_bit.create_text(230, 50, text='', font=('bold', 20))
    

def move1():
    top_bit.create_line(25,375,200,375, fill='black', width=7)
def move2():
    top_bit.create_line(50,375,50,30, fill='black', width=7)
def move3():
    top_bit.create_line(47,30,300,30, fill='black', width=7)
def move4():
    top_bit.create_line(50,125,150,30, fill='black', width=7)
def move5():
    top_bit.create_line(300,27,300,80, fill='black', width=7)
def move6():
    top_bit.create_oval(335,80,260,150, outline='black', width=7)
def move7():
    top_bit.create_line(300,150,300,260, fill='black', width=7)
def move8():
    top_bit.create_line(300,200,250,160, fill='black', width=7)
def move9():
    top_bit.create_line(300,200,350,160, fill='black', width=7)
def move10():
    top_bit.create_line(300,260,250,330, fill='black', width=7)
def move11():
    top_bit.create_line(300,260,350,330, fill='black', width=7)
    
def quits():
    hangman.destroy()

def main():
    style()
    wrong_word()
    display()
    buttons()
    hangman.mainloop()

if __name__ == "__main__":
    main()
