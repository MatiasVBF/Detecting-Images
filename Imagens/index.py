import boto3

# Criar cliente Rekognition
client = boto3.client('rekognition', region_name='us-east-1')

# Carregar imagem
with open("celebridade.jpg", "rb") as image:
    response = client.recognize_celebrities(Image={'Bytes': image.read()})

# Exibir resultados
for celebrity in response['CelebrityFaces']:
    print(f"Nome: {celebrity['Name']}")
    print(f"Confiança: {celebrity['MatchConfidence']:.2f}%")
    print("-" * 30)
