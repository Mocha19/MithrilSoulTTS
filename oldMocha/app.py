import json
from PyQt5 import QtWidgets, QtCore

from oldMocha.tts_widget import TTSWidget
from oldMocha.preferences_widget import PreferencesWidget

class TTSApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_user_settings()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle('Charisma Echo AI')
        self.setMinimumSize(600, 400)

        # Set user preferences
        self.is_dark_mode = True
        self.font_size = 12 # set to none if you want it to load saved font size

        self.context_rules = True
        self.auto_switch = True
        self.remember_last_profile = True
        self.auto_correction = True

        # Create the tab widget
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.addTab(TTSWidget(self), "TTS")
        self.tabs.addTab(PreferencesWidget(self), "Preferences")
        #self.tabs.addTab(ProfilesWidget(self), "Profiles") <--------------------------------------------------------------------------------------

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

    #Load user settings from the JSON file
    def load_user_settings(self):
        try:
            with open('stored_data.json', 'r') as f:
                data = json.load(f)
                user_prefs = data.get('user_preferences', {})
                self.is_dark_mode = user_prefs.get('is_dark_mode', True)
                self.font_size = user_prefs.get('font_size', 12)

                # Load profile settings
                profile_prefs = data.get('profiles', {})
                self.context_rules = profile_prefs.get('context_rules', '')
                self.auto_switch = profile_prefs.get('auto_switch', False)
                self.remember_last_profile = profile_prefs.get('remember_last_profile', False)
                self.auto_correction = profile_prefs.get('auto_correction', False)

        except (FileNotFoundError, json.JSONDecodeError): # creates json file if it cant find one
            self.save_user_settings()

    # Save user settings to the JSON file
    def save_user_settings(self):
        data = {
            'user_preferences': {
                'is_dark_mode': self.is_dark_mode,
                'font_size': self.font_size,
            },
            'profiles': {
                'context_rules': self.context_rules,
                'auto_switch': self.auto_switch,
                'remember_last_profile': self.remember_last_profile,
                'auto_correction': self.auto_correction,
            }
        }

        with open('stored_data.json', 'w') as f:
            json.dump(data, f, indent=4)
