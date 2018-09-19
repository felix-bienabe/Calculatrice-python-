#!/usr/bin/env python3
# coding: utf-8

import calculController

# On importe Tkinter


from Tkinter import *


# On crée une fenêtre, racine de notre interface

fenetre = Tk()

fenetre.rowconfigure(0, weight=1)
fenetre.columnconfigure(0, weight=1)

# On crée un label (ligne de texte) souhaitant la bienvenue

# Note : le premier paramètre passé au constructeur de Label est notre

# interface racine

champ_label = Label(fenetre, text="CALCULATRICE")


# On affiche le label dans la fenêtre

champ_label.pack()

var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=40)
ligne_texte.pack()



def printint(text):
    ligne_texte.insert(END, text)   # END : les characteres s'affichent à la fin des autres.  text: variable de la fonction



def operator(op):
        global val 
        global intval    
        global ope      
        ope = op
        val = var_texte.get()                  #variable val = ce qui était écrit dans la fenetre
        intval = int(var_texte.get())          #variable val convertit en int
        var_texte.set("")                      #fenêtre effacée

def operatortwo(op):
        global val3
        global intval3
        global ope      
        ope = op
        val = var_texte.get()                  
        intval = int(var_texte.get()) 
        

def equal():
        global val2
        global intval2
        global intval
        global ope
        val2 = var_texte.get()
        intval2 = int(var_texte.get())
        if ope == "+":
            var_texte.set(intval + intval2)
    
        elif ope == "-":
            var_texte.set(intval - intval2)
            intval = intval - intval2
        

        elif ope == "*":
            var_texte.set(intval * intval2)
            intval = intval * intval2
        
        elif ope == "/":
            var_texte.set(intval / intval2)
            intval = intval / intval2

        elif ope == "²":
            var_texte.set(intval * intval)
            intval = intval * intval
        
    


bouton_1 = Button(fenetre, text="1", command=lambda:printint("1")) # Si on clique sur le button 1, appelle la fonction qui modifie l'Entry(ligne_texte)
bouton_1.pack( side = LEFT )

bouton_2 = Button(fenetre, text="2", command=lambda:printint("2"))
bouton_2.pack( side = LEFT)

bouton_3 = Button(fenetre, text="3", command=lambda:printint("3"))
bouton_3.pack( side = LEFT )

bouton_4 = Button(fenetre, text="4", command=lambda:printint("4"))
bouton_4.pack( side = LEFT )

bouton_5 = Button(fenetre, text="5", command=lambda:printint("5"))
bouton_5.pack( side = LEFT )

bouton_6 = Button(fenetre, text="6", command=lambda:printint("6"))
bouton_6.pack( side = LEFT)

bouton_7 = Button(fenetre, text="7", command=lambda:printint("7"))
bouton_7.pack( side = LEFT )

bouton_8 = Button(fenetre, text="8", command=lambda:printint("8"))
bouton_8.pack( side = LEFT)

bouton_9 = Button(fenetre, text="9", command=lambda:printint("9"))
bouton_9.pack( side = LEFT)

bouton_0 = Button(fenetre, text="0", command=lambda:printint("0"))
bouton_0.pack( side = LEFT)

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side = BOTTOM)

bouton_moins = Button(fenetre, text="=", command=lambda:equal())
bouton_moins.pack(side = BOTTOM)

bouton_division = Button(fenetre, text="/", command=lambda:operator("/"))
bouton_division.pack(side = BOTTOM)

bouton_multiplication = Button(fenetre, text="x", command=lambda:operator("*"))
bouton_multiplication.pack(side = BOTTOM)

bouton_moins = Button(fenetre, text="-", command=lambda:operator("-"))
bouton_moins.pack(side = BOTTOM)

bouton_plus = Button(fenetre, text="+", command=lambda:operator("+"))
bouton_plus.pack( side = BOTTOM)


bouton_plus = Button(fenetre, text="SQR", command=lambda:operatortwo("²"))
bouton_plus.pack( side = BOTTOM)
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre

fenetre.mainloop()