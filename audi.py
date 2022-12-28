class AUDI:
    def __init__(self):
        self.models=["q7","a8","a6","a3"]

    def modelsout(self):
        print("these are the available models in audi :")
        for model in self.models:
            print(model)