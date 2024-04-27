import tkinter as tk
from tkinter import *
from chat import get_response, therapist, generate_response

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def _on_enter_pressed(self, event):
       msg = self.msg_entry.get()
       self._insert_message(msg, "You")
    
   def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{'Omen'}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = tk.Label(self, text="This is page 1")
       #label.pack(side="top", fill="both", expand=True)
       # text widget
       self.text_widget = tk.Text(self, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
       self.text_widget.place(relheight=1, relwidth=1, rely=0.08)
       self.text_widget.configure(cursor="arrow", state=DISABLED)
       # bottom label
       bottom_label = Label(self, bg=BG_GRAY, height=80)
       bottom_label.place(relwidth=1, rely=0.825)
       # message entry box
       self.msg_entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
       self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
       self.msg_entry.focus()
       self.msg_entry.bind("<Return>", self._on_enter_pressed)
       
       # send button
       send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
       send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
       
   
        

        
        
class Page2(Page):
    def _on_enter_pressed(self, event):
       msg = self.msg_entry.get()
       self._insert_message(msg, "You")
    
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{'Omen'}: {therapist(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
    
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = tk.Label(self, text="This is page 2")
       #label.pack(side="top", fill="both", expand=True)
       # text widget
       self.text_widget = tk.Text(self, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
       self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
       self.text_widget.configure(cursor="arrow", state=DISABLED)
       # bottom label
       bottom_label = Label(self, bg=BG_GRAY, height=80)
       bottom_label.place(relwidth=1, rely=0.825)
       # message entry box
       self.msg_entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
       self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
       self.msg_entry.focus()
       self.msg_entry.bind("<Return>", self._on_enter_pressed)
       # send button
       send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
       send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
       
       
       
class Page3(Page):
   def _on_enter_pressed(self, event):
       msg = self.msg_entry.get()
       self._insert_message(msg, "You")
    
   def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{'Omen'}: {generate_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
    
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = tk.Label(self, text="This is page 3")
       #label.pack(side="top", fill="both", expand=True)
        # text widget
       self.text_widget = tk.Text(self, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
       self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
       self.text_widget.configure(cursor="arrow", state=DISABLED)
       # bottom label
       bottom_label = Label(self, bg=BG_GRAY, height=80)
       bottom_label.place(relwidth=1, rely=0.825)
       # message entry box
       self.msg_entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
       self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
       self.msg_entry.focus()
       self.msg_entry.bind("<Return>", self._on_enter_pressed)
       # send button
       send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
       send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
       
       

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)    
        container.pack(side="top", fill="both", expand=True)
        

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        
        # tiny divider
        line = Label(self, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        #chatbot button
        chat_btn = tk.Button(buttonframe, text = 'Chatbot', font=FONT, bg=BG_GRAY, command= p1.show)
        chat_btn.place(x=0, y=0, width=200)
        
        #info button
        info_btn = tk.Button(buttonframe, text = 'Information',font=FONT, bg=BG_GRAY, command=p3.show)
        info_btn.place(x=400, y=0, width=200)
        
        #Therapist button
        ther_btn = tk.Button(buttonframe, text = 'Therapist', font=FONT, bg=BG_GRAY, command = p2.show)
        ther_btn.place(x=200, y=0, width=200)
        
        #exit applicatoin button 
        exit_btn = tk.Button(buttonframe, text = 'Exit', font=FONT, bg=BG_GRAY, command = root.destroy)
        exit_btn.place(x=600, y=0, width=200)
        
        
        
        b1.pack(side = "left")
        
        

        p1.show()
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Omen: Mental Health Assistant")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.mainloop()