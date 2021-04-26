
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt

class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setStyleSheet('QMainWindow { background-color: pink; }'
                            'QPushButton { background-color: cyan; border: none; padding: 10px; border-radius: 5px; }'
                            'QPushButton:hover { background-color: white; }')
        self.vBox = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.vBox)
        self.buttons = {}
        
        self.createTitle()
        self.createHorizontalLayout()
        self.createGameButton()

    def createTitle(self):
        # Create Box Layout to store Title
        hBox = QHBoxLayout()
        # Create label for Title
        title = QLabel()
        title.setText('TicTacToe')
        titleFontSettings = QFont()
        titleFontSettings.setPointSize(20)
        titleFontSettings.setWeight(QFont.Bold)
        title.setFont(titleFontSettings)
        title.setStyleSheet("margin: 20px 0;")
        hBox.addWidget(title)
        hBox.setAlignment(Qt.AlignCenter)
        # Add Horizontal Box Layout to Vertical Box Layout
        self.vBox.addLayout(hBox)

    def createHorizontalLayout(self):
        # Create Box Layout to store label and input field for Ip Address
        hBox = QHBoxLayout()
        # Create Label
        labelIp = QLabel()
        labelIp.setText('Ip Address')
        labelIp.setStyleSheet('margin-bottom: 30px;')
        hBox.addWidget(labelIp)
        # Create Input Field for Ip Address
        self.inputIp = QLineEdit()
        self.inputIp.setStyleSheet('margin-bottom: 30px;')
        hBox.addWidget(self.inputIp)
        # Add Horizontal Box Layout to Vertical Box Layout
        self.vBox.addLayout(hBox)

    def createGameButton(self):
        # Create Box Layout to store Button
        hBox = QHBoxLayout()
        # Create Button Start Game
        startBtn = QPushButton('START GAME')
        startBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttons['start'] = startBtn
        hBox.addWidget(startBtn)
        # Create Button Join Game
        joinBtn = QPushButton('JOIN GAME')
        joinBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttons['join'] = joinBtn
        hBox.addWidget(joinBtn)
        # Add Horizontal Box Layout to Vertical Box Layout
        self.vBox.addLayout(hBox)