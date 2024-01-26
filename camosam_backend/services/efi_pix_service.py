import os
import json
from dotenv import load_dotenv
import requests
import base64


load_dotenv(override=True)


def get_pix_token() -> tuple[str, bool]:
  try:
    auth = base64.b64encode(
      (f'{os.getenv("CLIENT_ID")}:{os.getenv("CLIENT_SECRET")}'
    ).encode()).decode()

    payload = {'grant_type': 'client_credentials'}

    headers = {
    'Authorization': f'Basic {auth}',
    'Content-Type': 'application/json'
    }

    response = requests.post(f'{os.getenv("BASE_URL")}/oauth/token',
                            headers=headers,
                            data=json.dumps(payload),
                            cert=os.getenv('CERTIFIED_PEM'))

    if response.status_code == 200:
      response_json = response.json()
      return response_json.get('access_token'), None

    return f'[GET TOKEN ERROR]: {response.status_code}, {response.text}', True
  except Exception as error:
    return f'[GET TOKEN ERROR]: {error}', True


def create_order(headers: dict, debt_value: str) -> tuple[str, bool]:
  try:
    payload = {
      'calendario': {
      'expiracao': 3600
      },
      'devedor': {
      'cpf': os.getenv('CPF_PIX') ,
      'nome': os.getenv('MAIN_USER_PIX')
      },
      'valor': {
      'original': debt_value
      },
      'chave': os.getenv('PIX_KEY'),
      'solicitacaoPagador': 'Presente para SAM'
    }

    response = requests.post(f'{os.getenv("BASE_URL")}/v2/cob',
                            headers=headers,
                            data=json.dumps(payload),
                            cert=os.getenv('CERTIFIED_PEM'))

    if response.status_code == 201:
      return response.json(), None

    return f'[CREATE ORDER ERROR]: {response.status_code}, {response.text}', True
  except Exception as error:
    return f'[CREATE ORDER ERROR]: {error}', True


def create_qrcode(headers: dict, location_id: str) -> tuple[str, bool]:
  try:
    response = requests.get(f'{os.getenv("BASE_URL")}/v2/loc/{location_id}/qrcode',
                            headers=headers,
                            cert=os.getenv('CERTIFIED_PEM'))

    if response.status_code == 200:
      return response.json(), None

    return f'[CREATE QRCODE ERROR]: {response.status_code}, {response.text}', True
  except Exception as error:
    return f'[CREATE QRCODE ERROR]: {error}', True


def create_charge(debt_value: str) -> tuple[str, bool]:
  try:
    headers = {
    'Authorization': f'Bearer {get_pix_token()[0]}',
    'Content-Type': 'application/json'
    }
    location_id, error = create_order(headers, debt_value)
    if error:
      raise Exception
    location_id = location_id.get('loc').get('id')
    qr_code, error = create_qrcode(headers, location_id)
    if error:
      raise Exception

    image_qr_code = qr_code.get('imagemQrcode')
    return image_qr_code, None
  except Exception as error:
    return f'[CHARGE ERROR]: {error}', True
