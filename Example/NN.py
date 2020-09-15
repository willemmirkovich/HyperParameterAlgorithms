from tensorflow.keras import layers, models, Sequential

class NN:

    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.parameter_choices = [
            {},
            {},
            {}
        ]
        self.args = None
        self.model = None


    def generate_random_model(self):
        parameters = None

        self.generate_model(parameters)

    def generate_model(self, parameters):
        self.parameters = parameters


    def fit(self, X_train, Y_train, X_valid, Y_valid, epochs):
        self.model.fit(X_train, Y_train, epochs=epochs, validation_data=(X_valid, Y_valid))

    def evaluate(self, X_test, Y_test):
        return self.model.evaluate(X_test, Y_test)