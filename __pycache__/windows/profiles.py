#this is the profiles window
#here we set up the vaious tabs and visual settings for the profiles window.
from PyQt5 import QtWidgets
from profiletabs.narrator import create_narrator_tab
from profiletabs.profile import create_profile_tab

def create_profile_window(parent):
    profile_widget = QtWidgets.QWidget()

    # Create a tab widget for Profiles
    tab_widget = QtWidgets.QTabWidget()

    # Add each profile tab
    tab_widget.addTab(create_narrator_tab(parent), "Narrator")
    tab_widget.addTab(create_profile_tab(parent), "Profile")

    # Layout for the Profile window
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(tab_widget)
    profile_widget.setLayout(vbox)

    return profile_widget