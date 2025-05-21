# 🚦 Classificação de Sinais de Trânsito com Deep Learning

Este projeto é uma aplicação web construída com **Streamlit** para classificar sinais de trânsito utilizando um modelo de Deep Learning treinado com TensorFlow/Keras.

## 📷 Funcionalidades

- Upload de imagens ou captura pela câmera
- Predição de sinais de trânsito a partir de um modelo CNN
- Interface moderna e responsiva com Streamlit
- Suporte a imagens em tons de cinza

## 🧠 Modelo

O modelo foi treinado em sinais de trânsito normalizados para uma dimensão de `32x32`, em escala de cinza. O arquivo `.hdf5` com os pesos está localizado na pasta `app/model/`.

## 📁 Estrutura do Projeto

```
detector-sinais-streamlit/
├── app/
│   ├── app.py              # Interface principal do Streamlit
│   ├── classify.py         # Lógica de carregamento e predição do modelo
│   ├── constants.py        # Nomes dos sinais em português
│   ├── utils.py            # Funções auxiliares de imagem
│   ├── assets/
│   │   └── ilustracao.jpg  # Imagem decorativa
│   └── model/
│       └── Traffic_Sign_Classifier_CNN.hdf5  # Modelo treinado
├── requirements.txt
└── README.md
```

## 🚀 Como Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/detector-sinais-streamlit.git
cd detector-sinais-streamlit
```

2. Instale os requisitos:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app/app.py
```

## ☁️ Deploy no Streamlit Cloud

1. Faça login em: https://streamlit.io/cloud
2. Conecte seu repositório GitHub
3. Selecione o arquivo `app/app.py` como entrypoint
4. Pronto! Sua aplicação estará disponível online 🎉

## 🛠 Requisitos

- Python 3.8+
- TensorFlow 2.x
- Streamlit
- Pillow

## 📬 Contato

Desenvolvido por [Paciência Aníbal Muienga] – Contribuições, dúvidas ou sugestões são bem-vindas!

---

© 2025 - Licença MIT
