print("Analizator tekstu:")

def analyze():
    text = input("Podaj tekst: ")
    a = "!@#$%^&*()-=_+/*.,:;<>""''"
    b = "1234567890"

    chars = 0
    special_chars = 0
    spaces =0
    lowercases = 0
    uppercases = 0
    numbers = 0

    for i in range(len(text)):   
        if text[i] == " ":
            spaces +=1
            pass
        else:
            if text[i].islower():
                lowercases += 1
            elif text[i].isupper():
                uppercases += 1    
            chars += text.count(text) 
            for char in a:
                if char == text[i]:
                    special_chars += 1
            for num in b:
                if num == text[i]:
                    numbers += 1        

    print(f"Łącznie znaków w tekscie: {chars+spaces}")                        
    print(f"Litery: {chars-special_chars-numbers}")
    print(f"Znaki specjalne: {special_chars}")
    print(f"Duze litery: {uppercases}")
    print(f"Male litery: {lowercases}")
    print(f"Liczby: {numbers}")
    print(f"Spacje: {spaces}")

analyze()        