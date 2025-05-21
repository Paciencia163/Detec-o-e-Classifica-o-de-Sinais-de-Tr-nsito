from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

_model = None

def get_model():
    global _model
    if _model is None:
        _model = load_model('model/Traffic_Sign_Classifier_CNN.hdf5')
    return _model

def predict(image_stream):
    model = get_model()
    image = load_img(image_stream, target_size=(32, 32), color_mode="grayscale")
    image = img_to_array(image) / 255.0
    image = np.reshape(image, [1, 32, 32, 1])
    prediction = model.predict(image)
    return int(np.argmax(prediction, axis=-1)[0])
