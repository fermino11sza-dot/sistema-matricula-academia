import tkinter as tk
from tkinter import messagebox

def adicionar_aluno():
    nome = entry_nome.get().strip()
    curso = entry_curso.get().strip()

    if not nome or not curso:
        messagebox.showwarning("Campos vazios", "Por favor, preencha os dois campos.")
        return

    lista_alunos.insert(tk.END, f"{nome} - {curso}")

    entry_nome.delete(0, tk.END)
    entry_curso.delete(0, tk.END)
    entry_nome.focus()

def limpar_lista():
    lista_alunos.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Alunos - SENAI")
janela.geometry("400x400")
janela.resizable(False, False)

frame_campos = tk.Frame(janela, padx=10, pady=10)
frame_campos.pack(fill="x")

label_nome = tk.Label(frame_campos, text="Nome do aluno")
label_nome.grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame_campos, width=30)
entry_nome.grid(row=0, column=1, pady=5)

label_curso = tk.Label(frame_campos, text="Curso")
label_curso.grid(row=1, column=0, sticky="w", pady=5)
entry_curso = tk.Entry(frame_campos, width=30)
entry_curso.grid(row=1, column=1, pady=5)

frame_botoes = tk.Frame(janela, padx=10, pady=5)
frame_botoes.pack(fill="x")

botao_adicionar = tk.Button(frame_botoes, text="Adicionar", command=adicionar_aluno, width=15)
botao_adicionar.pack(side="left", padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar lista", command=limpar_lista, width=15)
botao_limpar.pack(side="left", padx=5)

frame_lista = tk.Frame(janela, padx=10, pady=10)
frame_lista.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

lista_alunos = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 11))
lista_alunos.pack(fill="both", expand=True)

scrollbar.config(command=lista_alunos.yview)

entry_nome.focus()

janela.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def adicionar_aluno():
    nome = entry_nome.get().strip()
    curso = entry_curso.get().strip()
    idade = entry_idade.get().strip()
    email = entry_email.get().strip()
    turno = turno_var.get()
    telefone = entry_telefone.get().strip()

    if not nome or not curso or not idade or not email or not turno or not telefone:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    lista_alunos.insert(
        tk.END,
        f"{nome} - {curso} - Idade: {idade} - E-mail: {email} - Turno: {turno} - Tel: {telefone}"
    )

    entry_nome.delete(0, tk.END)
    entry_curso.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    turno_var.set("")
    entry_nome.focus()

def limpar_lista():
    lista_alunos.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Alunos - SENAI")
janela.geometry("520x520")
janela.resizable(False, False)

frame_campos = tk.Frame(janela, padx=10, pady=10)
frame_campos.pack(fill="x")

label_nome = tk.Label(frame_campos, text="Nome do aluno")
label_nome.grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame_campos, width=35)
entry_nome.grid(row=0, column=1, pady=5)

label_curso = tk.Label(frame_campos, text="Curso")
label_curso.grid(row=1, column=0, sticky="w", pady=5)
entry_curso = tk.Entry(frame_campos, width=35)
entry_curso.grid(row=1, column=1, pady=5)

label_idade = tk.Label(frame_campos, text="Idade")
label_idade.grid(row=2, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(frame_campos, width=35)
entry_idade.grid(row=2, column=1, pady=5)

label_email = tk.Label(frame_campos, text="E-mail")
label_email.grid(row=3, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame_campos, width=35)
entry_email.grid(row=3, column=1, pady=5)

label_turno = tk.Label(frame_campos, text="Turno")
label_turno.grid(row=4, column=0, sticky="w", pady=5)
turno_var = tk.StringVar()
combo_turno = ttk.Combobox(
    frame_campos, textvariable=turno_var,
    values=["Manhã", "Tarde", "Noite"], width=32, state="readonly"
)
combo_turno.grid(row=4, column=1, pady=5)

label_telefone = tk.Label(frame_campos, text="Telefone")
label_telefone.grid(row=5, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(frame_campos, width=35)
entry_telefone.grid(row=5, column=1, pady=5)

frame_botoes = tk.Frame(janela, padx=10, pady=5)
frame_botoes.pack(fill="x")

botao_adicionar = tk.Button(frame_botoes, text="Adicionar", command=adicionar_aluno, width=15)
botao_adicionar.pack(side="left", padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar lista", command=limpar_lista, width=15)
botao_limpar.pack(side="left", padx=5)

frame_lista = tk.Frame(janela, padx=10, pady=10)
frame_lista.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

lista_alunos = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 10))
lista_alunos.pack(fill="both", expand=True)

scrollbar.config(command=lista_alunos.yview)

entry_nome.focus()

janela.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

CURSOS = [
    "Eletrotécnica",
    "Mecânica Industrial",
    "Informática",
    "Automação Industrial",
    "Logística",
    "Segurança do Trabalho",
    "Mecatrônica",
    "Administração"
]

FORMAS_PAGAMENTO = [
    "Boleto",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Pix",
    "Dinheiro"
]

SITUACAO_PAGAMENTO = [
    "Pago",
    "Pendente"
]

def adicionar_aluno():
    nome = entry_nome.get().strip()
    curso = curso_var.get()
    idade = entry_idade.get().strip()
    email = entry_email.get().strip()
    turno = turno_var.get()
    telefone = entry_telefone.get().strip()
    pagamento = pagamento_var.get()
    situacao = situacao_var.get()

    if not nome or not curso or not idade or not email or not turno or not telefone or not pagamento or not situacao:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    lista_alunos.insert(
        tk.END,
        f"{nome} - {curso} - Idade: {idade} - E-mail: {email} - Turno: {turno} - "
        f"Tel: {telefone} - Pagamento: {pagamento} ({situacao})"
    )

    entry_nome.delete(0, tk.END)
    curso_var.set("")
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    turno_var.set("")
    pagamento_var.set("")
    situacao_var.set("")
    entry_nome.focus()

def limpar_lista():
    lista_alunos.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Alunos - SENAI")
janela.geometry("560x600")
janela.resizable(False, False)

frame_campos = tk.Frame(janela, padx=10, pady=10)
frame_campos.pack(fill="x")

label_nome = tk.Label(frame_campos, text="Nome do aluno")
label_nome.grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame_campos, width=35)
entry_nome.grid(row=0, column=1, pady=5)

