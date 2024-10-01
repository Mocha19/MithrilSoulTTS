from PyQt5 import QtWidgets, QtCore
from tts_widget import TTSWidget
from preferences_widget import PreferencesWidget

class TTSApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle('Charisma Echo AI')
        self.setMinimumSize(600, 400)

        # Default to dark mode
        self.is_dark_mode = True
        self.font_size = 12  # Default font size

        # Create the tab widget
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.addTab(TTSWidget(self), "TTS")
        self.tabs.addTab(PreferencesWidget(self), "Preferences")

        # Main layout for the entire window
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        # Apply the initial dark mode style
        self.apply_styles()

    # Apply the current styles based on the theme and font size
    def apply_styles(self):
        if self.is_dark_mode:
            self.setStyleSheet(f"""
                QWidget {{
                    background-color: #212121;
                    color: darkgray;
                    font-size: {self.font_size}px;
                }}
            """)
        else:
            self.setStyleSheet(f"""
                QWidget {{
                    background-color: #FFFFFF;
                    color: black;
                    font-size: {self.font_size}px;
                }}
            """)

    # Toggle dark/light mode
    def toggle_theme(self, state):
        self.is_dark_mode = state == QtCore.Qt.Checked
        self.apply_styles()

    # Adjust font size and maintain current theme
    def change_font_size(self, value):
        self.font_size = value
        self.apply_styles()
