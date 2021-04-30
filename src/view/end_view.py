
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QListWidgetItem, QListWidget, QStatusBar
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
        self.createGameButton()

    def createListWidget(self):
        """Function to create list view for game record"""

        #! Create List Widget
        self.listWidget = QListWidget()
        #! Add List Widget to Vertical Box Layout
        self.verticalLayout.addWidget(self.listWidget)

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
        item = QListWidgetItem(item)
        self.listWidget.insertItem(0, item)