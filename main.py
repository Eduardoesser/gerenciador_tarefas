# main.py

tarefas = []  # Aqui vamos guardar as tarefas

def mostrar_menu():
    print("\n=== Menu ===")
    print("1. Adicionar tarefa")
    print("2. Sair")
    print("3. Listar tarefas")  # ← essa é a nova opção

# Loop principal
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
        
    elif escolha == "3":
        if tarefas:
            print("\n=== Tarefas ===")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
        else:
            print("Nenhuma tarefa cadastrada.")

    elif escolha == "2":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
