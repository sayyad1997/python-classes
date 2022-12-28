class NISSAN:
    def __init__(self):
        self.models=['altima', '370z', 'cube', 'rogue']

    def modelsout(self):
        print("these are the available models in nissan :")
        for model in self.models:
            print(model)