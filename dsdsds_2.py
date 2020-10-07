
import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("horse.mp3")
pygame.mixer.music.play()
pygame.event.wait()

from tkinter import *

root = Tk()
root.title("NCL the RPG")
root.geometry("800x500+300+100")
root.resizable(FALSE,FALSE)
root.iconbitmap("personagem.ico")
root.iconbitmap(default = "personagem.ico")
root["background"] = 'gray'

#funções___________________________________
def cores():
    top_level = Toplevel()
    top_level.title("opções de cores da interface")
    top_level.geometry("200x200+600+100")
    top_level.resizable(FALSE, FALSE)
    top_level["background"] = 'gray'

    def btn_top1():
        root["background"] = 'black'
        list["bg"] = 'white'
        list["fg"] = '#ff7f00'
        label_descrição["bg"] = 'white'
        label_descrição["fg"] = "#ff7f00"
        label_text["bg"] = 'black'
        label_text["fg"] = 'white'
        label_fase["fg"] = 'white'
        label_fase["bg"] = 'black'
        btn_1["bg"] = 'white'
        btn_1["fg"] = 'black'
        label_btnin["fg"] = '#ff7f00'
        label_invisivel["bg"] = 'black'
        label_invisivel_2["bg"] = 'black'
        btn_2["bg"] = 'white'
        btn_2["fg"] = 'black'

    def btn_top2():
        root["background"] = 'white'
        list["bg"] = 'gray'
        list["fg"] = 'yellow'
        label_descrição["bg"] = 'gray'
        label_descrição["fg"] = 'yellow'
        label_btnin["fg"] = 'yellow'
        label_text["bg"] = 'white'
        label_text["fg"] = 'black'
        label_fase["fg"] = 'black'
        label_fase["bg"] = 'white'
        label_text["bd"] = 2
        label_fase["bd"] = 2
        label_text["relief"] = 'solid'
        label_fase["relief"] = 'solid'
        btn_1["bg"] = 'black'
        btn_1["fg"] = 'white'
        btn_2["bg"] = 'black'
        btn_2["fg"] = 'white'
        label_invisivel["bg"] = 'white'
        label_invisivel_2["bg"] = 'white'

    def btn_top3():
        root["background"] = 'gray'
        list["bg"] = 'black'
        list["fg"] = 'yellow'
        label_descrição["bg"] = 'black'
        label_descrição["fg"] = 'yellow'
        label_btnin["fg"] = 'yellow'
        label_text["bg"] = 'black'
        label_text["fg"] = 'white'
        label_fase["fg"] = 'white'
        label_fase["bg"] = 'black'
        btn_1["bg"] = 'gray'
        label_invisivel["bg"] = 'gray'
        label_invisivel_2["bg"] = 'gray'
        btn_2["bg"] = 'gray'
        btn_2["fg"] = 'black'

    button_top_1 = Button(
        top_level,
        text = "opção 1",
        bd = 5,
        relief = "sunken",
        bg = "black",
        fg = "white",
        command = btn_top1
    )

    label_top_invisivel_1 = Label(top_level,bg = "gray")

    button_top_2 = Button(
        top_level,
        text = "opção 2",
        bd = 5,
        relief = "sunken",
        bg = "black",
        fg = "white",
        command = btn_top2
    )

    label_top_invisivel_2 = Label(top_level,bg = "gray")

    button_top_3 = Button(
        top_level,
        text = "opção 3",
        bd = 5,
        relief = "sunken",
        bg = "black",
        fg = "white",
        command = btn_top3,
    )

    #grids_________________________________
    button_top_1.pack()
    label_top_invisivel_1.pack()
    button_top_2.pack()
    label_top_invisivel_2.pack()
    button_top_3.pack()

def mapa():
    top_level = Toplevel(mapamenu)

#menu_____________________________________

meuMenu = Menu(root)
root.config(menu = meuMenu)

filemenu = Menu(meuMenu)
filemenu.add_command(label = "cores", command = cores)
meuMenu.add_cascade(label = "cores", menu = filemenu)

mapamenu = Menu(meuMenu)
mapamenu.add_command(label = 'mapa', command = mapa)
meuMenu.add_cascade(label = "mapa", menu = mapamenu)

#widgets__________________________________

list = Listbox(root, width = 50, height = 17, bg = "black")

nome = ['primeira fase', 'segunda fase']

for nomes in nome:
    list.insert(END, nomes)
    list["fg"] = 'yellow'

texto0 = StringVar()

label_descrição = Label(root,width = 40, height = 17, bg = "black", fg = "yellow")

label_fase = Label(text = "Fases:", width = 42, fg = "white", bg = "black")
label_text = Label(text = "descrição:",width = 42, bg = "black", fg = "white")
label_invisivel_2 = Label(bg = "gray", width = 5)
label_invisivel = Label(bg = "gray", width = 5)

label_btnin = Label(root, text = 'pontos', bg = 'black', width = 12, height = 2, fg = "yellow")

#funções de jogo____________________________

def seleção():
    if (list.get(ACTIVE)) == 'primeira fase':
        label_descrição["text"] = 'primeira fase'
        label_descrição["justify"] = LEFT

btn_1 = Button(
    text = "escolher",
    width = 12,
    height = 2,
    fg ="black",
    bg = "gray",
    bd = 10,
    relief = "sunken",
    command = seleção
)

def seleção2():
    if label_descrição["text"] == 'primeira fase':
        label_btnin["text"] = '1'

btn_2 = Button(
    text = "clicar",
    width = 12,
    height = 2,
    fg = "black",
    bg = "gray",
    bd = 10,
    relief = "sunken",
    command = seleção2
)

#grids______________________________________

list.grid(row = 1, column = 0)
label_fase.grid(row = 0, column = 0)
label_text.grid(row = 0, column = 4)
label_invisivel.grid(row = 0, column = 3)
label_invisivel_2.grid(row = 0, column = 1)
label_descrição.grid(row = 1, column = 4)
btn_1.grid(row = 2, column = 0)
label_btnin.grid(row = 0, column = 2)
btn_2.grid(row = 2, column = 4)

root.mainloop()