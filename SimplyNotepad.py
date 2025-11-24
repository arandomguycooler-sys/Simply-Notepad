import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import os

# --- Configuration
app_name = "SimplyNotepad"
creator = "Vsy"
title = f"{app_name} by {creator}"

# --- Access the Bundled Icon ---
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# --- Functions ---
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as f:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, f.read())
            update_line_numbers()
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as f:
                f.write(text_area.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

def exit_editor():
    root.destroy()

def update_line_numbers(event=None):
    lines = text_area.get(1.0, "end-1c").split("\n")
    line_numbers.config(state="normal")
    line_numbers.delete(1.0, tk.END)
    for i in range(1, len(lines)+1):
        line_numbers.insert(tk.END, f"{i}\n")
    line_numbers.config(state="disabled")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def cut_text():
    text_area.event_generate("<<Cut>>")

def on_scroll(*args):
    text_area.yview(*args)
    line_numbers.yview(*args)

# --- GUI Setup ---
root = tk.Tk()
root.withdraw()

# --- Main Window ---
root.deiconify()
root.title(title)
root.geometry("700x500")
icon_path = os.path.join(base_path, "NotepadPlus.ico")
root.iconbitmap(icon_path)

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Line numbers
line_numbers = tk.Text(root, width=4, padx=3, takefocus=0, border=0,
                       background="lightgray", state="disabled", yscrollcommand=scrollbar.set)
line_numbers.pack(side="left", fill="y")

# Main text area
text_area = tk.Text(root, wrap="word", undo=True, yscrollcommand=scrollbar.set)
text_area.pack(expand=True, fill="both", side="right")
text_area.bind("<KeyRelease>", update_line_numbers)
text_area.bind("<MouseWheel>", lambda e: update_line_numbers())

# Connect scrollbar
scrollbar.config(command=on_scroll)

# --- Menu ---
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")

root.bind("<Control-c>", lambda e: copy_text())
root.bind("<Control-v>", lambda e: paste_text())
root.bind("<Control-x>", lambda e: cut_text())

update_line_numbers()
root.mainloop()
