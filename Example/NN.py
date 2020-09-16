from tensorflow.keras import layers, models, Sequential
from numpy.random import choice

class NN:

    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.parameter_choices = [
            {
                'name': 'filters_1',
                'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            },
            {
                'name': 'kernel_size_1',
                'values': [1, 2, 3, 4, 5, 6, 7, 8, 9]
            },
            {
                'name': 'dense_1',
                'values': [1, 2, 3, 4, 5, 6, 7]
            }
        ]
        self.parameters = []
        self.model = None


    def generate_random_model(self):
        parameters = []
        for i in range(len(self.parameter_choices)):
            parameters.append(choice(self.parameter_choices[i]['values']))
        self.generate_model(parameters)

    def generate_model(self, parameters):
        self.parameters = parameters
        self.model = Sequential()
        self.model.add(layers.Conv2D(input_shape=self.input_shape,
                                     filters=self.parameters[0],
                                     kernel_size=(self.parameters[1], self.parameters[1]),
                                     data_format='channels_last'))
        self.model.add(layers.Conv2DTranspose(self.parameters[0], (self.parameters[1], self.parameters[1])))
        self.model.add(layers.Dense(self.parameters[2]))
        self.model.add(layers.Dense(1))
        self.model.compile(loss='mse', optimizer='adam')


    def fit(self, X_train, Y_train, X_valid, Y_valid, epochs):
        self.model.fit(X_train, Y_train, epochs=epochs, validation_data=(X_valid, Y_valid))

    def evaluate(self, X_test, Y_test):
        return self.model.evaluate(X_test, Y_test)

    def save(self):
        self.model.save('./saved_models')