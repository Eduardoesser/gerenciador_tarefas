# Lista onde vamos guardar as tarefas (cada tarefa será um dicionário)
tarefas = []

# Função que mostra o menu principal do programa
def mostrar_menu():
    print("\n=== Menu ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")
    print("4. Marcar tarefa como concluida")  # Adicionamos essa opção

# Função que mostra as tarefas cadastradas
def mostrar_tarefas():
    # Se a lista estiver vazia, avisamos o usuário
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("\n=== Lista de Tarefas ===")
        # Usamos enumerate para numerar as tarefas, começando do 1
        for i, tarefa in enumerate(tarefas, start=1):
            # Mostramos um emoji de acordo com o status da tarefa
            status = "✅" if tarefa["concluida"] else "❌"
            # Mostramos o número, título e status da tarefa
            print(f"{i}. {tarefa['titulo']} - {status}")

def marcar_tarefa_concluida():
    mostrar_tarefas()  # Mostra as tarefas pro usuário escolher
    if not tarefas:
        return  # Se a lista estiver vazia, sai da função

    try:
        numero = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Loop principal do programa, que mantém o menu ativo até o usuário sair
while True:
    mostrar_menu()  # Exibe o menu
    escolha = input("Escolha uma opção: ")  # Lê a opção digitada

    # Se o usuário escolher "1", vamos adicionar uma nova tarefa
    if escolha == "1":
        titulo = input("Digite a tarefa: ")  # Lê o título da tarefa
        # Criamos a tarefa como um dicionário com título e status
        tarefa = {"titulo": titulo, "concluida": False}
        tarefas.append(tarefa)  # Adicionamos à lista
        print("Tarefa adicionada com sucesso!")

    # Se o usuário escolher "2", mostramos a lista de tarefas
    elif escolha == "2":
        mostrar_tarefas()

    # Se o usuário escolher "3", saímos do programa
    elif escolha == "3":
        print("Saindo...")
        break  # Interrompe o loop e encerra o programa

    elif escolha == "4":
        marcar_tarefa_concluida()


    # Caso a opção não seja válida, avisamos o usuário
    else:
        print("Opção inválida. Tente novamente.")


