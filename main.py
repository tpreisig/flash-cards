from tkinter import *
import random
import pandas

data = pandas.read_csv("data/keywords_phonetic_lowercase.csv")
current_one = {}
learn_them = data.to_dict(orient="records")

def next_one():
    global current_one
    current_one = random.choice(learn_them)
    canvas.itemconfig(card_title, text="Phonetic Translation")
    canvas.itemconfig(card_word, text=current_one["Phonetic Translation"])
    canvas.itemconfig(card_background, image=card_front_image)
    print("Know it. No need to flip 😉")

def display_solution():
    print("Flip the card and show the solution.")
    canvas.itemconfig(card_title, text="Word")
    canvas.itemconfig(card_word, text=current_one["Word"])
    canvas.itemconfig(card_background, image=card_back_image)

# window setup
window = Tk()
window.title("Flash Cards")
window.configure(padx=50, pady=50, bg="cyan3")
window.geometry('900x640')


canvas = Canvas(width=800, height=524, bg="cyan3")
card_front_image = PhotoImage(file="assets/card_front.png")
card_back_image = PhotoImage(file="assets/card_back.png")
card_background = canvas.create_image(404, 264, image=card_front_image)
card_title = canvas.create_text(404, 160, text="Start by clicking", font=("Trebuchet", 20, "italic"))
card_word = canvas.create_text(404, 240, text="Check", font=("Trebuchet", 36, "bold"))
canvas.config(bg="cyan3", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="assets/close-circle-fill.png")
button1 = Button(image=cross_image, borderwidth=0, command=display_solution)
button1.grid(row=0, column=0)

check_image = PhotoImage(file="assets/checkbox-circle-fill.png")
button2 = Button(image=check_image, borderwidth=0, command=next_one)
button2.grid(row=0, column=1)


window.mainloop()

print(learn_them)
