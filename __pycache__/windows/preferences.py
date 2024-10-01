
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