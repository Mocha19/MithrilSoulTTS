import json
from PyQt5 import QtWidgets, QtCore
from tts_widget import TTSWidget
from preferences_widget import PreferencesWidget

class TTSApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.load_user_settings()
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
        self.save_user_settings() # -NEW-

    # Adjust font size and maintain current theme
    def change_font_size(self, value):
        self.font_size = value
        self.apply_styles()
        self.save_user_settings() # -NEW-

    # Load user settings from the JSON file
    def load_user_settings(self):
        try:
            with open('user_data.json','r') as f:
                data = json.load(f)
                self.is_dark_mode = data.get('is_dark_mode', True)
                self.font_size = data.get('font_size', 12)
        except (FileNotFoundError, json.JSONDecodeError): #if json file doesnt exist, it creates a new file with default preferences
            self.save_user_settings() 

    # Save user settings to the JSON file
    def save_user_settings(self):
        data = {'is_dark_mode': self.is_dark_mode, 'font_size': self.font_size}

        with open('user_data.json','w') as f:
            json.dump(data, f, indent=4)
