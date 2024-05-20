from gerenciador import GerenciadorTarefas
import datetime

gerenciador = GerenciadorTarefas()

def menu():
    print("1. Adicionar usuário")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Mostrar tarefas")
    print("5. Finalizar tarefa")
    print("6. Mostrar usuários")
    print("7. Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        admin = None
        while admin not in ("s", "n"):
            admin = input("O usuário é administrador? (s/n): ")
        admin = admin == "s"
        gerenciador.adicionar_usuario(nome, senha, admin)
    elif opcao == "2":
        titulo = input("Digite o título da tarefa: ")
        responsavel_nome = input("Digite o nome do responsável pela tarefa: ")
        data_fim = datetime.datetime.now() + datetime.timedelta(days=int(input("Digite o número de dias até o fim da tarefa: ")))
        gerenciador.adicionar_tarefa(titulo, responsavel_nome, data_fim)
    elif opcao == "3":
        titulo = input("Digite o título da tarefa a ser removida: ")
        usuario_nome = input("Digite o nome do usuário que está removendo a tarefa: ")
        senha = input("Digite a senha do usuário: ")
        gerenciador.remover_tarefa(titulo, usuario_nome, senha)
    elif opcao == "4":
        status = None
        while status not in ("ativas", "concluidas", "todas"):
            status = input("Você quer ver tarefas ativas, concluídas ou todas? ")
        gerenciador.mostrar_tarefas(status)
    elif opcao == "5":
        titulo = input("Digite o título da tarefa a ser finalizada: ")
        usuario_nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        if not gerenciador.finalizar_tarefa(titulo, usuario_nome, senha):
            print("Usuário ou senha incorretos. Tarefa não finalizada.")
    elif opcao == "6":
        usuario_nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        gerenciador.mostrar_usuarios(usuario_nome, senha)
    elif opcao == "7":
        break
    else:
        print("Opção inválida. Tente novamente.")


