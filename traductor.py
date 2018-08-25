from textblob import TextBlob
import tkinter as tk

root = tk.Tk()
root.title("Gui Translator")
root.geometry("450x500")


# function to translate
def traducir():
    try:
        blob = TextBlob(text1.get("1.0", 'end-1c'))
        text2.config(state="normal")
        text2.insert(tk.INSERT, blob.translate(to=tbox.get()) + "\n")
        text2.config(state="disabled")
    except Exception as err:
        text2.config(state="normal")
        text2.insert(tk.INSERT, "Error {}".format(err))
        text2.config(state="disabled")


# function to clear boxes
def limpiar():
    text1.delete("1.0", 'end-1c')
    tbox.delete(0, 'end')
    text2.config(state="normal")
    text2.delete("1.0", 'end-1c')
    text2.config(state="disabled")


# function to quit
def salir():
    root.destroy()


lb1 = tk.Label(root, text="Insert text to translate")
lb1.pack()
lb2 = tk.Label(root, text="Enter initials in two letters of the language to translate")
lb3 = tk.Label(root, text="\nThe default language is English")

# INPUT TEXTBOX
text1 = tk.Text(root, height=10, width=50, bg='white')

# OUTPUT TEXTBOX
text2 = tk.Text(root, height=10, width=50, bg='white')

# INPUT TEXTBOX LANGUAGE
tbox = tk.Entry(root, width='2', bg='white')

# BUTTONS
mButton = tk.Button(root, text="Translate", command=traducir)
cButton = tk.Button(root, text="Clear", command=limpiar)
qButton = tk.Button(root, text="Quit", command=salir)

# INPUT TEXTBOX 1
text1.pack()

# LABEL LANGUAGE
lb2.pack()

# TEXTBOX LANGUAGE
tbox.pack()

# OUTPUT TEXTBOX
text2.config(state="disabled")
text2.pack()

# LABEL DEFAULT LANGUAGE
lb3.pack(side="bottom")

# BUTTONS
mButton.pack(side="left", ipadx=5, padx=20)
cButton.pack(side="left")
qButton.pack(side="right", padx=20)

# EXECUTER
root.mainloop()
