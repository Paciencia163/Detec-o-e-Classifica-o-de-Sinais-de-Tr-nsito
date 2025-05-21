import streamlit as st
from PIL import Image
from classify import predict
from constants import NOMES_DE_SINAIS
from utils import convert_to_rgb, image_to_byte_stream

def main():
    st.title("🚦 Classificação de Sinais de Trânsito com Deep Learning")
    st.image("assets/ilustracao.jpg", caption='Classificação de Sinais de Trânsito', use_container_width=True)

    st.header("Entrada de Imagem")
    option = st.selectbox("Escolha o método de entrada:", ["Upload de Imagem", "Captura com Câmera"])

    image = None
    if option == "Upload de Imagem":
        uploaded_file = st.file_uploader("Escolha uma imagem JPG...", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file)

    elif option == "Captura com Câmera":
        camera_image = st.camera_input("Capture uma imagem")
        if camera_image:
            image = Image.open(camera_image)

    if image:
        st.image(image, caption='Imagem Selecionada', use_container_width=True)
        if st.button("Classificar"):
            process_and_display_prediction(image)

def process_and_display_prediction(image):
    with st.spinner("Classificando..."):
        rgb_image = convert_to_rgb(image)
        img_bytes = image_to_byte_stream(rgb_image)
        label = predict(img_bytes)
        nome_sinal = NOMES_DE_SINAIS.get(label, "Sinal desconhecido")

        st.markdown(f"""
            <div style="text-align: center; animation: pulse 2s infinite;">
                <h2 style="font-size: 36px; color: #4CAF50;">{nome_sinal}</h2>
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
