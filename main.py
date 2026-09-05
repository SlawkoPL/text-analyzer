import tkinter as tk

# Main program

def analyze():
    text = text_input.get("1.0", "end-1c").replace("\r", "")

    chars = len(text)
    special_chars = 0
    spaces = 0
    lowercases = 0
    uppercases = 0
    numbers = 0

    for i in range(len(text)):   
        if text[i].isspace():
            spaces +=1
        elif text[i].islower():
            lowercases += 1
        elif text[i].isupper():
            uppercases += 1    
        elif text[i].isdigit():
            numbers += 1
        else:
            special_chars += 1         

    result = f"""📊 WYNIKI ANALIZY TEKSTU/RESULTS:
        ----------------------------------------
        ● Łącznie wszystkich znaków/All chars: {chars}
        ● Wszystkie litery/All letters: {uppercases+lowercases}
        └ Małe litery/Lowercases: {lowercases}
        └ Duże litery/Uppercases: {uppercases}
        ● Liczby (cyfry)/Numbers: {numbers}
        ● Znaki specjalne/Special chars: {special_chars}
        ● Spacje i entery/Spaces + enters: {spaces}""" 

    result_text.set(result)    

# GUI initialization
window = tk.Tk()
window.geometry("700x600")
window.title("Text analyzer - analizator tekstu")

info = tk.Label(window, text="Wprowadz tekst do analizy/Input text for analyze")
text_input = tk.Text(window)
analyze_button = tk.Button(window, text="Analyze", command=analyze)
result_text = tk.StringVar(window)
result_show = tk.Label(window, textvariable=result_text)
info.pack()
text_input.pack()
analyze_button.pack()
result_show.pack()
window.mainloop()