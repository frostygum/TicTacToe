
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QMessageBox

class BaseController:
    """
        This class is used as base for created controller
    """

    def __init__(self, navigationWidget, views):
        """Initiate function"""

        self.mainView = views['start']
        self.gameView = views['game']
        self.navigationWidget = navigationWidget

    def changeWindow(self, windowPage):
        """Function to change window with given param"""

        if(windowPage == 'start'):
            #! Goto Main Page
            window = self.mainView
            #! Reset sizing
            self.navigationWidget.setWindowTitle('TicTacToe')
            self.navigationWidget.setFixedSize(330, 200)
        elif(windowPage == 'game'):
            #! Goto GGame Page
            window = self.gameView
            #! Reset sizing
            self.navigationWidget.setWindowTitle('TicTacToe')
            self.navigationWidget.setFixedSize(330, 360)
        
        #! Create empty status bar
        window.createStatusBar('')
        self.navigationWidget.addWidget(window)
        self.navigationWidget.setCurrentIndex(self.navigationWidget.currentIndex() + 1)

    def showDialog(self, msg, title, callback = None):
        """Function to show Alert Dialog"""

        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.exec()
        #! Run any given callback after user close the dialog
        if callback != None:
            callback()