label_curso = tk.Label(frame_campos, text="Curso")
label_curso.grid(row=1, column=0, sticky="w", pady=5)
curso_var = tk.StringVar()
combo_curso = ttk.Combobox(
    frame_campos, textvariable=curso_var,
    values=CURSOS, width=32, state="readonly"
)
combo_curso.grid(row=1, column=1, pady=5)

label_idade = tk.Label(frame_campos, text="Idade")
label_idade.grid(row=2, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(frame_campos, width=35)
entry_idade.grid(row=2, column=1, pady=5)

label_email = tk.Label(frame_campos, text="E-mail")
label_email.grid(row=3, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame_campos, width=35)
entry_email.grid(row=3, column=1, pady=5)

label_turno = tk.Label(frame_campos, text="Turno")
label_turno.grid(row=4, column=0, sticky="w", pady=5)
turno_var = tk.StringVar()
combo_turno = ttk.Combobox(
    frame_campos, textvariable=turno_var,
    values=["Manhã", "Tarde", "Noite"], width=32, state="readonly"
)
combo_turno.grid(row=4, column=1, pady=5)

label_telefone = tk.Label(frame_campos, text="Telefone")
label_telefone.grid(row=5, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(frame_campos, width=35)
entry_telefone.grid(row=5, column=1, pady=5)

label_pagamento = tk.Label(frame_campos, text="Forma de Pagamento")
label_pagamento.grid(row=6, column=0, sticky="w", pady=5)
pagamento_var = tk.StringVar()
combo_pagamento = ttk.Combobox(
    frame_campos, textvariable=pagamento_var,
    values=FORMAS_PAGAMENTO, width=32, state="readonly"
)
combo_pagamento.grid(row=6, column=1, pady=5)

label_situacao = tk.Label(frame_campos, text="Situação do Pagamento")
label_situacao.grid(row=7, column=0, sticky="w", pady=5)
situacao_var = tk.StringVar()
combo_situacao = ttk.Combobox(
    frame_campos, textvariable=situacao_var,
    values=SITUACAO_PAGAMENTO, width=32, state="readonly"
)
combo_situacao.grid(row=7, column=1, pady=5)

frame_botoes = tk.Frame(janela, padx=10, pady=5)
frame_botoes.pack(fill="x")

botao_adicionar = tk.Button(frame_botoes, text="Adicionar", command=adicionar_aluno, width=15)
botao_adicionar.pack(side="left", padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar lista", command=limpar_lista, width=15)
botao_limpar.pack(side="left", padx=5)

frame_lista = tk.Frame(janela, padx=10, pady=10)
frame_lista.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

lista_alunos = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 10))
lista_alunos.pack(fill="both", expand=True)

scrollbar.config(command=lista_alunos.yview)

entry_nome.focus()

janela.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

# Cores do padrão visual SENAI
COR_VERMELHO = "#EE1B24"
COR_CINZA_ESCURO = "#2D2D2D"
COR_BRANCO = "#FFFFFF"
COR_CINZA_CLARO = "#F2F2F2"

CURSOS = [
    "Eletrotécnica",
    "Mecânica Industrial",
    "Informática",
    "Automação Industrial",
    "Logística",
    "Segurança do Trabalho",
    "Mecatrônica",
    "Administração"
]

FORMAS_PAGAMENTO = [
    "Boleto",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Pix",
    "Dinheiro"
]

SITUACAO_PAGAMENTO = [
    "Pago",
    "Pendente"
]

def adicionar_aluno():
    nome = entry_nome.get().strip()
    curso = curso_var.get()
    idade = entry_idade.get().strip()
    email = entry_email.get().strip()
    turno = turno_var.get()
    telefone = entry_telefone.get().strip()
    pagamento = pagamento_var.get()
    situacao = situacao_var.get()

    if not nome or not curso or not idade or not email or not turno or not telefone or not pagamento or not situacao:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    lista_alunos.insert(
        tk.END,
        f"{nome} - {curso} - Idade: {idade} - E-mail: {email} - Turno: {turno} - "
        f"Tel: {telefone} - Pagamento: {pagamento} ({situacao})"
    )

    entry_nome.delete(0, tk.END)
    curso_var.set("")
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    turno_var.set("")
    pagamento_var.set("")
    situacao_var.set("")
    entry_nome.focus()

def limpar_lista():
    lista_alunos.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Alunos - SENAI")
janela.geometry("600x680")
janela.resizable(False, False)
janela.configure(bg=COR_CINZA_CLARO)

# Estilo para os Combobox (ttk)
estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure(
    "TCombobox",
    fieldbackground=COR_BRANCO,
    background=COR_BRANCO,
    foreground=COR_CINZA_ESCURO,
    arrowcolor=COR_VERMELHO,
    padding=4
)

# ---------- Cabeçalho ----------
frame_cabecalho = tk.Frame(janela, bg=COR_VERMELHO, height=90)
frame_cabecalho.pack(fill="x")
frame_cabecalho.pack_propagate(False)

label_titulo = tk.Label(
    frame_cabecalho,
    text="SENAI",
    font=("Arial", 26, "bold"),
    bg=COR_VERMELHO,
    fg=COR_BRANCO
)
label_titulo.pack(pady=(12, 0))

label_subtitulo = tk.Label(
    frame_cabecalho,
    text="Cadastro de Alunos",
    font=("Arial", 12),
    bg=COR_VERMELHO,
    fg=COR_BRANCO
)
label_subtitulo.pack()

# ---------- Formulário ----------
frame_campos = tk.Frame(janela, bg=COR_CINZA_CLARO, padx=20, pady=20)
frame_campos.pack(fill="x")

fonte_label = ("Arial", 10, "bold")
fonte_campo = ("Arial", 10)

def criar_label(texto, linha):
    tk.Label(
        frame_campos, text=texto, font=fonte_label,
        bg=COR_CINZA_CLARO, fg=COR_CINZA_ESCURO, anchor="w"
    ).grid(row=linha, column=0, sticky="w", pady=8, padx=(0, 10))

criar_label("Nome do aluno", 0)
entry_nome = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_nome.grid(row=0, column=1, pady=8)

criar_label("Curso", 1)
curso_var = tk.StringVar()
combo_curso = ttk.Combobox(
    frame_campos, textvariable=curso_var,
    values=CURSOS, width=32, state="readonly", font=fonte_campo
)
combo_curso.grid(row=1, column=1, pady=8)

criar_label("Idade", 2)
entry_idade = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_idade.grid(row=2, column=1, pady=8)

criar_label("E-mail", 3)
entry_email = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_email.grid(row=3, column=1, pady=8)

criar_label("Turno", 4)
turno_var = tk.StringVar()
combo_turno = ttk.Combobox(
    frame_campos, textvariable=turno_var,
    values=["Manhã", "Tarde", "Noite"], width=32, state="readonly", font=fonte_campo
)
combo_turno.grid(row=4, column=1, pady=8)

criar_label("Telefone", 5)
entry_telefone = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_telefone.grid(row=5, column=1, pady=8)

criar_label("Forma de Pagamento", 6)
pagamento_var = tk.StringVar()
combo_pagamento = ttk.Combobox(
    frame_campos, textvariable=pagamento_var,
    values=FORMAS_PAGAMENTO, width=32, state="readonly", font=fonte_campo
)
combo_pagamento.grid(row=6, column=1, pady=8)

criar_label("Situação do Pagamento", 7)
situacao_var = tk.StringVar()
combo_situacao = ttk.Combobox(
    frame_campos, textvariable=situacao_var,
    values=SITUACAO_PAGAMENTO, width=32, state="readonly", font=fonte_campo
)
combo_situacao.grid(row=7, column=1, pady=8)

# ---------- Botões ----------
frame_botoes = tk.Frame(janela, bg=COR_CINZA_CLARO, pady=10)
frame_botoes.pack(fill="x")

botao_adicionar = tk.Button(
    frame_botoes, text="Adicionar", command=adicionar_aluno,
    width=15, font=("Arial", 10, "bold"),
    bg=COR_VERMELHO, fg=COR_BRANCO,
    activebackground="#C4141C", activeforeground=COR_BRANCO,
    relief="flat", cursor="hand2"
)
botao_adicionar.pack(side="left", padx=20)

botao_limpar = tk.Button(
    frame_botoes, text="Limpar lista", command=limpar_lista,
    width=15, font=("Arial", 10, "bold"),
    bg=COR_CINZA_ESCURO, fg=COR_BRANCO,
    activebackground="#1A1A1A", activeforeground=COR_BRANCO,
    relief="flat", cursor="hand2"
)
botao_limpar.pack(side="left")

# ---------- Lista de alunos ----------
frame_lista = tk.Frame(janela, bg=COR_CINZA_CLARO, padx=20, pady=10)
frame_lista.pack(fill="both", expand=True)

label_lista = tk.Label(
    frame_lista, text="Alunos cadastrados", font=("Arial", 11, "bold"),
    bg=COR_CINZA_CLARO, fg=COR_CINZA_ESCURO, anchor="w"
)
label_lista.pack(fill="x", pady=(0, 5))

frame_listbox = tk.Frame(frame_lista, bd=1, relief="solid")
frame_listbox.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side="right", fill="y")

