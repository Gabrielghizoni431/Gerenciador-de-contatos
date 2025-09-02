import os
lista_Contatos=[]

def adicionar_contato(lista,nome):
    if nome.strip()=="":
      print("Nome nao pode estar em branco")
    else:
     lista.append(nome)
     print("Contato adicionado com sucesso!!!!")

def remover_contato(lista,nome):
   if nome.strip()=="":
      print("Nome nao pode estar em branco")
   if nome in lista : 
    lista.remove(nome)
    print("Contato apagado com sucesso!!!!")
   else:
      print("Contato nao encotrado na lista, tente novamente: ")
      


def menu():
  print("=== MENU ===")
  print("1- Adicionar contato")
  print("2- Remover contato")
  print("3- Buscar contato")
  print("4- Mostrar contatos")
  print("5- sair")


def mostrar_contatos(lista):
  if not lista :
      print("Nenhum Contato foi cadastrado!!!!")
  else:
    for i, contato  in enumerate (lista, start=1):
           print(f"{i} - {contato}")



def buscar_contatos(lista,nome):
  if nome.strip()=="":
      print("Nome nao pode estar em branco")
  while True:
    if nome in lista:
      indice=lista.index(nome)
      print(f"{indice + 1} - {lista[indice]}")
      
      break
    else:
      print("Nome nao encotrado na lista, tente novamente: ")
      nome = input("Qual nome voce quer na lista: ")


sair = 0
menus=0
while True:
 if menus==0:
   os.system("cls")
   menu()
   esco=int(input("Digite o numero que deseja: "))
   menus=1
  


 if esco == 1:
   os.system("cls")
   parar=1
   print("=== Adicionar contato ===")
   while parar!=0:
    
    novo_contato=input("Digite o nome do contato: ")
    adicionar_contato(lista_Contatos,novo_contato)
    parar=int(input("Digite 0 para finalizar e 1 para continuar: "))
    if parar ==0:
      esco = 0
      menus=0



 elif esco==2:
    os.system("cls")
    parar=1
    print("=== Remover contato ===")
    while parar!=0:
     mostrar_contatos(lista_Contatos)
     apagar_contato=input("Qual contato voce quer apagar? ")
     remover_contato(lista_Contatos,apagar_contato)
     parar =int(input("Digite 1 para continuar e 0 para finalizar: "))
     if parar ==0:
      esco=0
      menus=0
    

 elif esco==3:
   os.system("cls")
   parar =1 
   print("=== Buscar contato ===")
   while parar!=0:
    nome_na_lista=input("Qual nome voce quer na lista: ")
    buscar_contatos(lista_Contatos,nome_na_lista)
    parar= int(input("Digite 1 para continuar e 0 para finalizar: "))
    if parar ==0:
     esco=0
     menus=0



 elif esco==4:
   os.system("cls")
   print("=== Mostrar contatos ===")
   mostrar_contatos(lista_Contatos)
   parar= int(input("Digite 1 para continuar e 0 para finalizar: "))
   if parar ==0:
     esco=0
     menus=0
    
 elif esco==5:
   os.system("cls")
   break
