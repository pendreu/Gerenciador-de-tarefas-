def show_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar nova tarefa")
    print("2. Ver todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    print("------------------------------")

def add_task(tasks):
    """Adiciona uma nova tarefa à lista."""
    task = input("Digite a nova tarefa: ")
    tasks.append({"task": task, "completed": False})
    print(f"Tarefa '{task}' adicionada com sucesso.")

def view_tasks(tasks):
    """Exibe a lista de tarefas, mostrando o status de cada uma."""
    if not tasks:
        print("Nenhuma tarefa na lista.")
    else:
        print("\n--- Suas Tarefas ---")
        for i, item in enumerate(tasks):
            status = "✅" if item["completed"] else "❌"
            print(f"{i+1}. {status} {item['task']}")
        print("--------------------")

def complete_task(tasks):
    """Marca uma tarefa como concluída."""
    view_tasks(tasks)
    try:
        task_num = int(input("Digite o número da tarefa a ser concluída: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def remove_task(tasks):
    """Remove uma tarefa da lista."""
    view_tasks(tasks)
    try:
        task_num = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Tarefa '{removed_task['task']}' removida com sucesso.")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def main():
    """Função principal que gerencia o fluxo do programa."""
    tasks = []
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()