lista_alunos = tk.Listbox(
    frame_listbox, yscrollcommand=scrollbar.set,
    font=("Arial", 10), bg=COR_BRANCO, fg=COR_CINZA_ESCURO,
    selectbackground=COR_VERMELHO, selectforeground=COR_BRANCO,
    relief="flat", bd=0
)
lista_alunos.pack(fill="both", expand=True)

scrollbar.config(command=lista_alunos.yview)

entry_nome.focus()

janela.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

# Cores do padrão visual SENAI
COR_VERMELHO = "#EE1B24"
COR_CINZA_ESCURO = "#2D2D2D"
COR_BRANCO = "#FFFFFF"
COR_CINZA_CLARO = "#F2F2F2"

CURSOS = [
    "Eletrotécnica",
    "Mecânica Industrial",
    "Informática",
    "Automação Industrial",
    "Logística",
    "Segurança do Trabalho",
    "Mecatrônica",
    "Administração"
]

FORMAS_PAGAMENTO = [
    "Boleto",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Pix",
    "Dinheiro"
]

SITUACAO_PAGAMENTO = [
    "Pago",
    "Pendente"
]

def verificar_idade(*args):
    idade_texto = entry_idade.get().strip()

    if idade_texto.isdigit() and int(idade_texto) < 18:
        frame_responsavel.pack(fill="x", pady=(0, 10), before=frame_botoes)
    else:
        frame_responsavel.pack_forget()

