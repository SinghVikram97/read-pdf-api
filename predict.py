import sys
import numpy as np
import pandas as pd
import os
import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle


from sklearn.preprocessing import LabelEncoder
from tensorflow import keras

layers = keras.layers
models = keras.models

class Classifier:
    def __init__(self, model_path = "model.h5", vectorizer_path = "tokenizer.pkl", encoder_path = "encoder.pkl"):
        self.model = keras.models.load_model(model_path)
        self.vectorizer = pickle.load(open(vectorizer_path, 'rb'))
        self.encoder = pickle.load(open(encoder_path, 'rb'))

    def predict(self, input_string):
        input_string = [input_string]
        vectorized_string = self.vectorizer.texts_to_matrix(input_string)
        prediction = self.model.predict(vectorized_string).argmax()
        return self.encoder.inverse_transform([prediction])


def main():
    predictor = Classifier()
    inputText='code vita';
    
    ip=list(inputarg);
    ip=' '.join(ip);
    print(predictor.predict(inputText))
    
if __name__ == "__main__":
    main()