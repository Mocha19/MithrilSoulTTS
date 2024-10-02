from PyQt5 import QtWidgets, QtCore

class TTSWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.volume = 50  # Default volume
        self.init_ui()

    def init_ui(self):
        # Create UI elements for TTS
        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.setPlaceholderText("Enter your command...")

        self.submit_button = QtWidgets.QPushButton('Submit', self)
        self.history_box = QtWidgets.QTextEdit(self)
        self.history_box.setReadOnly(True)

        # Volume slider and buttons
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(self.volume)
        self.volume_slider.setTickInterval(10)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.volume_label = QtWidgets.QLabel(f"Volume: {self.volume}", self)
        self.listen_button = QtWidgets.QPushButton('Listen', self)
        self.speak_button = QtWidgets.QPushButton('Speak', self)

        # Layout for volume slider and buttons
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.volume_slider, stretch=2)
        hbox.addWidget(self.volume_label, stretch=1)
        hbox.addWidget(self.listen_button)
        hbox.addWidget(self.speak_button)

        # Layout for TTS tab
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.history_box)
        vbox.addWidget(QtWidgets.QLabel("Volume"))
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # Connect events
        self.submit_button.clicked.connect(self.submit_text)
        self.text_input.returnPressed.connect(self.submit_text)

    def set_volume(self, value):
        self.volume = value
        self.volume_label.setText(f"Volume: {value}")

    def submit_text(self):
        user_input = self.text_input.text()
        if user_input:
            translated_text = "Processing text: " + user_input
            self.history_box.append(f"Input: {user_input}\nResponse: {translated_text}")
