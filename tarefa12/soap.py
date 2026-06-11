
import requests
from xml.dom.minidom import parseString
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

op = input("digite um para a o código telefônico, dois para a bandeira e tres para o nome do país: ")
if op == '1':
    operation = "CountryIntPhoneCode"
elif op == '2':
    operation = "CountryFlag"
elif op == '3':    
    operation = "CountryName"
else:
    print("inválido")
    exit()

country_code = input("digite o código do país: ").upper()

# XML estruturado
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{operation}} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{operation}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
print(response.text)
print(response)

if response.status_code == 200:
    if op == '1':
        print("o código telefônico do país é:" + parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue)
    elif op == '2':
        print("a bandeira do país é:" + parseString(response.text).documentElement.getElementsByTagName("m:CountryFlagResult")[0].firstChild.nodeValue)
    elif op == '3':
        print("o nome do país é:" + parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue)