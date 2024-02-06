import random

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
}

for i in range(1, len(d) + 1):
    l = d[i][1]
    correct_answer = d[i][1][d[i][2]]
    print(l)
    random.shuffle(l)
    d[i][1] = l
    print(d[i][1])
    d[i][2] = d[i][1].index(correct_answer)
    print(d[i][1].index(correct_answer))

    print()

print(d)
