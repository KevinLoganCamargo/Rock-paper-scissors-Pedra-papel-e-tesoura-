from tkinter import *
import random
import win32gui,win32con
import tkinter.messagebox as mbox

try:
    ocultar_janela=win32gui.GetForegroundWindow()
    win32gui.ShowWindow(ocultar_janela,win32con.SW_HIDE)
except:
    pass

class Pygame:
    def __init__(self,op):
        #Imagens of the game
        self.img=PhotoImage(file='imagens\paper.png')
        self.img2=PhotoImage(file='imagens\ock.png')
        self.img3=PhotoImage(file='imagens\scissor.png')
        self.img4=PhotoImage(file='imagens/ninjinha.png')
        self.img5=PhotoImage(file='imagens/robozinho.png')

        self.fr=Frame(op,bg='#222222')
        self.fr.pack()

        self.fr2=Frame(op,bg='#222222')
        self.fr2.pack()

        self.fr3=Frame(op,bg='#222222')
        self.fr3.pack()

        self.fr4=Frame(op,bg='#222222')
        self.fr4.pack()

        self.fr5=Frame(op,bg='#222222')
        self.fr5.pack()

        self.botao_restart = Button(self.fr, text="Restart", font=('Century',10), relief=RAISED, command=self.finish)
        self.botao_restart.pack(side=RIGHT)

        self.lb=Label(self.fr,text='Pedra,Papel e Tesoura',width=20,height=5,background='#222222',foreground='blue',font=('Century',20,'bold'))
        self.lb.pack()

        self.lb_result = Label(self.fr, text='', fg='yellow', bg='#222222', font=('Century', 18))
        self.lb_result.pack(side=BOTTOM)

        self.pontos=0
        self.pontos2=0
        self.lb2=Label(self.fr2,text='Jogador         '+str(self.pontos)+'    X   '+str(self.pontos2)+'        Computador',fg='#1E90FF',bg='#222222',font=('Century',15))
        self.lb2.pack()

        self.lb_img=Label(self.fr3,image=self.img4,bg='#222222')
        self.lb_img.pack(side=LEFT)

        self.lb_space=Label(self.fr3,text='                                                 ',bg='#222222')
        self.lb_space.pack(side=LEFT)

        self.lb_img2=Label(self.fr3,image=self.img5,bg='#222222')
        self.lb_img2.pack(side=LEFT)

        self.choice=StringVar()
        self.rb_pedra=Radiobutton(self.fr4,text='Pedra',value='pedra',variable=self.choice,font=('Century',15),bg='#222222',fg='orange',pady=10)
        self.rb_pedra.pack(side=LEFT)

        self.rb_papel=Radiobutton(self.fr4,text='Papel',value='papel',variable=self.choice,font=('Century',15),bg='#222222',fg='orange',pady=10)
        self.rb_papel.pack(side=LEFT)

        self.rb_tesoura=Radiobutton(self.fr4,text='Tesoura',value='tesoura',variable=self.choice,font=('Century',15),bg='#222222',foreground='orange',pady=10)
        self.rb_tesoura.pack(side=LEFT)

        self.bt_play=Button(self.fr5,text='Jogar',font=('Century',25),bg='#555555',relief=GROOVE,border=8,command=self.play)
        self.bt_play.focus_force()
        self.bt_play.pack()

    def play(self):
         dic = {0:'pedra',1:'papel',2:'tesoura'}
         choice=self.choice.get()
         robot_choice = random.choice(dic)

         if choice=='tesoura':
                self.lb_img['image']=self.img3
         elif choice=='pedra':
                self.lb_img['image']=self.img2
         elif choice=='papel':
                self.lb_img['image']=self.img

         if robot_choice=='pedra':
                self.lb_img2['image']=self.img2
         elif robot_choice=='papel':
                self.lb_img2['image']=self.img
         elif robot_choice=='tesoura':
                self.lb_img2['image']=self.img3

         if choice=='pedra' and robot_choice=='pedra':
            self.lb_result['text']='Empate'
         elif choice=='papel' and robot_choice=='papel':
            self.lb_result['text']='Empate'
         elif choice=='tesoura' and robot_choice=='tesoura':
            self.lb_result['text']='Empate'
         elif choice=='pedra' and robot_choice=='tesoura':
            self.lb_result['text']='O Jogador venceu!'
            self.pontos+=1
            self.lb2['text'] ='Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'
         elif choice=='papel' and robot_choice=='pedra':
            self.lb_result['text']='O Jogador venceu!'
            self.pontos +=1
            self.lb2['text'] ='Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'
         elif choice=='tesoura' and robot_choice=='papel':
            self.lb_result['text']='O Jogador venceu!'
            self.pontos +=1
            self.lb2['text'] ='Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'
         elif choice=='pedra' and robot_choice=='papel':
            self.lb_result['text']='O Computador venceu!'
            self.pontos2 +=1
            self.lb2['text'] ='Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'
         elif choice=='papel' and robot_choice=='tesoura':
            self.lb_result['text']='O Computador venceu!'
            self.pontos2 +=1
            self.lb2['text'] = 'Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'
         elif choice=='tesoura' and robot_choice=='pedra':
            self.lb_result['text']='O Computador venceu!'
            self.pontos2 +=1
            self.lb2['text']= 'Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'

    def finish(self):
        resposta = mbox.askquestion("RESTART", "DESEJA REINICIAR?")
        if resposta == "yes":
            self.lb_result["text"] = ""
            self.lb_img["image"] = self.img4
            self.lb_img2["image"] = self.img5
            self.pontos = 0
            self.pontos2 = 0
            self.lb2['text'] = 'Jogador         ' + str(self.pontos) + '    X   ' + str(self.pontos2) + '        Computador'

op=Tk()
op.title('Pygame 1.0')
op.geometry('600x550+550+5')
op.iconbitmap('imagens\python.ico')
op['bg']='#222222'
op['relief']=RAISED
op['border']=5
game=Pygame(op)
op.mainloop()
