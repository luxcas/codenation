import requests
import hashlib
import json
import string

# dados answer.json
# get = {"numero_casas":7,
#        "token":"2d38ec6b1e27e6975322ff38c6506d209c2e51bc",
#        "cifrado":"aol pualyula? pz aoha aopun zapss hyvbuk? ovtly zptwzvu",
#        "decifrado":"",
#        "resumo_criptografico":""}


def cesar(cifrado, numero_casas):
    alfabeto = string.ascii_lowercase
    resultado = ''
    rotacao = int(numero_casas)
    for letra in cifrado:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            posicao = (posicao - rotacao) % 26
            resultado = resultado + alfabeto[posicao]
    return resultado


params = {'token': '2d38ec6b1e27e6975322ff38c6506d209c2e51bc'}
url_api = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
url_submit_solution = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=2d38ec6b1e27e6975322ff38c6506d209c2e51bc'

response = requests.get(url_api, params=params)

if response.status_code == requests.codes.ok:
    client_resp = response.text
    item = json.loads(client_resp)
    cifrado = item['cifrado']
    numero_casas = item['numero_casas']
    resumo_criptografico = item['resumo_criptografico']
    decifrado = cesar(cifrado, numero_casas)

    encrypted = hashlib.sha1(str(cifrado).encode('utf-8')).hexdigest()

    if decifrado:
        item['decifrado'] = cesar(cifrado, numero_casas)
        item['resumo_criptografico'] = encrypted

        fp = open('answer.json', 'w')

        fp.write(json.dumps(item))
        fp.close()

        headers = {'Content-type': 'multipart/form-data'}
        # files = {'file': open('answer.json', 'rb')}
        files = {'file': ('answer.json', open('answer.json', 'rb'))}
        payload = {'name': 'answer', 'file': open('answer.json', 'rb')}
        # enviar arquivo JSON answer.json
        response_post = requests.post(url_submit_solution, files=files, headers=headers, data=payload)
        # print(response_post)
        print(response_post.status_code)
        print(response_post.text)
        import pdb; pdb.set_trace()
