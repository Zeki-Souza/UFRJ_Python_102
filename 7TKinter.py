# -*- coding: cp1252 -*-
# 26/05/2015
# TKinter
"""
Created on Tue May 26 10:20:32 2015
    Lista de Exercicios:        TKinter
    File:                       Slide TKinter.pdf
    Curso:                      Computacao II (MAB225)
    Proffessor:                 Igor Leao
    Slide:                      Thiago Cruz de Fran�a
@author: Adolfo Emmanuel Correa Lopez
"""

# 1st part
#from Tkinter import *
from tkinter import *

#Pg. 34
### 2nd part
##about_message = "Hola"
####top = Toplevel()
##top = Tk()
##top.title("About this application...")
##
##msg = Message(top, text=about_message)
##msg.pack()
##
##button = Button(top,text="Dismiss",command=top.destroy)
##button.pack()
##
### 3ra part
##mainloop()

# Pg. 35

##class Application(Frame):
##    def __init__(self, master=None):
##        self.master = master
##        Frame.__init__(self, master)
##        self.msg = Label(self, text='Tiago')
##        self.msg.pack()
##        #self.bye = Button(self, text="Bye", command=self.quit)
##        #self.bye = Button(self, text="Bye", command=self.destroy)
##        self.bye = Button(self, text="Bye", command=master.destroy)
##        self.bye.pack()
##        self.pack()
##top = Tk()
##app = Application(top)
##mainloop()

# Pg. 38

###from Tkinter import *
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        lb1 = Label(text="MeuTexto")
##        lb1.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 39
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        var = StringVar()
##        label = Message(textvariable=var, relief=RAISED)
##        var.set("Hey!? How are you doing?")
##        label.pack()
##app = Application()
##mainloop()

# Pg. 40
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        self.btn = Button(self,text="Sair",command=self.quit) # quit � um callback
##        self.btn.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 41
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        entr = Entry()
##        entr.pack()
##        self.pack()
##        
##app = Application()
##mainloop()

# Pg. 42
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        checkb = Checkbutton(text="Me marque")
##        checkb.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 43
# Option Button

#class Application(Frame):
#    def __init__(self, master=None):
#        #Frame.__init__(self, master)
#        R1 = Radiobutton(text="Option 1", value=1)
#        R1.pack()
#        R2 = Radiobutton(text="Option 2", value=2)
#        R2.pack()
#        R3 = Radiobutton(text="Option 3", value=3)
#        R3.pack()
#        #self.pack()
#app = Application()
#mainloop()

# Erro os 2 ultimos botões ficam false
#class Application(Frame):
#    def __init__(self, master=None):
#        #Frame.__init__(self, master)
#        R1 = Radiobutton(text="Option 1", value=True)
#        R1.pack()
#        R2 = Radiobutton(text="Option 2", value=False)
#        R2.pack()
#        R3 = Radiobutton(text="Option 3", value=False)
#        R3.pack()
#        #self.pack()
#app = Application()
#mainloop()

# Pg. 44
# ListBox
#class Application(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self, master)
#        Lb1 = Listbox()
#        Lb1.insert(1, "Python")
#        Lb1.insert(2, "Perl")
#        Lb1.insert(3, "C")
#        Lb1.insert(4, "PHP")
#        Lb1.insert(5, "JSP")
#        Lb1.insert(6, "Ruby")
#        Lb1.pack()
#        self.pack()
#app = Application()
#mainloop()

# Pg. 46
# Colored Buttons
# Usado para agrupar widgets. Após o Frame.__init__(self, master)
#class Application():
#    def __init__(self, master=None):
#        #Frame.__init__(self, master)
#        frame = Frame()
#        frame.pack()
#        bottomframe = Frame()
#        bottomframe.pack(side = BOTTOM)
#        redbutton = Button(frame, text="Red", fg="red", bg="green")
#        redbutton.pack(side = LEFT)
#        greenbutton = Button(frame, text="Brown", fg="brown")
#        greenbutton.pack(side = LEFT)
#        bluebutton = Button(frame, text="Blue", fg="blue")
#        bluebutton.pack(side = LEFT)
#        blackbutton = Button(bottomframe, text="Black", fg="black")
#        blackbutton.pack(side = BOTTOM)
#app = Application()
#mainloop()

