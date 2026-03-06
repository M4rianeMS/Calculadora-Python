import tkinter as tk

def calcular():
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        
        
        op = variavel_escolhida.get() 
        
        if op == "+": res = num1 + num2
        elif op == "-": res = num1 - num2
        elif op == "*": res = num1 * num2
        elif op == "/": 
            res = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
        else: 
            res = "Operação inválida"
        
        lbl_resultado.config(text=f"Resultado: {res}", fg="black")
    except Exception as e:
        
        lbl_resultado.config(text="Erro: Verifique os valores", fg="red") 

janela = tk.Tk()
janela.title("Minha Calculadora")
janela.geometry("250x250")

ent1 = tk.Entry(janela)
ent1.pack(pady=5)

opcoes = ["+", "-", "*", "/"]
variavel_escolhida = tk.StringVar(janela)
variavel_escolhida.set(opcoes[0]) # Valor padrão


menu_op = tk.OptionMenu(janela, variavel_escolhida, *opcoes)
menu_op.pack(pady=5)

ent2 = tk.Entry(janela)
ent2.pack(pady=5)

btn = tk.Button(janela, text="Calcular", command=calcular)
btn.pack(pady=10)

lbl_resultado = tk.Label(janela, text="Resultado: ")
lbl_resultado.pack(pady=10)

janela.mainloop()