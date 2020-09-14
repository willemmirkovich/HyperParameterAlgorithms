from tensorflow.keras import layers, models, Sequential

class NN:

    def __init__(self, shape):
        self.shape = shape
        self.args = None
        self.model = None


    def generate_random_model(self):
        args = []
        # TODO for each arg that you modify append to the list

        self.args = args



    def generate_model(self, args):
        None

        self.args = args

    def fit(self, X_train, Y_train, X_valid, Y_valid, epochs):
        self.model.fit(X_train, Y_train, epochs=epochs, validation_data=(X_valid, Y_valid))

    def evaluate(self, X_test, Y_test):
        return self.model.evaluate(X_test, Y_test)