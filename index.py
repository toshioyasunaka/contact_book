while True:
  print("\nMenu da Lista de Contatos")
  print("1. Visualizar lista de contatos")
  print("2. Editar contato")
  print("3. Marcar/desmarcar um contato como favorito")
  print("4. Visualizar contatos favoritos")
  print("5. Apagar um contato")
  print("6. Sair do Aplicação")

  choice = input("\nEscolha uma ação: ")
  contacts = []

  if choice == "1":
    print("\nLista de contatos:")
    print(contacts)

  elif choice == "6":
    break