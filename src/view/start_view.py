
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox, QStatusBar
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt

class StartView(QMainWindow):
    """
        This class is responsible for managing the start window views in the application 
    """

    #! Initialize class scope variables
    buttons = {}

    def __init__(self):
        """Function to create box to store widgets"""

        #! Calling parent class init function
        super(StartView, self).__init__()
        self.setStyleSheet(
            'QMainWindow { background-color: pink; }'
            'QPushButton { background-color: cyan; border: none; padding: 10px; border-radius: 5px; }'
            'QPushButton:hover { background-color: white; }'
        )
        #! Set the central widget and the general layout
        self.verticalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.verticalLayout)
        
        #! Create init views
        self.createTitle()
        self.createHorizontalLayout()
        self.createGameButton()

    def createTitle(self):
        """Function to create title"""

        #! Create Box Layout to store Title
        horizontalLayout = QHBoxLayout()
        #! Create label for Title
        title = QLabel()
        title.setText('TicTacToe')
        titleFontSettings = QFont()
        titleFontSettings.setPointSize(20)
        titleFontSettings.setWeight(QFont.Bold)
        title.setFont(titleFontSettings)
        title.setStyleSheet("margin: 20px 0;")
        horizontalLayout.addWidget(title)
        horizontalLayout.setAlignment(Qt.AlignCenter)
        #! Add Horizontal Box Layout to Vertical Box Layout
        self.verticalLayout.addLayout(horizontalLayout)

    def createHorizontalLayout(self):
        """Function to create label and input for Ip Address"""

        #! Create Box Layout to store label and input field for Ip Address
        horizontalLayout = QHBoxLayout()
        #! Create Label
        labelIp = QLabel()
        labelIp.setText('Ip Address')
        labelIp.setStyleSheet('margin-bottom: 30px;')
        horizontalLayout.addWidget(labelIp)
        #! Create Input Field for Ip Address
        self.inputIp = QLineEdit()
        self.inputIp.setStyleSheet('margin-bottom: 30px;')
        horizontalLayout.addWidget(self.inputIp)
        #! Add Horizontal Box Layout to Vertical Box Layout
        self.verticalLayout.addLayout(horizontalLayout)

    def createGameButton(self):
        """Function to create start button and join button"""

        #! Create Box Layout to store Button
        horizontalLayout = QHBoxLayout()
        #! Create Button Start Game
        startBtn = QPushButton('CREATE GAME')
        startBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttons['create'] = startBtn
        horizontalLayout.addWidget(startBtn)
        #! Create Button Join Game
        joinBtn = QPushButton('JOIN GAME')
        joinBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttons['join'] = joinBtn
        horizontalLayout.addWidget(joinBtn)
        #! Add Horizontal Box Layout to Vertical Box Layout
        self.verticalLayout.addLayout(horizontalLayout)

    def createStatusBar(self, msg):
        """Function to create status bar at StartView"""

        status = QStatusBar()
        status.showMessage(msg)
        self.setStatusBar(status)