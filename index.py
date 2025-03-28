def show_contacts(contacts):
  print("\nLista de contatos:")
  for index, contact in enumerate(contacts):
    favorite = "☆" if contact["favorite"] else " "
    print(f"{index + 1}. [{favorite}] {contact["name"]} - {contact["cellphone"]} - {contact["email"]}")
  return

def get_infos():
  name = input("Qual o nome do contato? ")
  cellphone = input("Qual o telefone do contato? ")
  email = input("Qual o e-mail do contato? ")
  favorite = True if input("Quer salvar o contato em favoritos (s/n) ") == "s" else False
  return name, cellphone, email, favorite

def add_contact(contacts, name, cellphone, email, favorite):
  contact = {
    "name": name,
    "cellphone": cellphone,
    "email": email,
    "favorite": favorite,
  }
  contacts.append(contact)
  print(f"O contato {name} foi adicionado à lista.")
  return

def show_contact(contact):
  def handle_key(key):
    if key == "name":
      return "Nome"
    elif key == "cellphone":
      return "Celular/Telefone"
    elif key == "email":
      return "E-mail"
    else:
      return "Favoritar/Desfavoritar"

  print("\n Informações do contato:")
  print(contact)
  for index, infos in enumerate(list(contact[0].items())):
    adjusted_index = index + 1
    print(f"{adjusted_index}. {handle_key(infos[0])} - {infos[1]}")
  return

def edit_contact(contacts):
  show_contacts(contacts)
  contact_index = int(input("\nQual o número do contato que deseja editar? "))
  contact_adjusted_index = contact_index - 1
  show_contact(contacts[contact_adjusted_index])
  chosen_information = input("\nQual informação deseja editar? ")
  if chosen_information == "1":
    edited_name = input("Como deseja salvar o nome agora? ")
    contacts[contact_adjusted_index]["name"] = edited_name
    print(f"O nome do contato foi alterado para {edited_name}")
  if chosen_information == "2":
    edited_cellphone = input("Como deseja salvar o número agora? ")
    contacts[contact_adjusted_index]["cellphone"] = edited_cellphone
    print(f"O número do contato foi alterado para {edited_cellphone}")
  if chosen_information == "3":
    edited_email = input("Como deseja salvar o e-mail agora? ")
    contacts[contact_adjusted_index]["email"] = edited_email
    print(f"O e-mail do contato foi alterado para {edited_email}")
  if chosen_information == "4":
    edited_favorite = input("Quer favoritar o contato? (s/n): ")
    if edited_favorite == "s":
      contacts[contact_adjusted_index]["favorite"] = True
      print("O contato foi marcado como favorito")
    elif edited_favorite == "n":
      contacts[contact_adjusted_index]["favorite"] = False
      print("O contato foi removido dos favoritos")
    else:
      print("Ação inválida!")
      return
  return

def mark_contact_as_favorite(contacts) :
  show_contacts(contacts)
  contact_index = int(input("\nDeseja modificar o favoritismo de qual contato? "))
  contact_adjusted_index = contact_index - 1
  contact_name = contacts[contact_adjusted_index]["name"]
  if contacts[contact_adjusted_index]["favorite"] == True:
    response = input(f"{contact_name} está na lista de favoritos, deseja removê-lo? (s/n) ")
    if response == "s":
      contacts[contact_adjusted_index]["favorite"] = False
      print(f"{contact_name} foi removido dos favoritos com sucesso")
      return
    if response == "n":
      contacts[contact_adjusted_index]["favorite"] = True
      print("Ação cancelada com sucesso")
      return
    else:
      print("Resposta inválida!")
      return
  if contacts[contact_adjusted_index]["favorite"] == False:
    response = input(f"{contact_name} NÃO está na lista de favoritos, deseja adicioná-lo? (s/n) ")
    if response == "s":
      contacts[contact_adjusted_index]["favorite"] = True
      print(f"{contact_name} foi adicionado como favorito!")
      return
    if response == "n":
      contacts[contact_adjusted_index]["favorite"] = False
      print("Ação cancelada com sucesso")
      return
    else:
      print("Resposta inválida!")
      return
  return

contacts = []
while True:
  print("\nMenu da Lista de Contatos")
  print("1. Visualizar lista de contatos")
  print("2. Adicionar um contato")
  print("3. Editar contato")
  print("4. Marcar/desmarcar um contato como favorito")
  print("5. Visualizar contatos favoritos")
  print("6. Apagar um contato")
  print("7. Sair do Aplicação")

  choice = input("\nEscolha uma ação: ")

  if choice == "1":
    show_contacts(contacts)

  if choice == "2":
    name, cellphone, email, favorite = get_infos()
    add_contact(contacts, name, cellphone, email, favorite)

  if choice == "3":
    edit_contact(contacts)

  if choice == "4":
    mark_contact_as_favorite(contacts)

  elif choice == "7":
    break