def adicionar_aluno():
    nome = entry_nome.get().strip()
    curso = curso_var.get()
    idade_texto = entry_idade.get().strip()
    email = entry_email.get().strip()
    turno = turno_var.get()
    telefone = entry_telefone.get().strip()
    pagamento = pagamento_var.get()
    situacao = situacao_var.get()

    if not nome or not curso or not idade_texto or not email or not turno or not telefone or not pagamento or not situacao:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    if not idade_texto.isdigit():
        messagebox.showwarning("Idade inválida", "Digite a idade usando apenas números.")
        return

    idade = int(idade_texto)
    menor_idade = idade < 18
    nome_responsavel = ""
    telefone_responsavel = ""

    if menor_idade:
        nome_responsavel = entry_nome_resp.get().strip()
        telefone_responsavel = entry_tel_resp.get().strip()

        if not nome_responsavel or not telefone_responsavel:
            messagebox.showwarning(
                "Dados do responsável obrigatórios",
                "Como o aluno é menor de idade, informe o nome e o telefone do responsável."
            )
            return

        if not confirmacao_var.get():
            messagebox.showwarning(
                "Confirmação necessária",
                "Confirme que o cadastro está sendo feito com autorização do responsável legal."
            )
            return

    linha = f"{nome} - {curso} - Idade: {idade} - E-mail: {email} - Turno: {turno} - " \
            f"Tel: {telefone} - Pagamento: {pagamento} ({situacao})"

    if menor_idade:
        linha += f" - [MENOR DE IDADE] Responsável: {nome_responsavel} - Tel. Resp.: {telefone_responsavel}"

    lista_alunos.insert(tk.END, linha)

    entry_nome.delete(0, tk.END)
    curso_var.set("")
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    turno_var.set("")
    pagamento_var.set("")
    situacao_var.set("")
    entry_nome_resp.delete(0, tk.END)
    entry_tel_resp.delete(0, tk.END)
    confirmacao_var.set(False)
    frame_responsavel.pack_forget()
    entry_nome.focus()

def limpar_lista():
    lista_alunos.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Alunos - SENAI")
janela.geometry("600x760")
janela.resizable(False, False)
janela.configure(bg=COR_CINZA_CLARO)

# Estilo para os Combobox (ttk)
estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure(
    "TCombobox",
    fieldbackground=COR_BRANCO,
    background=COR_BRANCO,
    foreground=COR_CINZA_ESCURO,
    arrowcolor=COR_VERMELHO,
    padding=4
)

# ---------- Cabeçalho ----------
frame_cabecalho = tk.Frame(janela, bg=COR_VERMELHO, height=90)
frame_cabecalho.pack(fill="x")
frame_cabecalho.pack_propagate(False)

label_titulo = tk.Label(
    frame_cabecalho,
    text="SENAI",
    font=("Arial", 26, "bold"),
    bg=COR_VERMELHO,
    fg=COR_BRANCO
)
label_titulo.pack(pady=(12, 0))

label_subtitulo = tk.Label(
    frame_cabecalho,
    text="Cadastro de Alunos",
    font=("Arial", 12),
    bg=COR_VERMELHO,
    fg=COR_BRANCO
)
label_subtitulo.pack()

# ---------- Formulário ----------
frame_campos = tk.Frame(janela, bg=COR_CINZA_CLARO, padx=20, pady=20)
frame_campos.pack(fill="x")

fonte_label = ("Arial", 10, "bold")
fonte_campo = ("Arial", 10)

def criar_label(pai, texto, linha):
    tk.Label(
        pai, text=texto, font=fonte_label,
        bg=COR_CINZA_CLARO, fg=COR_CINZA_ESCURO, anchor="w"
    ).grid(row=linha, column=0, sticky="w", pady=8, padx=(0, 10))

criar_label(frame_campos, "Nome do aluno", 0)
entry_nome = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_nome.grid(row=0, column=1, pady=8)

criar_label(frame_campos, "Curso", 1)
curso_var = tk.StringVar()
combo_curso = ttk.Combobox(
    frame_campos, textvariable=curso_var,
    values=CURSOS, width=32, state="readonly", font=fonte_campo
)
combo_curso.grid(row=1, column=1, pady=8)

