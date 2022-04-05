import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'  # De onde vem
headers = {'Content-Type': 'application/json'}  # Qual o formato json ou Xml

def testar_incluir_pet():
# Configura: o que se espera
  # Dados de entrada: virao do pet1.json
  # Resultado esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Snnopy'
    tag_esperada = 'Vacinado'


# Executa: resultado obtido
    resultado_obtido = requests.post(url=base_url + '/pet',
                  data=open('//Users//dudaalves//PycharmProjects//133pets//vendors//json//pet1.json', 'rb'),
                  headers=headers
                  )

# Valida: compara o esperado com o obtido
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()                       # Extrai o json do response
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado       # Checar tudo
    assert corpo_da_resposta['name'] == nome_pet_esperado             # Checar o nome do animal
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_consultar_pet():
    # 1 - Configura
    # 1.1 - Dados de entrada

    pet_id = '6599626'

    # 1.2 - Resultado Esperado

    status_code_esperado = 200
    nome_pet_esperado = 'Snnopy'
    tag_esperada = 'Vacinado'

    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado  # Checar tudo
    assert corpo_da_resposta['name'] == nome_pet_esperado  # Checar o nome do animal
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_alterar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'Snnopy'
    status_esperado = 'Solded'

    resultado_obtido = requests.put(
        url=f'{base_url}/pet',
        data=open('//Users//dudaalves//PycharmProjects//133pets//vendors//json//pet2.json', 'rb'),
        headers=headers
    )
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta["name"] == nome_pet_esperado
    assert corpo_da_resposta['status'] == status_esperado


def testar_deletar_pet():
    # Configura
    pet_id = '6599626'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    # Executa
    resultado_obtido = requests.delete(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )
    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == pet_id


