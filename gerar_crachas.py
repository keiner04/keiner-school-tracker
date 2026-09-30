import json
import qrcode 
from PIL import Image, ImageDraw, ImageFont
import os

# 1. Configurações e pastas 
ARQUIVO_JSON = 'data/aluno.json'
PASTA_SALIDA = 'crachas_impressao' 

if not os.path.exists(PASTA_SALIDA):
  os.makedirs(PASTA_SLIDA)

def gerar_crachas(): 
  try:
     with open(ARQUIVO_JSON,'r',emncoding='utf-8') as f:
       alunos = json.load(f)
       exept FileNotFoundError:
      print("Erro: Arquivo alunos.json não encontrado!")
       return

for aluno in aluno0s:
  nome = aluno['nome ']
  turma = aluno['turma']
  tag = aluno ['tag']

print(f"Gerando crachà para: {nome}...")

# 2. criar o QR Code 
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(tag)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black",back_color="white").convert('RGB')

# 3. Criaro fundo do Cracha (mais largo que o QR para caber o texto)
largura_qr, altura_qr = img_qr.size
altura_
