import json

with open("imobiliaria.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

imoveis = dados["imobiliaria"]["imoveis"]

for i, imovel in enumerate(imoveis, start=1):
    print(f"{i} - {imovel['descricao']}")

id_lido = int(input("\ndigite o ID do imóvel para ver mais detalhes: "))

imovel = imoveis[id_lido - 1]

print("\n- detalhes do imóvel\n")

print("descrição:", imovel["descricao"])
print("valor: R$", imovel["valor"])

end = imovel["endereco"]
print("\nendereço:")
print(" rua:", end["rua"])
print(" número:", end["numero"])
print(" bairro:", end["bairro"])
print(" cidade:", end["cidade"])

prop = imovel["proprietario"]
print("\nproprietário:")
print(" nome:", prop["nome"])
print(" email:", prop["email"])

print(" telefones:")
for tel in prop["telefones"]:
    print("  -", tel)

car = imovel["caracteristicas"]
print("\ncaracterísticas:")
print(" tamanho:", car["tamanho"])
print(" quartos:", car["numQuartos"])
print(" banheiros:", car["numBanheiros"])