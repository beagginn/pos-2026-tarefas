from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

id_prato = 0
for prato in pratos:
    id_prato += 1
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    print(f'{id_prato} - {nome}')

id_lido = int(input("Digite o id do prato para saber mais: "))
prato = pratos[id_lido-1]

elemento_nome = prato.getElementsByTagName('nome')[0]
nome = elemento_nome.firstChild.nodeValue
elemento_descricao = prato.getElementsByTagName('descricao')[0]
descricao = elemento_descricao.firstChild.nodeValue
elemento_preco = prato.getElementsByTagName('preco')[0]
preco = elemento_preco.firstChild.nodeValue
elemento_calorias = prato.getElementsByTagName('calorias')[0]
calorias = elemento_calorias.firstChild.nodeValue

print("nome:", nome)
print("descrição:", descricao)
print("preço:", preco)
print("calorias:", calorias)