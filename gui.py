import tkinter as tk
from tkinter import Frame, Label, Canvas, ttk
import json
import os

def load_data():
    """Carrega os dados do data.json."""
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            try:
                data = json.load(f)
                return data.get("results", [])
            except json.JSONDecodeError:
                return []  # Retorna uma lista vazia em caso de erro
    return []

def get_color(number):
    """Retorna as cores de fundo e texto com base no número."""
    if number == 0:
        return "white", "black"
    elif 1 <= number <= 7:
        return "red", "black"
    elif 8 <= number <= 14:
        return "black", "white"
    else:
        return "gray", "black"

def update_display(result_frame, last_number_circle, last_number_label, white_table):
    """Atualiza o conteúdo da moldura com os dados do JSON e o último número."""
    data = load_data()
    numbers = [item['number'] for item in data]

    # Limita a exibição aos primeiros 10 números
    numbers = numbers[:12]

    # Limpa os widgets antigos
    for widget in result_frame.winfo_children():
        if widget != last_number_circle and widget != white_table:
            widget.destroy()

    title_label = tk.Label(result_frame, text="Últimos Resultados", font=('Arial', 16), anchor='c', width=10)  # Alinhado à direita
    title_label.pack(pady=10, padx=5, fill=tk.X)

    number_frame = Frame(result_frame, bg='gray')
    number_frame.pack(pady=5, anchor='w')

    for number in numbers:
        bg_color, text_color = get_color(number)
        radius = 20
        circle = Canvas(number_frame, width=radius * 2, height=radius * 2, bg='gray', highlightthickness=0)
        circle.pack(side=tk.LEFT, padx=5)
        circle.create_oval(0, 0, radius * 2, radius * 2, fill=bg_color, outline='black')
        circle.create_text(radius, radius, text=str(number), fill=text_color, font=('Arial', 12))

    if numbers:
        first_number = numbers[0]  # Obter o primeiro número da lista
        first_bg_color, first_text_color = get_color(first_number)

        last_number_label.config(text=str(first_number), bg=first_bg_color, fg=first_text_color)

        last_radius = 30
        last_number_circle.config(width=last_radius * 2, height=last_radius * 2)

        last_number_circle.delete("all")
        last_number_circle.create_oval(0, 0, last_radius * 2, last_radius * 2, fill=first_bg_color, outline='black')
        last_number_label.place(relx=0.5, rely=0.5, anchor='center')


    update_white_table(white_table, data)

    # Chama a função novamente após 5 segundos
    result_frame.after(5000, update_display, result_frame, last_number_circle, last_number_label, white_table)
def update_white_table(white_table, data):
    """Atualiza a tabela de minutos brancos."""
    for row in white_table.get_children():
        white_table.delete(row)

    for item in data:
        if item['number'] == 0:
            minute = int(item['minute'])  # Convertendo o minuto para inteiro
            high_prob = (minute + 6) % 60
            medium_prob = (minute + 10) % 60
            low_prob = (minute + 12) % 60
            white_table.insert("", "end", values=(minute, high_prob, medium_prob, low_prob))

def create_gui(): 
    """Cria a interface gráfica."""
    window = tk.Tk()
    window.title("Conteúdo do data.json")
    window.geometry("600x400")  # Definindo um tamanho fixo para a janela

    # Frame para os botões
    button_frame = Frame(window, bg='gray')
    button_frame.pack(pady=10)

    buttons = ["Menu", "Adm", "Padrões", "Histórico", "Gerenciamento", "BOT"]
    for button in buttons:
        btn = tk.Button(button_frame, text=button, font=('Arial', 12), bg='lightblue')
        btn.pack(side=tk.LEFT, padx=5)

    # Frame para os resultados
    result_frame = Frame(window, borderwidth=2, relief="solid", width=300, height=200, bg='gray')
    result_frame.pack(padx=10, pady=10, anchor='ne', fill=tk.Y)  # Posicionando no canto inferior direito

    last_radius = 30
    last_number_circle = Canvas(result_frame, width=last_radius * 2, height=last_radius * 2, bg='gray', highlightthickness=0)
    last_number_circle.pack(pady=10)

    sniper_label = Label(window, text="Sniper Branco", bg='lightblue', font=('Arial', 16), width=20)
    sniper_label.pack(pady=5)  # Colocando um pouco de espaço acima

    last_number_label = Label(last_number_circle, bg='gray', font=('Arial', 18))
    last_number_label.place(relx=0.5, rely=0.5, anchor='center')

    # Frame para a tabela de brancos
    white_table_frame = Frame(window, bg='gray')
    white_table_frame.pack(padx=10, pady=10, anchor='center', fill=tk.X)  # Centralizando
# Adicionando a Label quadrada para "Sniper Branco"
    
    columns = ("minute", "Alta", "Média", "Baixa")
    white_table = ttk.Treeview(white_table_frame, columns=columns, show='headings')
    

    for col in columns:
        white_table.heading(col, text=col)
        white_table.column(col, anchor='center', width=100)

    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 12, 'bold'))
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

    white_table.pack(padx=10, pady=10, anchor='center', fill=tk.X)  # Centralizando

    

    # Carregar os dados iniciais
    update_display(result_frame, last_number_circle, last_number_label, white_table)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
