from tkinter import *
from getWordsForTranslation import ReadDocx
import random
from to_save_words import WordsToSave
from PIL import Image, ImageTk


get_words = ReadDocx()

words_dic = get_words.read_words()

eng_w = [k for k,v in words_dic.items()]
en = str()
rus = str()
total_clicked = 0
match_clicked = 0


new_window = Tk()
# new_window.geometry("250x200")
question_font = ("Helvetica",30)
answer_font = ("Helvetica", 23)
score_font= ("Helvetica",15)

def check_result(what_was_clicked):
    global en
    global rus
    global total_clicked
    global match_clicked
    if what_was_clicked in rus or rus in what_was_clicked:
        match_clicked+=1
        score_label.config(text=f"Correct!\nscore {match_clicked}/{total_clicked+1}, {round(match_clicked/(total_clicked+1) * 100, 2)}%")
        startGame()
    else:
        to_save = WordsToSave(f"{en} - {rus}")
        to_save.writeUp()
    total_clicked+=1

def startGame():
    global en
    global rus
    en = random.choice(eng_w)
    rus = words_dic[en]
    main_label.config(text=en)
    list_extra_answers = []
    for i in range(5):
        if i == 0:
            list_extra_answers.append(rus)
        else:
            w = random.choice(eng_w)
            if words_dic[w] not in list_extra_answers:
                list_extra_answers.append(words_dic[w])
            else:
                i-=1
    new_list_extra_ansers = random.sample(list_extra_answers,len(list_extra_answers))

    for idx,a in enumerate(new_list_extra_ansers):
        extra_button[idx].config(text=a,font=answer_font)
        extra_button[idx].config(command=lambda content=a: check_result(content))
        extra_button[idx].grid(row=3+idx,column=1, sticky="nsew")

score_label = Label(text="score", font=score_font, bg="lightblue")
score_label.grid(row=1,column=1, sticky="nsew")

# img=Image.open(".\\images\\card_front.png")
# photo = ImageTk.PhotoImage(img)
main_label = Label(text="", font=question_font, padx=50, pady=20, bg="lightgreen")
main_label.grid(row=2,column=1, sticky="nsew")



extra_button = [Button(text="",command=check_result) for i in range(5)]
startGame()







new_window.mainloop()
