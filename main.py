# TRIVIA QUIZ


import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess, os

d = {
    1: [
        "What is the capital city of Canada?",
        ["Ottawa", "Toronto", "Montreal", "Vancouver"],
        0,
    ],
    2: [
        "Who wrote 'To Kill a Mockingbird'?",
        ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"],
        0,
    ],
    3: ["What is the chemical symbol for oxygen?", ["O", "H", "O2", "C"], 0],
    4: [
        "Which country is known as the Land of the Rising Sun?",
        ["Japan", "China", "South Korea", "Thailand"],
        0,
    ],
    5: [
        "Who painted the ceiling of the Sistine Chapel?",
        ["Michelangelo", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"],
        0,
    ],
    6: [
        "What is the currency of the United Kingdom?",
        ["British Pound", "Euro", "US Dollar", "Yen"],
        0,
    ],
    7: [
        "Who was the first man to walk on the moon?",
        ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
        0,
    ],
    8: [
        "What is the largest ocean on Earth?",
        ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        0,
    ],
    9: [
        "Who is known as the father of modern physics?",
        ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        0,
    ],
    10: ["What is the chemical symbol for sodium?", ["Na", "S", "So", "N"], 0],
    11: [
        "What is the tallest animal in the world?",
        ["Giraffe", "Elephant", "Kangaroo", "Rhino"],
        0,
    ],
    12: [
        "Who wrote 'The Great Gatsby'?",
        ["F. Scott Fitzgerald", "Jane Austen", "Charles Dickens", "George Orwell"],
        0,
    ],
    13: [
        "What is the main ingredient in guacamole?",
        ["Avocado", "Tomato", "Onion", "Lime"],
        0,
    ],
    14: [
        "What is the primary ingredient in hummus?",
        ["Chickpeas", "Lentils", "Black Beans", "Kidney Beans"],
        0,
    ],
    15: [
        "What is the largest continent by land area?",
        ["Asia", "Africa", "North America", "Europe"],
        0,
    ],
    16: ["What is the chemical symbol for iron?", ["Fe", "Ir", "In", "I"], 0],
    17: [
        "Who painted the famous 'Mona Lisa'?",
        ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
        0,
    ],
    18: ["What is the chemical symbol for gold?", ["Au", "Ag", "Hg", "Pt"], 0],
    19: [
        "What is the smallest planet in our solar system?",
        ["Mercury", "Venus", "Earth", "Mars"],
        0,
    ],
    20: [
        "Who discovered penicillin?",
        ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Robert Koch"],
        0,
    ],
    21: [
        "What is the main ingredient in sushi?",
        ["Rice", "Noodles", "Seaweed", "Fish"],
        0,
    ],
    22: [
        "Who was the first female Prime Minister of the United Kingdom?",
        ["Margaret Thatcher", "Theresa May", "Angela Merkel", "Indira Gandhi"],
        0,
    ],
    23: ["What is the chemical symbol for carbon?", ["C", "Ca", "Co", "Cu"], 0],
    24: [
        "Which planet is known as the Red Planet?",
        ["Mars", "Jupiter", "Venus", "Saturn"],
        0,
    ],
    25: [
        "Who is the author of 'The Catcher in the Rye'?",
        ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain"],
        0,
    ],
    26: [
        "What is the process by which plants make their own food called?",
        ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
        0,
    ],
    27: [
        "Which element has the atomic number 1?",
        ["Hydrogen", "Oxygen", "Nitrogen", "Carbon"],
        0,
    ],
    28: [
        "What is the highest mountain in Africa?",
        ["Mount Kilimanjaro", "Mount Everest", "Mount McKinley", "Mount Elbrus"],
        0,
    ],
    29: [
        "Who is known as the 'Father of Medicine'?",
        ["Hippocrates", "Aristotle", "Socrates", "Plato"],
        0,
    ],
    30: ["What is the chemical symbol for silver?", ["Ag", "Si", "Au", "Hg"], 0],
    31: [
        "Which country is known as the 'Land of the Rising Sun'?",
        ["Japan", "China", "South Korea", "Thailand"],
        0,
    ],
    32: [
        "Who was the first woman to win a Nobel Prize?",
        ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Jane Goodall"],
        0,
    ],
    33: [
        "What is the capital city of Australia?",
        ["Canberra", "Sydney", "Melbourne", "Brisbane"],
        0,
    ],
    34: [
        "Who wrote the novel '1984'?",
        ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Jules Verne"],
        0,
    ],
    35: ["What is the chemical symbol for lead?", ["Pb", "Ld", "Pl", "Le"], 0],
    36: [
        "What is the largest moon of Jupiter?",
        ["Ganymede", "Europa", "Callisto", "Io"],
        0,
    ],
    37: [
        "Who is known as the 'Father of Geometry'?",
        ["Euclid", "Pythagoras", "Archimedes", "Aristotle"],
        0,
    ],
    38: ["What is the chemical symbol for potassium?", ["K", "P", "Po", "Ko"], 0],
    39: ["Who wrote 'The Odyssey'?", ["Homer", "Plato", "Socrates", "Aristotle"], 0],
    40: [
        "What is the largest organ in the human body?",
        ["Skin", "Liver", "Heart", "Brain"],
        0,
    ],
    41: ["What is the chemical symbol for calcium?", ["Ca", "Cl", "C", "Ce"], 0],
    42: [
        "Who is the current President of the United States?",
        ["Joe Biden", "Donald Trump", "Barack Obama", "George W. Bush"],
        0,
    ],
    43: [
        "What is the second most abundant element in the Earth's crust?",
        ["Silicon", "Oxygen", "Aluminum", "Iron"],
        0,
    ],
    44: ["What is the chemical symbol for helium?", ["He", "H", "Ho", "Hu"], 0],
    45: [
        "Who wrote the play 'Hamlet'?",
        ["William Shakespeare", "Christopher Marlowe", "Ben Jonson", "John Milton"],
        0,
    ],
    46: ["What is the chemical symbol for nitrogen?", ["N", "Ni", "Na", "Ne"], 0],
    47: [
        "Who discovered the theory of relativity?",
        ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Galileo Galilei"],
        0,
    ],
    48: ["What is the chemical symbol for phosphorus?", ["P", "Po", "Ph", "Pl"], 0],
    49: [
        "Who painted 'Starry Night'?",
        ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"],
        0,
    ],
    50: ["What is the chemical symbol for copper?", ["Cu", "C", "Co", "Ca"], 0],
}


for i in range(1, len(d) + 1):
    l = d[i][1]
    correct_answer = d[i][1][d[i][2]]
    random.shuffle(l)
    d[i][1] = l
    d[i][2] = d[i][1].index(correct_answer)


"""



count = 1

score = 0

print()

while count <= n:
    x = random.randint(1, 50)

    if x not in d:
        continue

    print(f"Q{count} : {d[x][0]}")
    print(f"A. {d[x][1][0]}\t B. {d[x][1][1]}\t C. {d[x][1][2]}\t D. {d[x][1][3]}")
    selection = ord(input("\nEnter the Option : ").upper()) - 65

    if selection == d[x][2]:
        score += 5

    count += 1
    print()
    del d[x]

print()
print("YOUR SCORE : ", score)
print("TOTAL NO. OF QUESTIONS YOU HAVE GOT CORRECT : ", score // 5, "out of", n)
print("PERCENTAGE : ", int(((score // 5) / n) * 100), "%")

"""

n = int(input("\nEnter the number of question you'd want to attend : "))

if n > 50:
    print("Enter a number less than 50.")
    n = int(input("\nEnter the number of question you'd want to attend : "))

print()

count = 1
score = 0


def change_question():
    global question_no_label, question_text, question_no_text, question_label, options, selected_option, count, x
    question_no_text = str(count) + " out of " + str(n)

    x = random.randint(1, 50)

    while x not in d:
        x = random.randint(1, 50)

    question_text = d[x][0]
    options = d[x][1]

    canvas.itemconfig(question_no_label, text=question_no_text)
    canvas.itemconfig(question_label, text=question_text)
    option1.config(text=options[0])
    option2.config(text=options[1])
    option3.config(text=options[2])
    option4.config(text=options[3])

    count += 1


def select_option(option):
    global score, x, count
    selected_option.set(value=option)
    if d[x][1][d[x][2]] == selected_option.get():
        score += 5
        print("You got it correct.")
        msg = messagebox.showinfo(
            message="You got it correct!", title="You got it correct!"
        )
    else:
        k = "You got it wrong!\nThe Correct answer was " + d[x][1][d[x][2]]
        msg = messagebox.showerror(message=k, title="You got it wrong!")
        print("You got it wrong.")

    print("You selected : ", selected_option.get())
    print("Correct Option : ", d[x][1][d[x][2]])
    print("Current Score : ", score)
    print()

    del d[x]

    if count > n:
        message = (
            "THE TEST IS OVER"
            + "\nSCORE: "
            + str(score)
            + "\nNO. OF QUESTIONS YOU GOT CORRECT : "
            + str(score // 5)
            + " out of "
            + str(n)
            + "\nPERCENTAGE : "
            + str(int(((score // 5) / n) * 100))
            + "%"
        )
        x = messagebox.showinfo(message=message, title="TEST RESULTS")

        if "TRIVIA_USER_SCORE" in dict(os.environ):
            os.environ["TRIVIA_USER_SCORE"] = str(
                int(os.environ["TRIVIA_USER_SCORE"]) + score
            )
            os.environ["TRIVIA_TOTAL_QUES"] = str(
                int(os.environ["TRIVIA_TOTAL_QUES"]) + n
            )
        else:
            os.environ["TRIVIA_USER_SCORE"] = str(score)
            os.environ["TRIVIA_TOTAL_QUES"] = str(n)

        window.destroy()
        subprocess.call(["python", "menu.py"])
    else:
        change_question()


window = Tk()


background_image = ImageTk.PhotoImage(Image.open("./wave-haikei.png"))

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

question_no_text = str(21) + " out of " + str(25)
question_no_label = canvas.create_text(
    450, 150, text=question_no_text, font=("KG Second Chances Sketch", 30), fill="white"
)

question_text = "Which one of the following is the capital of India?"
question_label = canvas.create_text(
    450, 225, text=question_text, font=("Pacifico", 20), fill="white"
)

options = ["Chennai", "Mumbai", "Kolkata", "Delhi"]
selected_option = StringVar()


option1 = Button(
    window,
    text=options[0],
    bg="#0066FF",
    fg="#ffffff",
    activebackground="#0066FF",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: select_option(options[0]),
)
option1.place(anchor="center", relx=0.5, rely=0.5)

option2 = Button(
    window,
    text=options[1],
    bg="#0066FF",
    fg="#ffffff",
    activebackground="#0066FF",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    justify="center",
    command=lambda: select_option(options[1]),
)
option2.place(anchor="center", relx=0.5, rely=0.6)

option3 = Button(
    window,
    text=options[2],
    bg="#0066FF",
    fg="#ffffff",
    activebackground="#0066FF",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    justify="center",
    command=lambda: select_option(options[2]),
)
option3.place(anchor="center", relx=0.5, rely=0.7)

option4 = Button(
    window,
    text=options[3],
    bg="#0066FF",
    fg="#ffffff",
    activebackground="#0066FF",
    activeforeground="#ffffff",
    font=("Poppins", 16),
    anchor="se",
    command=lambda: select_option(options[3]),
)
option4.place(anchor="center", relx=0.5, rely=0.8)

change_question()


arr = [option1, option2, option3, option4]


window.config(
    height=600,
    width=900,
)


window.title("TRIVIA QUIZ!")
window.resizable(0, 0)
window.mainloop()
