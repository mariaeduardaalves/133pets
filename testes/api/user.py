import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}

def test_post_user():
    # Configura
    status_code_esperado = 200   # se a comunicacao teve ida e volta
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '123'
    # Executa
    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open('//Users//dudaalves//PycharmProjects//133pets//vendors//json//user1.json', 'rb'),
        headers=headers
        )
    # Valida
    print(resultado_obtido)
    body_da_resposta = resultado_obtido.json()
    print(body_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert body_da_resposta['code'] == code_esperado
    assert body_da_resposta['type'] == type_esperado
    assert body_da_resposta['message'] == message_esperada

