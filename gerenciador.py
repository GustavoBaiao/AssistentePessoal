import datetime

class Usuario:
    def __init__(self, nome, senha, admin=False):
        self.nome = nome
        self.senha = senha
        self.admin = admin

class Tarefa:
    def __init__(self, titulo, responsavel, data_fim):
        self.titulo = titulo
        self.responsavel = responsavel
        self.data_fim = data_fim
        self.concluida = False

    def finalizar(self, senha):
        if senha == self.responsavel.senha:
            self.concluida = True
            return True
        else:
            return False

class GerenciadorTarefas:
    def __init__(self):
        self.usuarios = []
        self.tarefas = []

    def adicionar_usuario(self, nome, senha, admin=False):
        usuario = Usuario(nome, senha, admin)
        self.usuarios.append(usuario)

    def adicionar_tarefa(self, titulo, responsavel_nome, data_fim):
        responsavel = next((usuario for usuario in self.usuarios if usuario.nome == responsavel_nome), None)
        if responsavel:
            tarefa = Tarefa(titulo, responsavel, data_fim)
            self.tarefas.append(tarefa)
        else:
            print("Responsável pela tarefa não encontrado.")

    def remover_tarefa(self, titulo, usuario_nome, senha):
        usuario = next((usuario for usuario in self.usuarios if usuario.nome == usuario_nome), None)
        if usuario and usuario.admin and senha == usuario.senha:
            for i, tarefa in enumerate(self.tarefas):
                if tarefa.titulo == titulo:
                    del self.tarefas[i]
                    break
        else:
            print("Apenas administradores podem remover tarefas.")

    def mostrar_tarefas(self, status):
        if status == "ativas":
            tarefas = [tarefa for tarefa in self.tarefas if not tarefa.concluida]
        elif status == "concluidas":
            tarefas = [tarefa for tarefa in self.tarefas if tarefa.concluida]
        else:
            tarefas = self.tarefas

        for tarefa in tarefas:
            print(f"Título: {tarefa.titulo}, Responsável: {tarefa.responsavel.nome}, Data de término: {tarefa.data_fim}, Concluída: {tarefa.concluida}")

    def finalizar_tarefa(self, titulo, usuario_nome, senha):
        usuario = next((usuario for usuario in self.usuarios if usuario.nome == usuario_nome), None)
        if usuario and senha == usuario.senha:
            for tarefa in self.tarefas:
                if tarefa.titulo == titulo and tarefa.responsavel.nome == usuario_nome:
                    return tarefa.finalizar(senha)
        return False

    def mostrar_usuarios(self, usuario_nome, senha):
        usuario = next((usuario for usuario in self.usuarios if usuario.nome == usuario_nome), None)
        if usuario and usuario.admin and senha == usuario.senha:
            for usuario in self.usuarios:
                print(f"Nome: {usuario.nome}, Administrador: {usuario.admin}")
        else:
            print("Apenas administradores podem ver os usuários cadastrados.")
