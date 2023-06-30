from tkinter import *
from getWordsForTranslation import ReadDocx
import random
from to_save_words import WordsToSave
from PIL import Image, ImageTk
import textwrap


get_words = ReadDocx()

words_dic, words_meaning = get_words.read_words()
eng_w = [k for k,v in words_dic.items()]
en_in_eng_v = str()
ru_in_eng_v = str()
mean_in_eng_v = str()


eng_mean = [k for k,v in words_meaning.items()]




total_clicked = 0
match_clicked = 0

rus_dic={ru_meaning: eng_w for eng_w,ru_meaning in words_dic.items()}
ru_w = [k for k,v in rus_dic.items()]
en_in_rus_v = str()
ru_in_rus_v = str()

new_window = Tk()
# new_window.geometry("250x200")
question_font = ("Helvetica",30)
answer_font = ("Helvetica", 23)
score_font= ("Helvetica",15)

def wrap_text(text, width):
    wrapper = textwrap.TextWrapper(width=width)
    wrapped_text = wrapper.fill(text)
    return wrapped_text

def check_result(what_was_clicked):
    rus_list_to_check_whatWasClicked= "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    check_en_or_rus = str()
    global en_in_eng_v
    global ru_in_eng_v
    global en_in_rus_v
    global ru_in_rus_v
    global mean_in_eng_v

    global total_clicked
    global match_clicked
    
    

    if what_was_clicked[0] in rus_list_to_check_whatWasClicked or what_was_clicked[-1] in rus_list_to_check_whatWasClicked:
        check_en_or_rus = ru_in_eng_v
    
    elif en_in_rus_v:
        check_en_or_rus = en_in_rus_v
    else:
        check_en_or_rus = mean_in_eng_v

    if (what_was_clicked in check_en_or_rus):
        match_clicked+=1
        score_label.config(text=f"Correct!\nscore {match_clicked}/{total_clicked+1}, {round(match_clicked/(total_clicked+1) * 100, 2)}%\n")
        startGame()
    else:       
            
        if what_was_clicked[0] in rus_list_to_check_whatWasClicked or what_was_clicked[-1] in rus_list_to_check_whatWasClicked:
            to_save = WordsToSave(f"{en_in_eng_v} - {ru_in_eng_v}")
            
        else:
            to_save = WordsToSave(f"{en_in_rus_v} - {ru_in_rus_v}")
            
        to_save.writeUp()
    total_clicked+=1

def startGame():

    def eng_turn():
        global en_in_eng_v
        global ru_in_eng_v
        global mean_in_eng_v
        en_in_eng_v = random.choice(eng_w)
        en_idx = eng_w.index(en_in_eng_v)
        ru_in_eng_v = words_dic[en_in_eng_v]
        main_label.config(text=f"{en_in_eng_v}")
        original_text_scoreLabel=score_label.cget("text")
        score_label.config(text=f"{original_text_scoreLabel}\n{en_idx}/{len(eng_w)}")
        list_extra_answers = []
        for i in range(5):
            if i == 0:
                list_extra_answers.append(ru_in_eng_v)
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

    def eng_meaning():
        global en_in_eng_v
        # global ru_in_eng_v
        global mean_in_eng_v
        en_in_eng_v = random.choice(eng_w)
        en_idx = eng_w.index(en_in_eng_v)
        mean_in_eng_v = words_meaning[en_in_eng_v]
        if mean_in_eng_v == "":
            eng_turn()
        else:
            main_label.config(text=f"{en_in_eng_v}")
            original_text_scoreLabel=score_label.cget("text")
            score_label.config(text=f"{original_text_scoreLabel}\n{en_idx}/{len(eng_w)}")
            list_extra_answers = []
            for i in range(5):
                if i == 0:
                    list_extra_answers.append(mean_in_eng_v)
                else:
                    w = random.choice(eng_w)
                    if words_meaning[w] not in list_extra_answers:
                        list_extra_answers.append(words_meaning[w])
                    else:
                        i-=1
            new_list_extra_ansers = random.sample(list_extra_answers,len(list_extra_answers))
            for idx,a in enumerate(new_list_extra_ansers):
                extra_button[idx].config(text= wrap_text(a,width=40),font=answer_font)
                extra_button[idx].config(command=lambda content=a: check_result(content))
                extra_button[idx].grid(row=3+idx,column=1, sticky="nsew")

    
    def rus_turn():
        global ru_in_rus_v
        global en_in_rus_v
        ru_in_rus_v = random.choice(ru_w)
        ru_idx = ru_w.index(ru_in_rus_v)
        en_in_rus_v = rus_dic[ru_in_rus_v]
        main_label.config(text=f"{ru_in_rus_v}")
        original_text_scoreLabel=score_label.cget("text")
        score_label.config(text=f"{original_text_scoreLabel}\n{ru_idx}/{len(ru_w)}")
        list_extra_answers = []
        for i in range(5):
            if i == 0:
                list_extra_answers.append(en_in_rus_v)
            else:
                w = random.choice(ru_w)
                if rus_dic[w] not in list_extra_answers:
                    list_extra_answers.append(rus_dic[w])
                else:
                    i-=1
        new_list_extra_ansers = random.sample(list_extra_answers,len(list_extra_answers))

        for idx,a in enumerate(new_list_extra_ansers):
            extra_button[idx].config(text=a,font=answer_font)
            extra_button[idx].config(command=lambda content=a: check_result(content))
            extra_button[idx].grid(row=3+idx,column=1, sticky="nsew")

    # what_to_start = random.choice([eng_turn, rus_turn])
    what_to_start = random.choice([eng_meaning])

    what_to_start()

score_label = Label(text="score", font=score_font, bg="lightblue")
score_label.grid(row=1,column=1, sticky="nsew")


main_label = Label(text="", font=question_font, padx=50, pady=20, bg="lightgreen")
main_label.grid(row=2,column=1, sticky="nsew")




extra_button = [Button(text="",command=check_result) for i in range(5)]
startGame()







new_window.mainloop()
