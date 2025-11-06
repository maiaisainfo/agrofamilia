def verificar_senha(s, c):
    if s != c:
        return True
    else:
        return False

usuarios = [ ]
produtos= [ ]
escolha = 43455653

while escolha != '0':
    print ('Bem-Vindo ao Fazenda Agro!')
    print ('.......MENU PRINCIPAL.......')
    print('1-Cadastrar familia\n2-Fazer login\n3-Vizualizar produtos de todas as famílias\n4-Vizualizar lista de usuários cadastrados\n0-Sair  ')
    escolha = input('Digite a opção escolhida: ')

    if escolha == '1':
        cpf = input('Digite seu CPF: ')
        nome =input ('Digite seu nome: ')
        senha= input ('Digite a senha: ')
        confirmacao = input('Digite a confirmacao da senha: ')
        while verificar_senha (senha, confirmacao):
            senha = input('Digite a senha: ')
            confirmacao = input('Digite a confirmacao da senha: ')
        print ('Deu certo!')



    elif escolha == '4':
        print(usuarios)
        if len(usuarios) == 0:
            print('Nenhum usuário cadastrado ainda.')

    elif escolha == '2':
        cpf = input('Digite seu CPF: ')
        senha = input('Digite sua senha: ').lower()
        log_ok= False
        for usu in usuarios:
            if cpf== usu [1] and senha == usu [2]:
                log_ok= True
                break



        op = 353434
        if log_ok:

             while op != '0':
                print('.......MENU INTERNO.......')
                print('1-Inserir produto\n2-Remover produto\n3-Mostrar lista de produtos cadastrados\n4- Editar produtos cadastrados\n0-sair')
                op = input('Digite a opção escolhida: ')

                if op =='1':
                    prod= input('Digite o nome do produto: ')
                    quant = input('Digite a quantidade disponível do produto: ')
                    valor = input('Digite o valor do produto: ')
                    produtos.append ([prod,quant,valor, usuarios[0][1]])

                elif op== '3':
                    for pro in produtos:
                        if cpf == pro [3]:
                            print (produtos)

                elif op=='2':
                    for itens in range (len (produtos)):
                        print (itens, 'Nome do produto:', produtos [itens][0])
                    indice= int (input ('Digite o índice do produto escolhido: '))
                    produtos.pop (indice)

                elif op== '4':
                        for p in range (len(produtos)):
                            print(p, 'Nome do produto:', produtos[p][0])
                        indice = int(input('Digite o índice do produto escolhido: '))
                        produtos[indice][0] = input('Digite o nome do produto: ')
                        produtos[indice][1] = input('Digite a quantidade do produto: ')
                        produtos[indice][2] = input('Digite o valor do produto: ')

                elif op== '0':
                    print ('Saindo do menu interno...')

             else:
                 print('Acesso negado.Cadastre-se em nosso sistema ou insira seus dados corretamente.')



