criar_label(frame_campos, "Idade", 2)
entry_idade = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_idade.grid(row=2, column=1, pady=8)
entry_idade.bind("<KeyRelease>", verificar_idade)

criar_label(frame_campos, "E-mail", 3)
entry_email = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_email.grid(row=3, column=1, pady=8)

criar_label(frame_campos, "Turno", 4)
turno_var = tk.StringVar()
combo_turno = ttk.Combobox(
    frame_campos, textvariable=turno_var,
    values=["Manhã", "Tarde", "Noite"], width=32, state="readonly", font=fonte_campo
)
combo_turno.grid(row=4, column=1, pady=8)

criar_label(frame_campos, "Telefone", 5)
entry_telefone = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_telefone.grid(row=5, column=1, pady=8)

criar_label(frame_campos, "Forma de Pagamento", 6)
pagamento_var = tk.StringVar()
combo_pagamento = ttk.Combobox(
    frame_campos, textvariable=pagamento_var,
    values=FORMAS_PAGAMENTO, width=32, state="readonly", font=fonte_campo
)
combo_pagamento.grid(row=6, column=1, pady=8)

criar_label(frame_campos, "Situação do Pagamento", 7)
situacao_var = tk.StringVar()
combo_situacao = ttk.Combobox(
    frame_campos, textvariable=situacao_var,
    values=SITUACAO_PAGAMENTO, width=32, state="readonly", font=fonte_campo
)
combo_situacao.grid(row=7, column=1, pady=8)

# ---------- Bloco do responsável (aparece só se menor de idade) ----------
frame_responsavel = tk.Frame(janela, bg="#FCE9E9", padx=20, pady=15, bd=1, relief="solid")

label_aviso_resp = tk.Label(
    frame_responsavel,
    text="⚠ Aluno menor de idade — dados do responsável obrigatórios",
    font=("Arial", 10, "bold"),
    bg="#FCE9E9", fg=COR_VERMELHO
)
label_aviso_resp.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

criar_label(frame_responsavel, "Nome do responsável", 1)
entry_nome_resp = tk.Entry(frame_responsavel, width=35, font=fonte_campo, relief="solid", bd=1)
entry_nome_resp.grid(row=1, column=1, pady=8)

criar_label(frame_responsavel, "Telefone do responsável", 2)
entry_tel_resp = tk.Entry(frame_responsavel, width=35, font=fonte_campo, relief="solid", bd=1)
entry_tel_resp.grid(row=2, column=1, pady=8)

confirmacao_var = tk.BooleanVar()
check_confirmacao = tk.Checkbutton(
    frame_responsavel,
    text="Confirmo que este cadastro está sendo feito com autorização do responsável legal",
    variable=confirmacao_var,
    bg="#FCE9E9", fg=COR_CINZA_ESCURO,
    font=("Arial", 9), wraplength=480, justify="left",
    activebackground="#FCE9E9"
)
check_confirmacao.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))

# ---------- Botões ----------
frame_botoes = tk.Frame(janela, bg=COR_CINZA_CLARO, pady=10)
frame_botoes.pack(fill="x")

botao_adicionar = tk.Button(
    frame_botoes, text="Adicionar", command=adicionar_aluno,
    width=15, font=("Arial", 10, "bold"),
    bg=COR_VERMELHO, fg=COR_BRANCO,
    activebackground="#C4141C", activeforeground=COR_BRANCO,
    relief="flat", cursor="hand2"
)
botao_adicionar.pack(side="left", padx=20)

botao_limpar = tk.Button(
    frame_botoes, text="Limpar lista", command=limpar_lista,
    width=15, font=("Arial", 10, "bold"),
    bg=COR_CINZA_ESCURO, fg=COR_BRANCO,
    activebackground="#1A1A1A", activeforeground=COR_BRANCO,
    relief="flat", cursor="hand2"
)
botao_limpar.pack(side="left")

# ---------- Lista de alunos ----------
frame_lista = tk.Frame(janela, bg=COR_CINZA_CLARO, padx=20, pady=10)
frame_lista.pack(fill="both", expand=True)

label_lista = tk.Label(
    frame_lista, text="Alunos cadastrados", font=("Arial", 11, "bold"),
    bg=COR_CINZA_CLARO, fg=COR_CINZA_ESCURO, anchor="w"
)
label_lista.pack(fill="x", pady=(0, 5))

frame_listbox = tk.Frame(frame_lista, bd=1, relief="solid")
frame_listbox.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side="right", fill="y")

lista_alunos = tk.Listbox(
    frame_listbox, yscrollcommand=scrollbar.set,
    font=("Arial", 10), bg=COR_BRANCO, fg=COR_CINZA_ESCURO,
    selectbackground=COR_VERMELHO, selectforeground=COR_BRANCO,
    relief="flat", bd=0
)
lista_alunos.pack(fill="both", expand=True)

scrollbar.config(command=lista_alunos.yview)

entry_nome.focus()

janela.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

# Cores do padrão visual SENAI
COR_VERMELHO = "#EE1B24"
COR_CINZA_ESCURO = "#2D2D2D"
COR_BRANCO = "#FFFFFF"
COR_CINZA_CLARO = "#F2F2F2"

IDADE_MINIMA = 15  # não é permitido cadastrar alunos com 14 anos ou menos

