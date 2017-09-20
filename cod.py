arquivo = open('texto.txt', 'r')
conteudo = arquivo.readlines()
texto = []

nome = input("Informe seu nome: ")
rua = input("Informe seu endereço (Rua): ") 
cep = int(input("Informe seu endereço (CEP): "))
bairro =input("Informe seu endereço (Bairro): ") 
estado = input("Informe seu Estado: ")
telefone = int(input("Informe seu telefone: "))
def ad():
    arquivo = open('texto.txt', 'w')
    conteudo.append("%s"%nome)
    texto.append("%s"%nome)
    conteudo.append("%s, %i, %s, %s"%(rua, cep, bairro, estado))
    texto.append("%s, %i, %s, %s"%(rua, cep, bairro, estado))
    conteudo.append("%i"%telefone)
    texto.append("%i"%telefone)
    arquivo.writelines(conteudo)
    arquivo.close()
    

ad()
         
def consulta():
        pos = input("Qual o nome?: ")
        for i in texto:
            if (pos == i):
                return (pos)

pergunta = input("Você deseja consultar? (s,n)")
if (pergunta == "s" or pergunta == "S"):
    print(consulta())
