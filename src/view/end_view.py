
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QListWidgetItem, QListWidget, QStatusBar, QLabel
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QSize

class EndView(QMainWindow):
    """
        This class is responsible for managing the end window views in the application 
    """

    #! Initialize class scope variables
    buttons = {}
    listWidget = None

    def __init__(self):
        """Function to create box to store widgets"""

        #! Calling parent class init function
        super(EndView, self).__init__()
        self.setStyleSheet(
            'QMainWindow { background-color: pink; }'
            'QPushButton { background-color: cyan; border: none; padding: 10px; border-radius: 5px; }'
            'QPushButton:hover { background-color: white; }'
            'QListWidget { background-color: pink; }'
            'QListWidget::item { padding: 10px }'
        )
        #! Set the central widget and the general layout
        self.verticalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.verticalLayout)
        
        #! Create init views
        self.createListWidget()
        self.createCount()
        self.createGameButton()

    def createListWidget(self):
        """Function to create list widget for game record"""

        #! Create List Widget
        self.listWidget = QListWidget()
        #! Add List Widget to Vertical Box Layout
        self.verticalLayout.addWidget(self.listWidget)

    def createCount(self):
        """Function to create win counter at EndView"""

        #! Create Box Layout to store Counter
        horizontalLayout = QHBoxLayout()
        #! Create Box Layout to store Host Counter
        horizontalLayoutHost = QHBoxLayout()
        #! Create Box Layout to store Client Counter
        horizontalLayoutClient = QHBoxLayout()
        #! Create Label for Host
        labelHost = QLabel()
        labelHost.setText('Host: ')
        labelHost.setStyleSheet('margin-bottom: 10px; margin-top: 10px; max-width: 35px;')
        horizontalLayoutHost.addWidget(labelHost)
        #! Create count for Host
        self.countHost = QLabel()
        self.countHost.setText('')
        self.countHost.setStyleSheet('margin-bottom: 10px; margin-top: 10px;')
        horizontalLayoutHost.addWidget(self.countHost)
        #! Create Label for Client
        labelClient = QLabel()
        labelClient.setText('Client: ')
        labelClient.setStyleSheet('margin-bottom: 10px; margin-top: 10px; max-width: 35px;')
        horizontalLayoutClient.addWidget(labelClient)
        #! Create count for Host
        self.countClient = QLabel()
        self.countClient.setText('')
        self.countClient.setStyleSheet('margin-bottom: 10px; margin-top: 10px;')
        horizontalLayoutClient.addWidget(self.countClient)
        #! Add Horizontal Box Layout Host to Horizontal Box Layout
        horizontalLayout.addLayout(horizontalLayoutHost)
        #! Add Horizontal Box Layout Client to Horizontal Box Layout
        horizontalLayout.addLayout(horizontalLayoutClient)
        #! Add Horizontal Box Layout to Vertical Box Layout
        self.verticalLayout.addLayout(horizontalLayout)


    def createGameButton(self):
        """Function to create play button and exit button"""

        #! Create Box Layout to store Button
        horizontalLayout = QHBoxLayout()
        #! Create Button Play Again
        playBtn = QPushButton('PLAY AGAIN')
        playBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttons['play'] = playBtn
        horizontalLayout.addWidget(playBtn)
        #! Create Button Exit Game
        exitBtn = QPushButton('EXIT GAME')
        exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttons['exit'] = exitBtn
        horizontalLayout.addWidget(exitBtn)
        #! Add Horizontal Box Layout to Vertical Box Layout
        self.verticalLayout.addLayout(horizontalLayout)

    def createStatusBar(self, msg):
        """Function to create status bar at EndView"""

        status = QStatusBar()
        status.showMessage(msg)
        self.setStatusBar(status)

    def createListWidgetItem(self, item):
        """Function to create item inside list widget"""

        item = QListWidgetItem(item)
        self.listWidget.insertItem(0, item)

    def emptyList(self):
        """Function to emptying list widget"""
        
        self.verticalLayout.removeWidget(self.listWidget)
        self.listWidget = QListWidget()
        self.verticalLayout.insertWidget(0, self.listWidget)