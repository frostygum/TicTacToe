from PyQt5.QtWidgets import QMessageBox

class BaseController:
    def __init__(self, navigationWidget, views):
        self.mainView = views['main']
        self.gameView = views['game']
        self.navigationWidget = navigationWidget

    def changeWindow(self, windowPage):
        if(windowPage == 'main'):
            window = self.mainView
            self.navigationWidget.setWindowTitle('TicTacToe')
            self.navigationWidget.setFixedSize(330, 200)
        elif(windowPage == 'game'):
            window = self.gameView
            self.navigationWidget.setWindowTitle('Player X Playing')
            self.navigationWidget.setFixedSize(330, 330)
        self.navigationWidget.addWidget(window)
        self.navigationWidget.setCurrentIndex(self.navigationWidget.currentIndex() + 1)

    def showDialog(self, msg, title, callback = None):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle('Alert')
        msgBox.exec()
        if callback != None:
            callback()