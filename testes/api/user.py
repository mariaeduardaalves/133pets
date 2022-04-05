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


def test_get_user():
    # Configura
    username = 'maria'
    status_code_esperado = 200
    id_esperado = 123
    firstName_esperado = 'duda'
    lastName_esperado = 'silva'
    email_esperado = 'maria@maria.com'
    password_esperado = '12345678'
    phone_esperado = '99999999999'
    userStatus_esperado = 0
    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/user/' + username,
        headers=headers
    )
    # Valida
    print(resultado_obtido)
    body_da_resposta = resultado_obtido.json()
    print(body_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert body_da_resposta['id'] == id_esperado
    assert body_da_resposta['username'] == username
    assert body_da_resposta['firstName'] == firstName_esperado
    assert body_da_resposta['lastName'] == lastName_esperado
    assert body_da_resposta['email'] == email_esperado
    assert body_da_resposta['password'] == password_esperado
    assert body_da_resposta['phone'] == phone_esperado
    assert body_da_resposta['userStatus'] == userStatus_esperado


def test_put_user():
    # Configura
    username = 'maria'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '123'
    # Executa
    resultado_obtido = requests.put(
        url=base_url + '/user/' + username,
        data=open('//Users//dudaalves//PycharmProjects//133pets//vendors//json//user2.json', 'rb'),
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


def test_delete_user():
    # Configura
    username = 'maria'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = 'maria'
    # Executa
    resultado_obtido = requests.delete(
        url=base_url + '/user/' + username,
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
