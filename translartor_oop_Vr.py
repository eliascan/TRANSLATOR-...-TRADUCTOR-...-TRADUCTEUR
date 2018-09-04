from textblob import TextBlob
from Tkinter import *
import ttk

'''
WITH THIS SCRIPT YOU MUST USE PYTHON 2.7 TO RUN IT
'''

class MyTranslator:
    def __init__(self, master):
        self.master = master
        master.title("Translator")
        master.geometry("375x450")
        master.wm_iconbitmap('icon.png')

        # LABELS
        self.lb1 = Label(master, text="Place the text to be translated and posted")
        self.lb2 = Label(master, text="Select the language of your preference")

        # INPUT TEXTBOX
        self.text1 = Text(master, height=10, width=50, bg='#E3E3E3', insertborderwidth=2)

        # OUTPUT TEXTBOX
        self.text2 = Text(master, height=10, width=50, bg='#E3E3E3', insertborderwidth=2)

        # INPUT COMBOBOX LANGUAGE
        vars = ["English", "French", "Spanish", "Germany", "Italy"]
        self.cboxl = ttk.Combobox(master, width=8, values=vars)
        self.cboxl.current(0)

        # BUTTONS
        self.tButton = ttk.Button(master, text="Translate", command=self.traducir)
        self.cButton = ttk.Button(master, text="Clear", command=self.limpiar)
        self.qButton = ttk.Button(master, text="Quit", command=self.salir)

        ############## POSICIONAMIENTO ##################

        # LABEL TITLE
        self.lb1.grid(row=0, columnspan=3)

        # INPUT TEXTBOX 1
        self.text1.grid(row=1, padx=8, columnspan=3)

        # LABEL LANGUAGE
        self.lb2.grid(row=2, columnspan=3)

        # COMBOBOX LANGUAGE
        self.cboxl.grid(row=3, column=0, pady=5, columnspan=3)

        # OUTPUT TEXTBOX
        self.text2.config(state="disabled")
        self.text2.grid(row=4, padx=8, columnspan=3)

        # BUTTONS
        self.tButton.grid(row=5, column=0)
        self.cButton.grid(row=5, column=1)
        self.qButton.grid(row=5, column=2)

    @property
    def idioma(self):
        if self.cboxl.get() == "English":
            return "en"
        elif self.cboxl.get() == "French":
            return "fr"
        elif self.cboxl.get() == "Spanish":
            return "es"
        elif self.cboxl.get() == "Germany":
            return "de"
        elif self.cboxl.get() == "Italy":
            return "it"

    # function to translate
    def traducir(self):
        try:
            blob = TextBlob(self.text1.get("1.0", "end-1c"))
            self.text2.config(state="normal")
            self.text2.insert(INSERT, blob.translate(to=self.idioma) + "\n")
            self.text2.config(state="disabled")
        except Exception as err:
            self.text2.config(state="normal")
            self.text2.insert(INSERT, "Error {}".format(err))
            self.text2.config(state="disabled")

    # function to clear boxes
    def limpiar(self):
        self.text1.delete("1.0", 'end-1c')
        self.text2.config(state="normal")
        self.text2.delete("1.0", 'end-1c')
        self.text2.config(state="disabled")
        self.cboxl.current(0)

    # function to quit
    def salir(self):
        root.destroy()


if __name__ == '__main__':
    root = Tk()
    my_trans = MyTranslator(root)
    root.mainloop()
