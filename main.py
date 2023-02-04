import tkinter as tk




window = tk.Tk()
window.title("Marvel SpiderMan") 
window.geometry("300x300")

marvel="Spiderman's story is a great adventure with multiverses. Which way?"
spid0="It started off with a spider bite, got these crazy skills and had to be super secret. A custome would do"
spid1="Here I am. Wanna see more of my action?...Follow me"
spid2="Into action--see us in action. I was still practising my new skills then it all happened. Villians attacking our city"
danger="Electric danger but I call it fun and fly. Fly and kick. Oh! Save. I fight for the humans I love. "
work="A day at work kicking butt and danger away from my beloved"
someone="That's why we need someone to fly with and fight for in the highs and lows. For love and support"
together="In the end we are better together even when it means saying goodbye"

verse="I share my adventures as spiderman in this verse. Thought it was uni but it's multiverse"
fight="You may think our universe is just cute and games with friends until the bad guys show up. We fight for our friends and homes. We protect our universe from the bad and kick the danger away for good"
here2="In this verse, danger threatens our fun and adventure but our team is strong and ready to win"
some2="Someone must be also beside us in the evening sunsets as we sing the verse and celebrate the day won"
end="but in the end, we are all better together as a big team of friends and family"


def theVerse():
  global words
  canvas.itemconfig(container,image=verim)
  words["text"]=verse
  button.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()
  
  

def theVerse0():
  global words
  canvas.itemconfig(container,image=figm)
  words["text"]=fight
  button3.pack_forget()
  button4.pack_forget()
  button5.pack()
  button6.pack()
  

def theMovie():
  global words
  canvas.itemconfig(container, image=spid0im)
  words["text"]=f"""{spid0}.
  🕸️{spid1}"""
  button.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()

def theMovie3():
  global words
  canvas.itemconfig(container,image=togim)
  words["text"]=together
  button9.pack_forget()
  button10.pack_forget()
  button11.pack()
  button12.pack()

def theMovie2():
  global words
  canvas.itemconfig(container,image=som1m)
  words["text"]=someone
  button7.pack_forget()
  button8.pack_forget()
  button9.pack()
  button10.pack()

def theMovie1():
  global words
  canvas.itemconfig(container,image=elecim)
  words["text"]=danger
  button5.pack_forget()
  button6.pack_forget()
  button7.pack()
  button8.pack()

def theVerse1():
  global words
  canvas.itemconfig(container,image=herim)
  words["text"]=here2
  button5.pack_forget()
  button6.pack_forget()
  button7.pack()
  button8.pack()

def theVerse2():
  global words
  canvas.itemconfig(container,image=som2im)
  words["text"]=some2
  button7.pack_forget()
  button8.pack_forget()
  button9.pack()
  button10.pack()

def theVerse3():
   global words
   canvas.itemconfig(container,image=enim)
   words["text"]=end
   button9.pack_forget()
   button10.pack_forget()
   button11.pack()
   button12.pack()
   

def theMovie0():
  global words
  canvas.itemconfig(container,image=spid2im)
  words["text"]=f"""{spid2}⚡🕷️
  ⚔️{work}"""
  canvas.itemconfig(container,image=workim)

  button3.pack_forget()
  button4.pack_forget()
  button5.pack()
  button6.pack()

def start():
  global words
  canvas.itemconfig(container,image=comim)
  words["text"]=marvel
  button11.pack_forget()
  button12.pack_forget()
  button.pack()
  button2.pack()
  

comim=tk.PhotoImage(file="comic.PNG")
spid0im=tk.PhotoImage(file="Spid0.PNG")
spid1im=tk.PhotoImage(file="Spid1.PNG")
spid2im=tk.PhotoImage(file="Spider2.PNG")
elecim=tk.PhotoImage(file="electric.PNG")
workim=tk.PhotoImage(file="work.PNG")
som1m=tk.PhotoImage(file="someone.PNG")
togim=tk.PhotoImage(file="together.PNG")
verim=tk.PhotoImage(file="verse.PNG")
figm=tk.PhotoImage(file="fightt.PNG")
herim=tk.PhotoImage(file="here2.PNG")
som2im=tk.PhotoImage(file="some2.PNG")
enim=tk.PhotoImage(file="end.PNG")  
  

canvas=tk.Canvas(window, width=320,height=220)
canvas.pack()
container=canvas.create_image(150,150,image=comim)
words=tk.Label(text=marvel)
words.pack()
button=tk.Button(text="Into the Verse",command=theVerse)
button.pack()
button2=tk.Button(text="The Movie",command=theMovie)
button2.pack()
button3=tk.Button(text="Advance to action into the comic verse>>",command=theVerse0)
button4=tk.Button(text="Let's just stick to the electric movie version",command=theMovie0)
button5=tk.Button(text="See the whole Into the Spiderverse comic team in action",command=theVerse1)
button6=tk.Button(text="Thinking the movie seems more dangerous? Let's swing in for more",command=theMovie1)
button7=tk.Button(text="See how it sets after some comical actions ",command=theVerse2)
button8=tk.Button(text="Check out for more of our multiverse family♥️",command=theMovie2)
button9=tk.Button(text="Check how we all beginning another comic verse..at the end",command=theVerse3)
button10=tk.Button(text="The chapters must close for us to explore other multiverses..what next?",command=theMovie3)
button11=tk.Button(text="Until then..let's see how it all started Into the Spiderverse<<>>>",command=start)
button12=tk.Button(text="Or was the beginning better? How did the man get spidey speedy?<<<< ",command=start)

tk.mainloop()