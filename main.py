import requests
import json



while True:
    try:
        user_input = input("Digite o CEP que está procurando: ")

        api_call = requests.get(f"https://viacep.com.br/ws/{user_input}/json/")

        api_response = api_call.json()

        city = api_response["localidade"]

        state = api_response["uf"]

        cep = api_response["cep"]

        street = api_response["logradouro"]

        neighborhood =api_response["bairro"]

        print(f'''  
    CEP = {cep}
    Logradouro = {street}
    Bairro = {neighborhood}
    Cidade = {city}
    Estado = {state}
    ''')
        
        keep_going = input("Deseja buscar por mais algum cep?(sim/nao): ").lower()

        if keep_going == "nao" or keep_going == "não":
            break
        elif keep_going == "sim":
            pass
        else:
            print("Error! Você deve responder com 'sim'ou 'nao'")
            break

    except KeyboardInterrupt:
        print("A excecução foi interrompida pelo usuário!")
        break

    except ValueError:
        print("Error! Verifique se o CEP foi digitado corretamente.")
    
    except:
        print("Error! Reinicie o programa e tente novamente.")


print("Execução finalizada!")



