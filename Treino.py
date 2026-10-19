import mysql.connector 
import requests

#Conexão com o banco de dados
mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="(Paparoch12345",
    database="projeto"
)

#Printando no terminal se a conexão deu certo! 
print(mydb)         

#Valor de entrada CEP para passarmos a função buscarcep
a = input("Digite seu cep: ")

#Função buscar cep, buscando as requisições que vamos colocar no banco de dados usando api de CEP pública
def buscarcep(cep1): 
    
    #Requisição get para pegar os valores do CEP
    buscacep = requests.get(f"https://viacep.com.br/ws/{cep1}/json/")
    
    #Usando json para conseguirmos requsitar linhas especificas da API
    dados = buscacep.json()
    
    #Dicionário para definir em uma única váriavel todas as requisições que precisamos
    endereco = {
    "cep": dados["cep"],
    "logradouro": dados["logradouro"],
    "bairro": dados["bairro"],
    "cidade": dados["localidade"],
    "uf": dados["uf"],
    }
    
    #Retornando a váriavel que vai nos mostrar os resultados obtidos do CEP 
    return endereco

#Váriavel para execurtamos nossos comandos SQL 
mycursor = mydb.cursor()

#Insert para enviarmos as informações obtidas do CEP da pessoa para o banco de dados já criado
sql = "INSERT INTO enderecos (cep, logradouro, bairro, cidade, uf) VALUES(%(cep)s, %(logradouro)s, %(bairro)s, %(cidade)s, %(uf)s)"

#recebendo a função buscarcep com CEP da pessoa que enviou
endereco = buscarcep(a)

#Executando o SQL assim enviando os dados
mycursor.execute(sql,endereco)

#Confirmação dos comandos enviados para o SQL 
mydb.commit()

#Segunda verificação para saber se o CEP foi mostrado corretamente
print(buscarcep(a))