CURSOS = [
    "Eletrotécnica",
    "Mecânica Industrial",
    "Informática",
    "Automação Industrial",
    "Logística",
    "Segurança do Trabalho",
    "Mecatrônica",
    "Administração"
]

FORMAS_PAGAMENTO = [
    "Boleto",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Pix",
    "Dinheiro"
]

SITUACAO_PAGAMENTO = [
    "Pago",
    "Pendente"
]


def somente_numeros(texto):
    return "".join(filter(str.isdigit, texto))


def verificar_idade(*args):
    idade_texto = entry_idade.get().strip()

    if idade_texto.isdigit() and int(idade_texto) < 18:
        frame_responsavel.pack(fill="x", pady=(0, 10), before=frame_botoes)
    else:
        frame_responsavel.pack_forget()


def adicionar_aluno():
    nome = entry_nome.get().strip()
    curso = curso_var.get()
    idade_texto = entry_idade.get().strip()
    email = entry_email.get().strip()
    turno = turno_var.get()
    telefone = entry_telefone.get().strip()
    pagamento = pagamento_var.get()
    situacao = situacao_var.get()
    cpf = entry_cpf.get().strip()
    rua = entry_rua.get().strip()
    numero = entry_numero.get().strip()
    bairro = entry_bairro.get().strip()
    cidade = entry_cidade.get().strip()
    contato_emergencia = entry_contato_emerg.get().strip()
    alergias_condicoes = texto_saude.get("1.0", tk.END).strip()

    campos_obrigatorios = [
        nome, curso, idade_texto, email, turno, telefone, pagamento, situacao,
        cpf, rua, numero, bairro, cidade, contato_emergencia
    ]

    if not all(campos_obrigatorios):
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    if not idade_texto.isdigit():
        messagebox.showwarning("Idade inválida", "Digite a idade usando apenas números.")
        return

    idade = int(idade_texto)

    if idade <= 14:
        messagebox.showerror(
            "Inscrição não permitida",
            f"Não é permitida a inscrição de alunos com {IDADE_MINIMA - 1} anos ou menos.\n"
            f"Idade mínima para cadastro: {IDADE_MINIMA} anos."
        )
        return

    cpf_numeros = somente_numeros(cpf)
    if len(cpf_numeros) != 11:
        messagebox.showwarning("CPF inválido", "Digite um CPF válido, com 11 números.")
        return

    menor_idade = idade < 18
    nome_responsavel = ""
    telefone_responsavel = ""

    if menor_idade:
        nome_responsavel = entry_nome_resp.get().strip()
        telefone_responsavel = entry_tel_resp.get().strip()

        if not nome_responsavel or not telefone_responsavel:
            messagebox.showwarning(
                "Dados do responsável obrigatórios",
                "Como o aluno é menor de idade, informe o nome e o telefone do responsável."
            )
            return

        if not confirmacao_var.get():
            messagebox.showwarning(
                "Confirmação necessária",
                "Confirme que o cadastro está sendo feito com autorização do responsável legal."
            )
            return

    if not alergias_condicoes:
        alergias_condicoes = "Nenhuma informada"

    endereco = f"{rua}, nº {numero} - {bairro} - {cidade}"

    linha = (
        f"{nome} - CPF: {cpf} - {curso} - Idade: {idade} - E-mail: {email} - "
        f"Turno: {turno} - Tel: {telefone} - Endereço: {endereco} - "
        f"Pagamento: {pagamento} ({situacao}) - "
        f"Emergência: {contato_emergencia} - Saúde: {alergias_condicoes}"
    )

    if menor_idade:
        linha += f" - [MENOR DE IDADE] Responsável: {nome_responsavel} - Tel. Resp.: {telefone_responsavel}"

    lista_alunos.insert(tk.END, linha)

    entry_nome.delete(0, tk.END)
    curso_var.set("")
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    turno_var.set("")
    pagamento_var.set("")
    situacao_var.set("")
    entry_cpf.delete(0, tk.END)
    entry_rua.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_bairro.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_contato_emerg.delete(0, tk.END)
    texto_saude.delete("1.0", tk.END)
    entry_nome_resp.delete(0, tk.END)
    entry_tel_resp.delete(0, tk.END)
    confirmacao_var.set(False)
    frame_responsavel.pack_forget()
    entry_nome.focus()


def limpar_lista():
    lista_alunos.delete(0, tk.END)


janela = tk.Tk()
janela.title("Cadastro de Alunos - SENAI")
janela.geometry("650x900")
janela.resizable(False, False)
janela.configure(bg=COR_CINZA_CLARO)

# Estilo para os Combobox (ttk)
estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure(
    "TCombobox",
    fieldbackground=COR_BRANCO,
    background=COR_BRANCO,
    foreground=COR_CINZA_ESCURO,
    arrowcolor=COR_VERMELHO,
    padding=4
)

# ---------- Canvas com scroll (formulário ficou grande) ----------
canvas_principal = tk.Canvas(janela, bg=COR_CINZA_CLARO, highlightthickness=0)
scrollbar_geral = tk.Scrollbar(janela, orient="vertical", command=canvas_principal.yview)
frame_scrollavel = tk.Frame(canvas_principal, bg=COR_CINZA_CLARO)

