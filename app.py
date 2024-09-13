import streamlit as st
from PIL import Image
import classify
import numpy as np
import io

# Dicionário de nomes de sinais traduzido para português
NOMES_DE_SINAIS = {
    0: 'Limite de velocidade (20km/h)',
    1: 'Limite de velocidade (30km/h)',
    2: 'Limite de velocidade (50km/h)',
    3: 'Limite de velocidade (60km/h)',
    4: 'Limite de velocidade (70km/h)',
    5: 'Limite de velocidade (80km/h)',
    6: 'Fim do limite de velocidade (80km/h)',
    7: 'Limite de velocidade (100km/h)',
    8: 'Limite de velocidade (120km/h)',
    9: 'Proibido ultrapassar',
    10: 'Proibido ultrapassar veículos com mais de 3,5 toneladas',
    11: 'Prioridade na próxima interseção',
    12: 'Estrada prioritária',
    13: 'Dê a preferência',
    14: 'Pare',
    15: 'Proibido veículos',
    16: 'Proibido veículos com mais de 3,5 toneladas',
    17: 'Entrada proibida',
    18: 'Cuidado geral',
    19: 'Curva perigosa à esquerda',
    20: 'Curva perigosa à direita',
    21: 'Curva dupla',
    22: 'Estrada irregular',
    23: 'Estrada escorregadia',
    24: 'Estreitamento da pista à direita',
    25: 'Obras na pista',
    26: 'Semáforos',
    27: 'Pedestres',
    28: 'Travessia de crianças',
    29: 'Travessia de bicicletas',
    30: 'Cuidado com gelo/neve',
    31: 'Travessia de animais selvagens',
    32: 'Fim de todos os limites de velocidade e ultrapassagem',
    33: 'Vire à direita à frente',
    34: 'Vire à esquerda à frente',
    35: 'Siga em frente',
    36: 'Siga em frente ou à direita',
    37: 'Siga em frente ou à esquerda',
    38: 'Mantenha-se à direita',
    39: 'Mantenha-se à esquerda',
    40: 'Rotatória obrigatória',
    41: 'Fim da proibição de ultrapassagem',
    42: 'Fim da proibição de ultrapassagem para veículos com mais de 3,5 toneladas'
}

def main():
    st.title("Detecção e Classificação de Sinais de Trânsito - Deep Learning")

    # Inserir uma imagem ilustrativa no topo da aplicação
    st.image("ilustracao.jpg", caption='Classificação de Sinais de Trânsito', use_column_width=True)

    # Opções de upload de imagem ou captura pela câmera usando selectbox
    st.header("Escolha uma opção de entrada:")
    option = st.selectbox("Selecione o método de entrada:", ["Fazer upload de uma imagem", "Capturar imagem da câmera"])

    if option == "Fazer upload de uma imagem":
        uploaded_file = st.file_uploader("Escolha uma imagem...", type="jpg")
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption='Imagem Carregada', use_column_width=True)

            if st.button('Prever'):
                process_and_predict(image)

    elif option == "Capturar imagem da câmera":
        camera_image = st.camera_input("Capture uma imagem usando a câmera")
        if camera_image:
            image = Image.open(camera_image)
            st.image(image, caption='Imagem Capturada', use_column_width=True)

            if st.button('Prever'):
                process_and_predict(image)

def process_and_predict(image):
    with st.spinner('Classificando...'):
        # Converter para RGB se necessário
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Converter a imagem em uma stream de bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        img_bytes.seek(0)  # Mover o ponteiro para o início do arquivo em bytes
        
        label = classify.predict(img_bytes)
        res = NOMES_DE_SINAIS.get(label)

        # CSS para aumentar o tamanho da fonte e adicionar animação
        st.markdown(f"""
            <div style="text-align: center; animation: pulse 2s infinite;">
                <h2 style="font-size: 36px; color: #4CAF50;">{res}</h2>
            </div>
            <style>
            @keyframes pulse {{
                0% {{ transform: scale(1); }}
                50% {{ transform: scale(1.1); }}
                100% {{ transform: scale(1); }}
            }}
            </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
