#all preferences have now been merged into a single json file. the file is now preferences.json
from PyQt5 import QtWidgets
from preferencetabs.general import create_general_tab
from preferencetabs.audio import create_audio_tab
from preferencetabs.advanced import create_advanced_tab
from preferencetabs.premium import create_premium_tab

def create_preferences_window(parent):
    preferences_widget = QtWidgets.QWidget()

    # Create a tab widget for Preferences
    tab_widget = QtWidgets.QTabWidget()

    # Add each preference tab
    tab_widget.addTab(create_general_tab(parent), "General")
    tab_widget.addTab(create_audio_tab(parent), "Audio")
    tab_widget.addTab(create_advanced_tab(parent), "Advanced")
    tab_widget.addTab(create_premium_tab(parent), "Premium")

    # Layout for the Preferences window
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(tab_widget)
    preferences_widget.setLayout(vbox)

    return preferences_widget


from tools.utils import save_preferences, load_preferences

class PreferenceManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        self.connect_signals()
        self.load_all_preferences()

    def setup_ui(self):
        self.tab_widget = QtWidgets.QTabWidget()
        self.audio_tab = audio.create_audio_tab(self)
        self.general_tab = general.create_general_tab(self)
        # Add other tabs as needed

        self.tab_widget.addTab(self.audio_tab, "Audio")
        self.tab_widget.addTab(self.general_tab, "General")
        # Add other tabs to the tab widget

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def connect_signals(self):
        widgets = [
            (self.noise_checkbox, 'stateChanged'),
            (self.echo_checkbox, 'stateChanged'),
            (self.autoplay_checkbox, 'stateChanged'),
            (self.instant_checkbox, 'stateChanged'),
            (self.mic_slider, 'valueChanged'),
            (self.mic_dropdown, 'currentIndexChanged'),
            (self.speaker_slider, 'valueChanged'),
            (self.speaker_dropdown, 'currentIndexChanged'),
            (self.narrator_dropdown, 'currentIndexChanged'),
            (self.narrator_slider, 'valueChanged'),
            (self.narrator_speed_slider, 'valueChanged'),
            # Add widgets from other tabs
        ]
        for widget, signal in widgets:
            getattr(widget, signal).connect(self.save_all_preferences)

    def save_all_preferences(self):
        self.save_audio_preferences()
        self.save_general_preferences()
        self.save_advanced_preferences()
        self.save_premium_preferences()

    def load_all_preferences(self):
        self.load_audio_preferences()
        self.load_general_preferences()
        self.load_advanced_preferences()
        self.load_premium_preferences()