from tkinter import *
from getWordsForTranslation import ReadDocx
import random


get_words = ReadDocx()
words_dic = get_words.read_words()
eng_w = [k for k,v in words_dic.items()]
en = str()
rus = str()


new_window = Tk()
# new_window.geometry("250x200")
question_font = ("Helvetica",30)
answer_font = ("Helvetica", 23)

def check_result(what_was_clicked):
    global en
    global rus
    if what_was_clicked in rus or rus in what_was_clicked:
        print(f"Correct '{en}' is '{what_was_clicked}'")
        click_the_button()

def click_the_button():
    global en
    global rus
    en = random.choice(eng_w)
    rus = words_dic[en]
    main_word_button.config(text=en)
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
        extra_button[idx].grid(row=2+idx,column=1, sticky="nsew")

main_word_button = Button(text="START", width=10, font=question_font,command=click_the_button)
main_word_button.grid(row=1,column=1, sticky="nsew")

extra_button = [Button(text="",command=check_result) for i in range(5)]







new_window.mainloop()
