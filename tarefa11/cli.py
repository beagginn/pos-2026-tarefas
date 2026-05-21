import users_wrapper as users

while True:
    print("\nMENU")
    print("1 - listar usuários")
    print("2 - detalhar usuário")
    print("3 - criar usuário")
    print("4 - editar usuário")
    print("5 - remover usuário")
    print("6 - sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        users_list = users.list()

        if users_list:
            print("\nlista de usuários:")
            for user in users_list:
                print(f"{user['id']} - {user['name']}")
        else:
            print("erro ao listar usuários.")

    elif opcao == "2":
        user_id = input("digite o ID do usuário: ")

        user = users.read(user_id)

        if user:
            print("\nDetalhes do usuário:")
            print(f"nome: {user['name']}")
            print(f"email: {user['email']}")
            print(f"telefone: {user['phone']}")
        else:
            print("usuário não encontrado.")

    elif opcao == "3":
        name = input("nome: ")
        email = input("email: ")
        phone = input("telefone: ")

        user = users.create(name, email, phone)

        if user:
            print("usuário criado com sucesso!")
        else:
            print("erro ao criar usuário.")

    elif opcao == "4":
        user_id = input("ID do usuário: ")

        name = input("novo nome: ")
        email = input("novo email: ")
        phone = input("novo telefone: ")

        user = users.update(user_id, name, email, phone)

        if user:
            print("usuário atualizado com sucesso!")
        else:
            print("erro ao atualizar usuário.")

    elif opcao == "5":
        user_id = input("ID do usuário: ")

        success = users.delete(user_id)

        if success:
            print("usuário removido com sucesso!")
        else:
            print("erro ao remover usuário.")

    elif opcao == "6":
        print("tchau...")
        break

    else:
        print("opção inválida.")