frame_scrollavel.bind(
    "<Configure>",
    lambda e: canvas_principal.configure(scrollregion=canvas_principal.bbox("all"))
)

canvas_principal.create_window((0, 0), window=frame_scrollavel, anchor="nw")
canvas_principal.configure(yscrollcommand=scrollbar_geral.set)

canvas_principal.pack(side="left", fill="both", expand=True)
scrollbar_geral.pack(side="right", fill="y")


def _on_mousewheel(event):
    canvas_principal.yview_scroll(int(-1 * (event.delta / 120)), "units")


canvas_principal.bind_all("<MouseWheel>", _on_mousewheel)

# ---------- Cabeçalho ----------
frame_cabecalho = tk.Frame(frame_scrollavel, bg=COR_VERMELHO, height=90, width=650)
frame_cabecalho.pack(fill="x")
frame_cabecalho.pack_propagate(False)

label_titulo = tk.Label(
    frame_cabecalho,
    text="SENAI",
    font=("Arial", 26, "bold"),
    bg=COR_VERMELHO,
    fg=COR_BRANCO
)
label_titulo.pack(pady=(12, 0))

label_subtitulo = tk.Label(
    frame_cabecalho,
    text="Cadastro de Alunos",
    font=("Arial", 12),
    bg=COR_VERMELHO,
    fg=COR_BRANCO
)
label_subtitulo.pack()

# ---------- Formulário principal ----------
frame_campos = tk.Frame(frame_scrollavel, bg=COR_CINZA_CLARO, padx=20, pady=20)
frame_campos.pack(fill="x")

fonte_label = ("Arial", 10, "bold")
fonte_campo = ("Arial", 10)


def criar_label(pai, texto, linha, coluna=0):
    tk.Label(
        pai, text=texto, font=fonte_label,
        bg=pai["bg"], fg=COR_CINZA_ESCURO, anchor="w"
    ).grid(row=linha, column=coluna, sticky="w", pady=8, padx=(0, 10))


criar_label(frame_campos, "Nome do aluno", 0)
entry_nome = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_nome.grid(row=0, column=1, pady=8)

criar_label(frame_campos, "CPF", 1)
entry_cpf = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_cpf.grid(row=1, column=1, pady=8)

criar_label(frame_campos, "Curso", 2)
curso_var = tk.StringVar()
combo_curso = ttk.Combobox(
    frame_campos, textvariable=curso_var,
    values=CURSOS, width=32, state="readonly", font=fonte_campo
)
combo_curso.grid(row=2, column=1, pady=8)

criar_label(frame_campos, "Idade", 3)
entry_idade = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_idade.grid(row=3, column=1, pady=8)
entry_idade.bind("<KeyRelease>", verificar_idade)

criar_label(frame_campos, "E-mail", 4)
entry_email = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_email.grid(row=4, column=1, pady=8)

criar_label(frame_campos, "Turno", 5)
turno_var = tk.StringVar()
combo_turno = ttk.Combobox(
    frame_campos, textvariable=turno_var,
    values=["Manhã", "Tarde", "Noite"], width=32, state="readonly", font=fonte_campo
)
combo_turno.grid(row=5, column=1, pady=8)

criar_label(frame_campos, "Telefone", 6)
entry_telefone = tk.Entry(frame_campos, width=35, font=fonte_campo, relief="solid", bd=1)
entry_telefone.grid(row=6, column=1, pady=8)

criar_label(frame_campos, "Forma de Pagamento", 7)
pagamento_var = tk.StringVar()
combo_pagamento = ttk.Combobox(
    frame_campos, textvariable=pagamento_var,
    values=FORMAS_PAGAMENTO, width=32, state="readonly", font=fonte_campo
)
combo_pagamento.grid(row=7, column=1, pady=8)

criar_label(frame_campos, "Situação do Pagamento", 8)
situacao_var = tk.StringVar()
combo_situacao = ttk.Combobox(
    frame_campos, textvariable=situacao_var,
    values=SITUACAO_PAGAMENTO, width=32, state="readonly", font=fonte_campo
)
combo_situacao.grid(row=8, column=1, pady=8)

# ---------- Endereço ----------
frame_endereco = tk.Frame(frame_scrollavel, bg=COR_CINZA_CLARO, padx=20, pady=5)
frame_endereco.pack(fill="x")

label_titulo_endereco = tk.Label(
    frame_endereco, text="Endereço", font=("Arial", 11, "bold"),
    bg=COR_CINZA_CLARO, fg=COR_VERMELHO, anchor="w"
)
label_titulo_endereco.grid(row=0, column=0, columnspan=2, sticky="w", pady=(5, 10))

criar_label(frame_endereco, "Rua", 1)
entry_rua = tk.Entry(frame_endereco, width=35, font=fonte_campo, relief="solid", bd=1)
entry_rua.grid(row=1, column=1, pady=8)

criar_label(frame_endereco, "Número", 2)
entry_numero = tk.Entry(frame_endereco, width=35, font=fonte_campo, relief="solid", bd=1)
entry_numero.grid(row=2, column=1, pady=8)

criar_label(frame_endereco, "Bairro", 3)
entry_bairro = tk.Entry(frame_endereco, width=35, font=fonte_campo, relief="solid", bd=1)
entry_bairro.grid(row=3, column=1, pady=8)

