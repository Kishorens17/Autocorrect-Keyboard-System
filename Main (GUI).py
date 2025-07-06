import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker

def autocorrect_text(input_text):
    spell = SpellChecker()
    
    words = input_text.split()
    lowercase_words = [word.lower() for word in words]
    misspelled = spell.unknown(lowercase_words)

    corrections = {}
    for word in misspelled:
        suggestions = spell.candidates(word)
        best_guess = spell.correction(word)
        corrections[word] = {
            'suggestions': suggestions,
            'best_guess': best_guess
        }

    corrected_text = []
    for word in words:
        word_lower = word.lower()
        if word_lower in corrections:
            corrected_word = corrections[word_lower]['best_guess']
            corrected_text.append(corrected_word)
        else:
            corrected_text.append(word)

    count = 0
    correction_log = ""
    for word, data in corrections.items():
        correction_log += f"Total corrections available: {len(data['suggestions'])}\n"
        correction_log += f"Misspelled: {word}\n"
        correction_log += f"Suggestions: {data['suggestions']}\n"
        correction_log += f"Autocorrected to: {data['best_guess']}\n\n"
        count += 1

    return ' '.join(corrected_text), count, correction_log

# GUI Function
def on_autocorrect():
    input_text = input_field.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Required", "Please enter some text.")
        return

    corrected, total, log = autocorrect_text(input_text)
    
    output_field.config(state='normal')
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, corrected)
    output_field.config(state='disabled')

    suggestion_field.config(state='normal')
    suggestion_field.delete("1.0", tk.END)
    suggestion_field.insert(tk.END, f"Total words corrected: {total}\n\n{log}")
    suggestion_field.config(state='disabled')

root = tk.Tk()
root.title("Sentence Autocorrect System")
root.geometry("700x600")

tk.Label(root, text="Enter your sentence:", font=("Arial", 12, "bold")).pack(pady=5)
input_field = tk.Text(root, height=4, width=80, font=("Arial", 11))
input_field.pack(pady=5)

tk.Button(root, text="Autocorrect", command=on_autocorrect, font=("Arial", 12), bg="#84baf8").pack(pady=10)

tk.Label(root, text="Corrected Sentence:", font=("Arial", 12, "bold")).pack()
output_field = tk.Text(root, height=3, width=80, font=("Arial", 11), state='disabled', bg="#98f89c")
output_field.pack(pady=5)

tk.Label(root, text="Suggestions and Corrections:", font=("Arial", 12, "bold")).pack()
suggestion_field = tk.Text(root, height=15, width=80, font=("Arial", 10), state='disabled', bg="#a1f5f5")
suggestion_field.pack(pady=5)

root.mainloop()
