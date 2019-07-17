
import numpy as np
import pandas as pd
import os
import itertools
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle


from sklearn.preprocessing import LabelEncoder
from tensorflow import keras

layers = keras.layers
models = keras.models


class NewsClassifier:
    def __init__(self, model_path = "model.h5", vectorizer_path = "tokenizer.pkl", encoder_path = "encoder.pkl"):
        self.model = keras.models.load_model(model_path, compile=False)
        self.vectorizer = pickle.load(open(vectorizer_path, 'rb'))
        self.encoder = pickle.load(open(encoder_path, 'rb'))

    def predict(self, input_string):
        input_string = [input_string]
        vectorized_string = self.vectorizer.texts_to_matrix(input_string)
        prediction = self.model.predict(vectorized_string).argmax()
        print(prediction)
        return self.encoder.inverse_transform([prediction])


def main():
    predictor = NewsClassifier()
    ip=sys.argv[1];
    for st in ip:
        if st==',':
            st=' '
    print(ip);
    print(predictor.predict(ip))

if __name__ == "__main__":
    main()
