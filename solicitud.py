import requests

bandera = True
bandera2 = True

codigosMoneda = ["USD", "EUR", "JPY", "COP", "BRL", "CAD", "MXN", "ARS"]
print(f"Monedas Disponibles: {codigosMoneda}")

inputCode, inputCode2 = None, None

while bandera:
    inputCode = input("Ingrese el codigo de la moneda base: ").strip().upper() # Añade mayuscula justo cuando termina el input
    if inputCode in codigosMoneda:
        while bandera2:
            inputCode2 = input("Ingrese el codigo de la moneda destino: ").strip().upper()
            if inputCode2 in codigosMoneda:
                bandera2 = False
            else:
                print(f"El codigo {inputCode2} no es valido o no esta disponible")

        bandera = False
    else:
        print(f"El codigo {inputCode} no es valido o no esta disponible")

inputAmount = float(input("Digite la cantidad: $"))
url = "http://127.0.0.1:5000/convert"
params = {
    "from": inputCode,
    "to": inputCode2,
    "amount": inputAmount
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"{data['amount']} {data['base_currency']} son {data['converted_amount']} {data['target_currency']}")
else:
    print("Error en la solicitud:", response.json())