# Pg. 47
# Funciona como a tela de um pintor onde � poss�vel desenhar outras formas
# envia uma mensagem para o canvas orientando-o
# a trocar algumas caracter�sticas do objeto texto
# canvas.itemconfig(texto, font=('SansSerif', '36'), fill='red', anchor=NW)
# ...
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        canvas = Canvas(master = None, background='white')
##        #canvas.pack()
##        texto = canvas.create_text(100, 75, text="Alo mundo!")
##        canvas.itemconfig(texto, font=('SansSerif', '36'), fill='red', anchor=NW)
##        canvas.pack()
##        bt = Button(master = None, text = "ola")
##        bt.pack(side=TOP)
##        bt.pack(side=LEFT)
##        bt["text"] = "alterado"
##        #bt.fg = "red"
##        bt["fg"] = "red"
###top = Tk()
###app = Application(top)
##app = Application()
##mainloop()

# Pg. 49
# Um painel de menu. Implementa menus de janela, pulldowns e popups
#class Application(Frame):
#    def __init__(self, master=Tk()):
#        Frame.__init__(self, master)
#        menubar = Menu()
#        filemenu = Menu(menubar, tearoff=0)
#        filemenu.add_command(label="New")
#        filemenu.add_command(label="Open")
#        filemenu.add_command(label="Save")
#        filemenu.add_command(label="Save as...")
#        filemenu.add_command(label="Close")
#        filemenu.add_separator()
#        filemenu.add_command(label="Exit", command=quit)
#        menubar.add_cascade(label="File", menu=filemenu)
#        master.config(menu=menubar)
#        self.pack()
#app = Application()
##mainloop()
#app.mainloop()

# Pg. 50
# Permite especificar um valor atrav�s de um ponteiro em uma escala linear
##def sel():
##    selection = "Value = " + str(var.get())
##    label.config(text = selection)
##root = Tk()
##var = DoubleVar()
##scale = Scale( root, variable = var )
##scale.pack(anchor=CENTER)
##button = Button(root, text="Get Scale Value", command=sel)
##button.pack(anchor=CENTER)
##label = Label(root)
##label.pack()
##root.mainloop()

# Pg. 51
# Rolamento para widgets com superf�cie �til vari�vel (Text, Canvas, Entry, Listbox)
##root = Tk()
##scrollbar = Scrollbar(root)
##scrollbar.pack( side = RIGHT, fill=Y )
##
##mylist = Listbox(root, yscrollcommand = scrollbar.set )
##for line in range(100):
##    mylist.insert(END, "This is line number " + str(line))
##    
##mylist.pack( side = LEFT, fill = BOTH )
##scrollbar.config( command = mylist.yview )
##
##mainloop()

# Pg. 52
# Text:
# Exibe e permite editar texto formatado. Tamb�m suporta imagens e
# janelas embutidas
##root = None
###root = Tk()
##text = Text(root)
##text.insert(INSERT, "Hello.....")
##text.insert(END, "Bye Bye.....")
##text.pack()
##text.tag_add("here", "1.0", "1.4")
##text.tag_add("start", "1.8", "1.13")
##text.tag_config("here", background="yellow", foreground="blue")
##text.tag_config("start", background="black", foreground="green")
##
##mainloop()

# Pg. 53
# Toplevel: Uma janela separada

##root = Tk()
##top1 = Toplevel()
##top2 = Toplevel(bg="black")
##mainloop()

#class Application(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self, master)
#        self.msg = Label(self, text='Tiago')
#        self.msg.pack()
#        self.bye = Button(self, text="Bye", command=self.quit)
#        self.bye.pack()
#        self.pack()
#app = Application()
#app.master.title("Catalogo do Mato")
#app.master.geometry("100x200+900+500")
#mainloop()

# ......................................................................
# 08/06/2015

# Pg. 55

#class Application(Frame):
#    def __init__(self, master = None):
#        
#        Frame.__init__(self, master)
#        self.msg = Label(self, text = 'Tiago')
#        self.msg.pack()
#        self.bye = Button(self, text="Bye", command=self.quit)
#        self.bye.pack()
#        self.pack()
#app = Application()
#app.master.title("Calango do Mato")
#app.master.geometry("100x200+900+500")
#mainloop()
 
# Pg. 59

#top = Frame()
#top.pack()
#rotulo = Label(top, text="R�tulo Exemplo", foreground="blue")
#rotulo.pack()
#rotulo.configure(relief="ridge", font="Arial 24 bold", border=5, background="yellow")
#mainloop() 

# ......................................................................
# 02/06/2015

# .....................................
# Redimensionando
# .....................................

# Pg. 61
##top = Frame(); top.pack()
###top.configure(relief="groove", border=10)#, font="Times 24 bold")
##top["relief"]="groove"
##top["border"]=10
##a = Label (top, text="A"); a.pack (side="left")
##b = Label (top, text="B"); b.pack (side="bottom")
##c = Label (top, text="C"); c.pack (side="right")
##d = Label (top, text="D"); d.pack (side="top")
##for widget in (a,b,c,d):
##    widget.configure(relief="groove", border=10, font="Times 24 bold")
##top.mainloop()


# Pg. 63
##top = Frame(); top.pack()#top.pack(fill="y")
##top.configure(relief="groove", border=10)
##a = Label (top, text="A"); a.pack (side="left", fill="y")
##b = Label (top, text="B"); b.pack (side="bottom", fill="x")
##c = Label (top, text="C"); c.pack (side="right")
##d = Label (top, text="D"); d.pack (side="top")
##for widget in (a,b,c,d):
##    widget.configure(relief="groove", border=10, font="Times 24 bold")
##top.mainloop()

# Pg. 64
# Exerc�cio 1 (executar e maximizar janela)
###from Tkinter import *
##top = Frame()
###top.pack()
###top.pack(fill='both')#, expand=True)
###top.pack(expand=True)
##top.pack(fill='both', expand=True)
##top.configure(relief="groove", border=10)
##a = Label (top, text="A")
##a.pack(side="left",fill="y")
##b = Label (top, text="B")
##b.pack (side="bottom",fill="x")
##c = Label (top, text="C")
##c.pack (side="right")
##d = Label (top, text="D")
##d.pack (side="top")
##
##for widget in (a,b,c,d):
##    widget.configure(relief="groove", border=10, font="Times 24 bold")
##top.mainloop()

# Pg. 65
# Exerc�cio 2 (executar e maximizar janela)
##top = Frame()
##top.pack(fill='both', expand=True)
##a = Label (top, text="A")
##a.pack (side="left",expand=True,fill="y")
##b = Label (top, text="B")
##b.pack (side="bottom",expand=True,fill="both")
##c = Label (top, text="C")
##c.pack (side="right")
##d = Label (top, text="D")
##d.pack (side="top")
##for widget in (a,b,c,d):
##    widget.configure(relief="groove", border=10, font="Times 24 bold")
##top.mainloop()

# Pg. 66
# Usando Frames para Auxiliar Layout
# Exerc�cio 3: executar e ampliar janela
##top = Frame() ; top.pack(fill='both', expand=True)
##f = Frame (top); f.pack (fill='x') # preenche o espa�o em x
##a = Label (f, text="A")
##b = Label (f, text="B")
##c = Label (f, text="C")
##d = Label (top, text="D")
##for w in (a,b,c,d):
##    w.configure(relief="groove", border=10, font="Times 24 bold")
##    w.pack(side="left", expand=True, fill="both")
##top.mainloop()

# ...............................................
# Programacao com Eventos
# ...............................................


# Pg. 69

# Exemplo
# Execute e clique no bot�o

##def inc():
##    n=int(rotulo.configure("text")[4])+1
##    print rotulo.configure("text") # Retorna os datos que o configure coleta do widget
##    rotulo.configure(text=str(n))
##b = Button(text="Incrementa",command=inc)
##b.pack()
##rotulo = Label(text="0")
##rotulo.pack()
##mainloop()

#class ex_pg69(Tk):
#    def inc(self):
#    #def inc():
#        n=int(rotulo.configure("text")[4])+1
#        print rotulo.configure("text") # Retorna os datos que o configure coleta do widget
#        rotulo.configure(text=str(n))
#    b = Button(text="Incrementa",command=inc)
#    b.pack()
#    rotulo = Label(text="0")
#    rotulo.pack()
#    mainloop()
#    
#main_window = Tk()
##win69 = Tk(main_window)
##ex_pag69 = ex_pg69(win69)
#ex_pag69 = ex_pg69(main_window)
#pg69 = Button(main_window, text = "Exemplo pg. 69", command = ex_pag69.inc)
#pg69.pack()
#mainloop()

# Eventos e Bind
# ..............................

# Pg. 71
##def clica (e):
##    txt = "Mouse clicado em\n%d,%d"%(e.x,e.y)
##    r.configure(text=txt)
##r = Label()
##r.pack(expand=True, fill="both")
##r.master.geometry("200x200") # determina o tamanho do label
###r.bind("<Button-1>", clica)  # Chama a um evento nao principal
####r.bind("<Button-2>", clica)
####r.bind("<Button-3>", clica)
###r.bind("<Motion>", clica)
##r.bind("<B1-Motion>", clica)
##mainloop()

# 09/06/2015......................................

# Pg. 75

##def clica (e):
## txt = "Mouse clicado em\n%d,%d"%(e.x,e.y)
## r.configure(text=txt)
## r.focus()
##def tecla(e):
## txt="Keysym=%s\nKeycode=%s\nChar=%s"%(e.keysym,e.keycode,e.char)
## r.configure(text=txt)
##r = Label()
##r.pack(expand=True, fill="both")
##r.master.geometry("200x200")
##r.bind("<Button-1>", clica)
##r.bind("<Key>", tecla)
##mainloop()


