# ROCK, PAPER AND SCISSORS

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random, os, time, subprocess


options = ["ROCK", "PAPER", "SCISSORS"]

user_score = 0
comp_score = 0

window = Tk()


def exit_game():
    global user_score, comp_score
    if "RPS_USER_SCORE" in dict(os.environ):
        os.environ["RPS_USER_SCORE"] = str(
            int(os.environ["RPS_USER_SCORE"]) + user_score
        )
        os.environ["RPS_COMP_SCORE"] = str(
            int(os.environ["RPS_COMP_SCORE"]) + comp_score
        )
    else:

        os.environ["RPS_USER_SCORE"] = str(user_score)
        os.environ["RPS_COMP_SCORE"] = str(comp_score)

    msg = (
        "RESULTS\nTotal no. of rounds : "
        + str(user_score + comp_score)
        + "\nYour Score : "
        + str(user_score)
        + " rounds "
        + "\nComputer Score : "
        + str(comp_score)
        + " rounds "
    )
    messagebox.showinfo(message=msg, title="SCORE")
    window.destroy()
    subprocess.call(["python", "menu.py"])


def user_selection(option):
    global user_score, comp_score
    comp_choice.set(value=options[random.randint(0, 2)])
    user_choice.set(value=option)

    if comp_choice.get() == "ROCK":
        canvas.itemconfig(comp_image, image=fist)
    elif comp_choice.get() == "PAPER":
        canvas.itemconfig(comp_image, image=palm)
    elif comp_choice.get() == "SCISSORS":
        canvas.itemconfig(comp_image, image=v)
    else:
        canvas.itemconfig(comp_image, image=init)

    if user_choice.get() == "ROCK":
        canvas.itemconfig(user_image, image=fist)
    elif user_choice.get() == "PAPER":
        canvas.itemconfig(user_image, image=palm)
    elif user_choice.get() == "SCISSORS":
        canvas.itemconfig(user_image, image=v)
    else:
        canvas.itemconfig(user_image, image=init)

    print(option, comp_choice.get())

    if option == "ROCK":
        if comp_choice.get() == "PAPER":
            messagebox.showinfo(
                message="The computer chose paper, the computer wins",
                title="The Computer Wins",
            )
            comp_score += 1

        elif comp_choice.get() == "SCISSORS":
            messagebox.showinfo(
                message="The computer chose scissors, You Win", title="You win"
            )
            user_score += 1

        else:
            messagebox.showinfo(
                message="The computer chose rock, its a tie", title="Its a tie"
            )
    elif option == "PAPER":
        if comp_choice.get() == "ROCK":
            messagebox.showinfo(
                message="The computer chose ROCK, You win", title="You Win"
            )
            user_score += 1

        elif comp_choice.get() == "SCISSORS":
            messagebox.showinfo(
                message="The computer chose scissors, the computer wins",
                title="The Computer Wins",
            )
            comp_score += 1

        else:
            messagebox.showinfo(
                message="The computer chose paper, its a tie", title="Its a tie"
            )
    else:
        if comp_choice.get() == "ROCK":
            messagebox.showinfo(
                message="The computer chose ROCK, the computer wins",
                title="The Computer Wins",
            )
            comp_score += 1

        elif comp_choice.get() == "PAPER":
            messagebox.showinfo(
                message="The computer chose PAPER, You Win", title="You win"
            )
            user_score += 1

        else:
            messagebox.showinfo(
                message="The computer chose SCISSORS, its a tie", title="Its a tie"
            )

    """
    comp_image.config(text="COMPUTER'S CHOICE")
    user_image.config(text="USER'S CHOICE")
    """
    time.sleep(1)
    canvas.itemconfig(user_image, image=init)
    canvas.itemconfig(comp_image, image=init)


background_image = ImageTk.PhotoImage(Image.open("./stacked-peaks-haikei.png"))

canvas = Canvas(
    window,
    width=900,
    height=600,
)
canvas.pack()

canvas.create_image(
    0,
    0,
    anchor=NW,
    image=background_image,
)


title_label = canvas.create_text(
    450,
    150,
    text="ROCK, PAPER AND SCISSORS",
    font=("KG Second Chances Sketch", 30),
    fill="white",
)

pvp_label = canvas.create_text(
    450,
    225,
    text="Player vs Computer",
    font=("Pacifico", 20),
    fill="white",
)

user_choice = StringVar()
comp_choice = StringVar()

fist = ImageTk.PhotoImage(Image.open("./fist.png"))
palm = ImageTk.PhotoImage(Image.open("./palm.png"))
v = ImageTk.PhotoImage(Image.open("./v.png"))
init = ImageTk.PhotoImage(Image.open("./init.png"))


comp_image = canvas.create_image(575, 375, image=init)
user_image = canvas.create_image(325, 375, image=init)

comp_text = canvas.create_text(
    575, 450, text="Computer", fill="#fff", font=("Poppins", 12)
)
user_text = canvas.create_text(325, 450, text="User", fill="#fff", font=("Poppins", 12))

exit_image = ImageTk.PhotoImage(Image.open("./exit.png"))
exit_button = canvas.create_image(810, 545, image=exit_image)
canvas.tag_bind(exit_button, "<Button-1>", lambda x: exit_game())


"""
user_image = Label(text=user_choice)
user_image.place(x=575, y=275)
"""


rock = Button(
    window,
    text="ROCK",
    bg="#00CC8E",
    fg="#ffffff",
    activebackground="#00CC8E",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: user_selection("ROCK"),
)
rock.place(x=200, y=525)

paper = Button(
    window,
    text="PAPER",
    bg="#00CC8E",
    fg="#ffffff",
    activebackground="#00CC8E",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: user_selection("PAPER"),
)
paper.place(x=400, y=525)

scissors = Button(
    window,
    text="SCISSORS",
    bg="#00CC8E",
    fg="#ffffff",
    activebackground="#00CC8E",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: user_selection("SCISSORS"),
)
scissors.place(x=600, y=525)


window.config(
    height=600,
    width=900,
)

window.title("ROCK, PAPER AND SCISSORS!")
window.resizable(0, 0)
window.mainloop()
