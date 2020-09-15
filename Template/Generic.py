class Generic:

    def __init__(self, input_shape):
        self.parameter_choices = [
            {
                'name': 'hyper-parameter name',
                'values': [1, 2, 3]
            }
        ]
        self.input_shape = input_shape
        self.parameters = None
        self.model = None

    def generate_random_model(self):
        parameters = None
        # select parameters randomly from parameter_choices
        self.generate_model(parameters)

    # TODO get a handle on where to handle these
    def generate_model(self, parameters):
        self.parameters = parameters
        model = None
        # based on paraemters, build model
        self.model = model

    def compile(self):
        # compile your model
        None

    def fit(self, X_train, Y_train, X_valid, Y_valid, epochs):
        # fit/train your model here
        None

    def evaluate(self, X_test, Y_test):
        # evaluate your model, used to evaluate fitness!
        None
