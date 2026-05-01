from xml.dom.minidom import parse
import json

def get_text(parent, tag):
    elems = parent.getElementsByTagName(tag)
    if elems and elems[0].firstChild:
        return elems[0].firstChild.nodeValue.strip()
    return None

dom = parse('imobiliaria.xml')
imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')
lista = []

for imovel in imoveis:
    descricao = get_text(imovel, "descricao")

    endereco_tag = imovel.getElementsByTagName("endereco")[0]
    rua = get_text(endereco_tag, "rua")
    numero = get_text(endereco_tag, "numero")
    bairro = get_text(endereco_tag, "bairro")
    cidade = get_text(endereco_tag, "cidade")

    proprietario_tag = imovel.getElementsByTagName("proprietario")[0]
    nome = get_text(proprietario_tag, "nome")
    email = get_text(proprietario_tag, "email")

    telefones_tags = proprietario_tag.getElementsByTagName("telefone")
    telefones = []
    for tel in telefones_tags:
        if tel.firstChild:
            telefones.append(tel.firstChild.nodeValue.strip())

    caracteristicas_tag = imovel.getElementsByTagName("caracteristicas")[0]
    tamanho = get_text(caracteristicas_tag, "tamanho")
    numQuartos = get_text(caracteristicas_tag, "numQuartos")
    numBanheiros = get_text(caracteristicas_tag, "numBanheiros")

    valor = get_text(imovel, "valor")

    lista.append({
        "descricao": descricao,
        "endereco": {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade
        },
        "proprietario": {
            "nome": nome,
            "email": email,
            "telefones": telefones
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    })

dados = {
    "imobiliaria": {
        "imoveis": lista
    }
}

with open('imobiliaria.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f)
