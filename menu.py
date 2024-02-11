# MENU

from tkinter import *
from PIL import ImageTk, Image
import subprocess, os
from tkinter import messagebox

trivia_score = os.environ.get("TRIVIA_USER_SCORE")
trivia_total_questions = os.environ.get("TRIVIA_TOTAL_QUES")
rps_comp_score = os.environ.get("RPS_COMP_SCORE")
rps_user_score = os.environ.get("RPS_USER_SCORE")

k = dict(os.environ)


window = Tk()


def trivia_quiz():
    window.destroy()
    subprocess.call(["python", "main.py"])


def rps():
    window.destroy()
    subprocess.call(["python", "x.py"])


def display_score():
    if "TRIVIA_USER_SCORE" not in k and "RPS_COMP_SCORE" not in k:
        messagebox.showwarning(
            title="PLAY EITHER OF THE TWO GAMES",
            message="Please play either of the two games listed in the menu in order to show the results.",
        )

    elif "TRIVIA_USER_SCORE" not in k:
        msg = (
            "ROCK, PAPER AND SCISSORS!\nUser's Score : "
            + rps_user_score
            + "\nComputer's Score : "
            + rps_comp_score
        )
        messagebox.showinfo(message=msg, title="SCORE (ROCK, PAPER and SCISSORS ONLY)")

    elif "RPS_USER_SCORE" not in k:
        msg = (
            "TRIVIA QUIZ!"
            + "\nSCORE: "
            + str(trivia_score)
            + "\nNO. OF QUESTIONS YOU GOT CORRECT : "
            + str(int(trivia_score) // 5)
            + " out of "
            + str(trivia_total_questions)
            + "\nPERCENTAGE : "
            + str(int(((int(trivia_score) // 5) / int(trivia_total_questions)) * 100))
            + "%"
        )

        messagebox.showinfo(message=msg, title="SCORE (TRIVIA QUIZ! ONLY)")

    else:
        msg = (
            "TRIVIA QUIZ!"
            + "\nSCORE: "
            + str(trivia_score)
            + "\nNO. OF QUESTIONS YOU GOT CORRECT : "
            + str(int(trivia_score) // 5)
            + " out of "
            + str(trivia_total_questions)
            + "\nPERCENTAGE : "
            + str(int(((int(trivia_score) // 5) / int(trivia_total_questions)) * 100))
            + "%"
            + "\n\nROCK, PAPER AND SCISSORS!\nUser's Score : "
            + rps_user_score
            + " rounds "
            + "\nComputer's Score : "
            + rps_comp_score
            + " rounds "
        )

        messagebox.showinfo(message=msg, title="SCORE")


background_image = ImageTk.PhotoImage(Image.open("./layered-waves-haikei.png"))

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

menu_label = canvas.create_text(
    450, 150, text="MENU", font=("KG Second Chances Sketch", 30), fill="white"
)

quiz_game_button = Button(
    window,
    text="Trivia Quiz!",
    bg="#e34c67",
    fg="#ffffff",
    activebackground="#e34c67",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: trivia_quiz(),
)

rps_game_button = Button(
    window,
    text="Rock, Paper and Scissors!",
    bg="#e34c67",
    fg="#ffffff",
    activebackground="#e34c67",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: rps(),
)

score_button = Button(
    window,
    text="Score",
    bg="#e34c67",
    fg="#ffffff",
    activebackground="#e34c67",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: display_score(),
)

quiz_game_button.place(anchor="center", relx=0.5, rely=0.45)

rps_game_button.place(anchor="center", relx=0.5, rely=0.6)

score_button.place(anchor="center", relx=0.5, rely=0.75)

team_members_title_label = canvas.create_text(
    775,
    300,
    text="Team Members",
    font=("Pacifico", 20),
    fill="white",
    justify="center",
)

team_members_text = "1. Madhav R.\n\n2.Srikant Subramanian\n\n3. Vishwaraj P. A. "
team_members_label = canvas.create_text(
    775,
    400,
    text=team_members_text,
    font=("Poppins", 14),
    fill="white",
    justify="center",
)

window.title("MENU")
window.resizable(0, 0)
window.mainloop()
