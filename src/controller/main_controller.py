class MainController:
    def __init__(self, view):
        self.view = view
        # Connect signals and slots
        self.connectSignals()

    def connectSignals(self):
        print("ok")