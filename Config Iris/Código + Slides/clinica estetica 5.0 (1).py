import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class ClinicaEsteticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agendamento de Serviços Estéticos")
        self.root.geometry("700x600")
        self.root.config(bg="#E1F7D5")

        # Lista de serviços
        self.servicos = [
            ("1", "Botox", 500.00),
            ("2", "Massagem Modeladora", 120.00),
            ("3", "Massagem Relaxante", 80.00),
            ("4", "Limpeza de Pele", 150.00),
            ("5", "Design de Sobrancelhas", 50.00),
            ("6", "Tratamento para Acne", 200.00),
            ("7", "Reconstrução Capilar", 100.00),
            ("8", "Depilação a Laser", 250.00),
            ("9", "Depilação a Cera", 100.00),
            ("10", "Drenagem Linfática", 200.00)
        ]

        self.clientes = []  # Lista para armazenar os clientes
        self.agendamentos = []  # Lista para armazenar os agendamentos

        # Criando o Notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, padx=10, expand=True)

        # Criando abas
        self.cadastro_frame = tk.Frame(self.notebook, bg="#E1F7D5", padx=20, pady=20)
        self.visualizacao_frame = tk.Frame(self.notebook, bg="#E1F7D5", padx=20, pady=20)

        self.notebook.add(self.cadastro_frame, text="Cadastro de Cliente")
        self.notebook.add(self.visualizacao_frame, text="Visualizar Agendamentos")

        # Criar telas
        self.criar_tela_cadastro_cliente()
        self.criar_tela_visualizar_agendamentos()

    def criar_tela_cadastro_cliente(self):
        # Título
        self.titulo_label = tk.Label(self.cadastro_frame, text="Cadastro de Cliente", font=("Arial", 18, "bold"), bg="#E1F7D5")
        self.titulo_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos de cadastro de cliente
        self.nome_label = tk.Label(self.cadastro_frame, text="Nome:", font=("Arial", 12), bg="#E1F7D5")
        self.nome_label.grid(row=1, column=0, pady=5, sticky="e")
        self.nome_entry = tk.Entry(self.cadastro_frame, font=("Arial", 12), bg="#F1F1F1")
        self.nome_entry.grid(row=1, column=1, pady=5)

        self.telefone_label = tk.Label(self.cadastro_frame, text="Telefone:", font=("Arial", 12), bg="#E1F7D5")
        self.telefone_label.grid(row=2, column=0, pady=5, sticky="e")
        self.telefone_entry = tk.Entry(self.cadastro_frame, font=("Arial", 12), bg="#F1F1F1")
        self.telefone_entry.grid(row=2, column=1, pady=5)

        self.email_label = tk.Label(self.cadastro_frame, text="E-mail:", font=("Arial", 12), bg="#E1F7D5")
        self.email_label.grid(row=3, column=0, pady=5, sticky="e")
        self.email_entry = tk.Entry(self.cadastro_frame, font=("Arial", 12), bg="#F1F1F1")
        self.email_entry.grid(row=3, column=1, pady=5)

        # Botão de Cadastro
        self.cadastrar_button = tk.Button(self.cadastro_frame, text="Cadastrar Cliente", font=("Arial", 14), bg="#58D68D", command=self.cadastrar_cliente)
        self.cadastrar_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Dropdown para selecionar serviço e forma de pagamento
        self.servico_label = tk.Label(self.cadastro_frame, text="Selecione o Serviço:", font=("Arial", 12), bg="#E1F7D5")
        self.servico_label.grid(row=5, column=0, pady=5, sticky="e")
        self.servico_combobox = ttk.Combobox(self.cadastro_frame, values=[f"{codigo} - {nome}" for codigo, nome, _ in self.servicos], font=("Arial", 12))
        self.servico_combobox.grid(row=5, column=1, pady=5)

        self.pagamento_label = tk.Label(self.cadastro_frame, text="Forma de Pagamento:", font=("Arial", 12), bg="#E1F7D5")
        self.pagamento_label.grid(row=6, column=0, pady=5, sticky="e")
        self.pagamento_combobox = ttk.Combobox(self.cadastro_frame, values=["Dinheiro", "Cartão", "Pix"], font=("Arial", 12))
        self.pagamento_combobox.grid(row=6, column=1, pady=5)

        # Botão para agendar o serviço
        self.agendar_button = tk.Button(self.cadastro_frame, text="Agendar Serviço", font=("Arial", 14), bg="#58D68D", command=self.agendar_servico)
        self.agendar_button.grid(row=7, column=0, columnspan=2, pady=20)

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()

        if not nome or not telefone or not email:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        cliente = {"nome": nome, "telefone": telefone, "email": email}
        self.clientes.append(cliente)
        messagebox.showinfo("Cadastro", f"Cliente {nome} cadastrado com sucesso!")

        # Limpar campos após cadastro
        self.nome_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def agendar_servico(self):
        nome_cliente = self.nome_entry.get()
        servico_selecionado = self.servico_combobox.get()
        pagamento = self.pagamento_combobox.get()

        if not nome_cliente or not servico_selecionado or not pagamento:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        # Verificando o serviço selecionado
        codigo_servico = servico_selecionado.split(" ")[0]
        servico = next((s for s in self.servicos if s[0] == codigo_servico), None)

        if servico:
            servico_nome = servico[1]
            servico_preco = servico[2]
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            agendamento = {
                "cliente": nome_cliente,
                "servico": servico_nome,
                "preco": servico_preco,
                "pagamento": pagamento,
                "data_hora": data_hora
            }
            self.agendamentos.append(agendamento)
            messagebox.showinfo("Agendamento Confirmado", f"Agendamento realizado com sucesso para {nome_cliente}!")
        else:
            messagebox.showerror("Erro", "Serviço não encontrado!")

    def criar_tela_visualizar_agendamentos(self):
        # Título
        self.agenda_label = tk.Label(self.visualizacao_frame, text="Visualizar Agendamentos", font=("Arial", 18, "bold"), bg="#E1F7D5")
        self.agenda_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Tabela de Agendamentos
        self.agendamentos_tree = tk.Listbox(self.visualizacao_frame, height=10, width=50, font=("Arial", 12))
        self.agendamentos_tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botão para mostrar agendamentos
        self.mostrar_agendamentos_button = tk.Button(self.visualizacao_frame, text="Mostrar Agendamentos", font=("Arial", 14), bg="#58D68D", command=self.mostrar_agendamentos)
        self.mostrar_agendamentos_button.grid(row=2, column=0, columnspan=3, pady=20)

    def mostrar_agendamentos(self):
        # Limpar listbox antes de mostrar os agendamentos
        self.agendamentos_tree.delete(0, tk.END)

        if not self.agendamentos:
            messagebox.showinfo("Sem Agendamentos", "Nenhum agendamento foi feito ainda!")
            return

        # Exibir todos os agendamentos na Listbox
        for agendamento in self.agendamentos:
            self.agendamentos_tree.insert(tk.END, f"Cliente: {agendamento['cliente']} | Serviço: {agendamento['servico']} | "
                                                 f"Data: {agendamento['data_hora']} | Pagamento: {agendamento['pagamento']} | "
                                                 f"Preço: R${agendamento['preco']:.2f}")

# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ClinicaEsteticaApp(root)
    root.mainloop()
