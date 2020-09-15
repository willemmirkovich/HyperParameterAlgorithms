class Generic:

    def __init__(self):
        self.arg_choices = [
            {
                'name': 'hyper-parameter name',
                'values': [1, 2, 3]
            }
        ]

    def generate_random_model(self):
        None

    # TODO get a handle on where to handle these
    def generate_model(self, args, mutation_probability):
        None

    def fit(self, X_train, Y_train, X_valid, Y_valid, epochs):
        None

    def evaluate(self, X_test, Y_test):
        None
