import zeep

wsdl = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl"

client = zeep.Client(wsdl=wsdl)

numero = input("Digite um número para converter: ")

result = client.service.NumberToWords(ubiNum=numero)

print(f"O número {numero} em palavras é: {result}")