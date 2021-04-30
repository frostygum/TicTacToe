
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QLabel, QListView, QStatusBar
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class EndView(QMainWindow):
    """
        This class is responsible for managing the end window views in the application 
    """

    #! Initialize class scope variables
    buttons = {}

    def __init__(self):
        """Function to create box to store widgets"""

        #! Calling parent class init function
        super(EndView, self).__init__()
        self.setStyleSheet(
            'QMainWindow { background-color: pink; }'
            'QPushButton { background-color: cyan; border: none; padding: 10px; border-radius: 5px; }'
            'QPushButton:hover { background-color: white; }'
            'QListView { background-color: pink; }'
        )
        #! Set the central widget and the general layout
        self.verticalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.verticalLayout)
        
        #! Create init views
        self.createListView()
        self.createGameButton()

    def createListView(self):
        """Function to create list view for game record"""

        #! Create List View
        listView = QListView()
        #! Add List View to Vertical Box Layout
        self.verticalLayout.addWidget(listView)

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