# Pg. 78

##def abrir(): print "abrir"
##def salvar(): print "salvar"
##def ajuda(): print "ajuda"
##
##top=Tk()
##principal=Menu(top)
##top.configure(menu=principal)
##
##arquivo=Menu(principal, tearoff = False) # tearoff = False tira trasejado
##arquivo.add_command(label="Abrir",command=abrir)
##arquivo.add_command(label="Salvar",command=salvar)
##
##principal.add_cascade(label="Arquivo",menu=arquivo)
### Tipos de Menu
### popup botao direito
### popdown
### cascade
### Tirar trasejado
###   tearoff=False
##principal.add_command(label="Ajuda",command=ajuda)
##
##mainloop()



# Pg. 80

##def alo():
##    print "Alo!"
##
##root = Tk()
##menu = Menu(root, tearoff=0)
##menu.add_command(label="Alo 1", command=alo)
##menu.add_command(label="Alo 2", command=alo)
##
##def popup(e):
##    menu.post(e.x_root, e.y_root)
##
##frame = Frame(root, width=200, height=200)
##frame.pack()
##frame.bind("<Button-3>", popup)
##mainloop()


# Pg. 83

##root = Tk()
##soma = DoubleVar(root)
##parcela = DoubleVar(root)
##def aritmetica (e):
##    soma.set(soma.get()+parcela.get())
##lsoma = Label(textvar=soma) # Atualiza automaticamente
##eparcela = Entry(textvar=parcela) # Transforma automaticamente double to string
##eparcela.bind("<Return>", aritmetica) # Apertar Enter
##lsoma.pack()
##eparcela.pack()
##mainloop()

#..............................................

# Pg. 89

#root=Tk()
#cor = StringVar(root)
#cor.set("black")
#l = Label(background=cor.get())
#l.pack(fill='both',expand=True)
#
#def pinta():
#    l.configure(background=cor.get())
#    
#for txt,val in (("preto","black"),
#                ("vermelho","red"),
#                ("azul","blue"),
#                ("verde","green")):
#    
#    Radiobutton(text=txt,value=val,variable=cor,command=pinta).pack(anchor=W)
#    
#mainloop()

#..............................................

# Pg. 91

#root=Tk()
#cor = StringVar(root)
#cor.set("black")
#l = Label(background=cor.get())
#l.pack(fill='both',expand=True)
#
#def pinta():
#    l.configure(background=cor.get())
#    
#for txt,val in (("preto","black"),
#                ("vermelho","red"),
#                ("azul","blue"),
#                ("verde","green")):
#    Radiobutton(text=txt,value=val,variable=cor, command=pinta,indicatoron=False).pack(fill='x')
#    
#mainloop()

#..............................................

# Pg. 94


#def insere():
#    e.insert(INSERT,"*")
# 
#def limpa():
##    e.delete(INSERT,END)
#    e.delete(0,END)
#    
#e=Entry(font="Arial 24")
#i=Button(text="Insere*",command=insere)
#l=Button(text="Limpa",command=limpa)
#e.pack()
#
#for w in (i,l):
#    w.pack(side='left')
#    
#mainloop()

#..............................................

# Pg. 96

#lb = Listbox()
#lb.pack(side=LEFT,expand=True,fill="both")
#sb = Scrollbar()
#sb.pack(side=RIGHT,fill="y")
#sb.configure(command=lb.yview)
#lb.configure(yscrollcommand=sb.set)
#
#for i in range(100):
#    lb.insert(END,i)
#mainloop()

#..............................................

# Pg. 98

#c = Canvas()
#c.pack()
#
#o = c.create_oval(1,1,200,100,outline="blue", width=5,fill="red")
#widget = Button(text="Tk Canvas")
#w = c.create_window(10,120,window=widget,anchor=W)
#l = c.create_line(100,0,120,30,50,60,100,120,fill="black",width=2)
#r = c.create_rectangle(40,150,100,200,fill="white")
##img = PhotoImage(file="./NelsonHaha2.gif")
##img = PhotoImage(file="./0398contr2.jpg")
#img = PhotoImage(file="./0398contr2.gif")
##img = PhotoImage(file="C:/Users/adolfo.correa/Documents/GitHub/UFRJ_Computacao_2/0398contr2.jpg")
#i = c.create_image (150,150,image=img,anchor=NW)
#a = c.create_arc (150,90,250,190,start=30,extent=60, 
#                  outline="green",fill="orange")
#t = c.create_text(200,35,text="Texto\nTexto",font="Arial 22")
#mainloop()