criar_label(frame_endereco, "Cidade", 4)
entry_cidade = tk.Entry(frame_endereco, width=35, font=fonte_campo, relief="solid", bd=1)
entry_cidade.grid(row=4, column=1, pady=8)

# ---------- Saúde / Emergência ----------
frame_saude = tk.Frame(frame_scrollavel, bg="#FFF6E5", padx=20, pady=15, bd=1, relief="solid")
frame_saude.pack(fill="x", padx=20, pady=15)

label_titulo_saude = tk.Label(
    frame_saude, text="Informações de Saúde e Emergência",
    font=("Arial", 11, "bold"), bg="#FFF6E5", fg=COR_VERMELHO, anchor="w"
)
label_titulo_saude.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

tk.Label(
    frame_saude, text="Contato de emergência (nome e telefone)",
    font=fonte_label, bg="#FFF6E5", fg=COR_CINZA_ESCURO, anchor="w"
).grid(row=1, column=0, sticky="w", pady=8, padx=(0, 10))
entry_contato_emerg = tk.Entry(frame_saude, width=35, font=fonte_campo, relief="solid", bd=1)
entry_contato_emerg.grid(row=1, column=1, pady=8)

tk.Label(
    frame_saude,
    text="Alergias, condições de saúde ou medicamentos de uso contínuo\n(deixe em branco se não houver)",
    font=fonte_label, bg="#FFF6E5", fg=COR_CINZA_ESCURO, anchor="w", justify="left"
).grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 5))

texto_saude = tk.Text(frame_saude, width=52, height=4, font=fonte_campo, relief="solid", bd=1)
texto_saude.grid(row=3, column=0, columnspan=2, pady=(0, 5))

# ---------- Bloco do responsável (aparece só se menor de idade) ----------
frame_responsavel = tk.Frame(frame_scrollavel, bg="#FCE9E9", padx=20, pady=15, bd=1, relief="solid")

label_aviso_resp = tk.Label(
    frame_responsavel,
    text="⚠ Aluno menor de idade — dados do responsável obrigatórios",
    font=("Arial", 10, "bold"),
    bg="#FCE9E9", fg=COR_VERMELHO
)
label_aviso_resp.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

criar_label(frame_responsavel, "Nome do responsável", 1)
entry_nome_resp = tk.Entry(frame_responsavel, width=35, font=fonte_campo, relief="solid", bd=1)
entry_nome_resp.grid(row=1, column=1, pady=8)

criar_label(frame_responsavel, "Telefone do responsável", 2)
entry_tel_resp = tk.Entry(frame_responsavel, width=35, font=fonte_campo, relief="solid", bd=1)
entry_tel_resp.grid(row=2, column=1, pady=8)

confirmacao_var = tk.BooleanVar()
check_confirmacao = tk.Checkbutton(
    frame_responsavel,
    text="Confirmo que este cadastro está sendo feito com autorização do responsável legal",
    variable=confirmacao_var,
    bg="#FCE9E9", fg=COR_CINZA_ESCURO,
    font=("Arial", 9), wraplength=480, justify="left",
    activebackground="#FCE9E9"
)
check_confirmacao.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))

# ---------- Botões ----------
frame_botoes = tk.Frame(frame_scrollavel, bg=COR_CINZA_CLARO, pady=10)
frame_botoes.pack(fill="x")

botao_adicionar = tk.Button(
    frame_botoes, text="Adicionar", command=adicionar_aluno,
    width=15, font=("Arial", 10, "bold"),
    bg=COR_VERMELHO, fg=COR_BRANCO,
    activebackground="#C4141C", activeforeground=COR_BRANCO,
    relief="flat", cursor="hand2"
)
botao_adicionar.pack(side="left", padx=20)

botao_limpar = tk.Button(
    frame_botoes, text="Limpar lista", command=limpar_lista,
    width=15, font=("Arial", 10, "bold"),
    bg=COR_CINZA_ESCURO, fg=COR_BRANCO,
    activebackground="#1A1A1A", activeforeground=COR_BRANCO,
    relief="flat", cursor="hand2"
)
botao_limpar.pack(side="left")

# ---------- Lista de alunos ----------
frame_lista = tk.Frame(frame_scrollavel, bg=COR_CINZA_CLARO, padx=20, pady=10)
frame_lista.pack(fill="both", expand=True)

label_lista = tk.Label(
    frame_lista, text="Alunos cadastrados", font=("Arial", 11, "bold"),
    bg=COR_CINZA_CLARO, fg=COR_CINZA_ESCURO, anchor="w"
)
label_lista.pack(fill="x", pady=(0, 5))

frame_listbox = tk.Frame(frame_lista, bd=1, relief="solid")
frame_listbox.pack(fill="both", expand=True)

scrollbar_lista = tk.Scrollbar(frame_listbox)
scrollbar_lista.pack(side="right", fill="y")

lista_alunos = tk.Listbox(
    frame_listbox, yscrollcommand=scrollbar_lista.set,
    font=("Arial", 9), bg=COR_BRANCO, fg=COR_CINZA_ESCURO,
    selectbackground=COR_VERMELHO, selectforeground=COR_BRANCO,
    relief="flat", bd=0, height=8
)
lista_alunos.pack(fill="both", expand=True)

scrollbar_lista.config(command=lista_alunos.yview)

entry_nome.focus()

janela.mainloop()
