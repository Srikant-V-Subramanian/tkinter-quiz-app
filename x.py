i = 0


def x():
    global i
    if i <= 1:
        print(i)
        x()

    i += 1


print(i)
