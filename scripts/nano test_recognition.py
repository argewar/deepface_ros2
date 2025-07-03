from deepface import DeepFace

# Caminho da imagem de teste
img_path = "~/deepface_ros2_ws/deepface_ros2/scripts/img_test1.jpg"  # Substitua por uma imagem nova da webcam ou outra

# Caminho para o dataset organizado
db_path = "../datasets/"

# Realiza o reconhecimento
try:
    result = DeepFace.find(img_path=img_path, db_path=db_path, enforce_detection=False)

    if not result[0].empty:
        identity = result[0].iloc[0]["identity"]
        print(f"Pessoa reconhecida: {identity}")
    else:
        print("Nenhuma correspondência encontrada.")

except Exception as e:
    print(f"Erro durante o reconhecimento: {e}")
