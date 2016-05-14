class IcoSphere():
    def __init__(self):
        """As long as the loader-function is in the module creating this
        class, it can run apparently!"""
        self.model = loader.loadModel("icosphere")

    def getModel(self):
        return self.model
