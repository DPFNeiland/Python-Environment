import tkinter as tk

def button_click(texto):
    print(f"Butal {texto} clicado")

def main():
    window = tk.Tk()
    window.title("Batalha Naval")

    button = tk.Button(window,
                        text="Jogar PvP",
                        command=button_click)
    
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()