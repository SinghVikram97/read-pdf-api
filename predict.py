
import pickle



import sys

import keras

layers = keras.layers
models = keras.models

inputText=sys.argv[1];
class NewsClassifier:
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
    predictor = NewsClassifier()
    while True:
        ip = inputText
        if ip == "quit":
            break
        print(predictor.predict(ip))

if __name__ == "__main__":
    main()

