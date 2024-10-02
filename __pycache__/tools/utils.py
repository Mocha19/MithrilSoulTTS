#this is the utils file

#this file is used to store utility functions that are used throughout the app.

import json
import os
from PyQt5 import QtWidgets

def create_checkbox_layout(checkbox, description):
    """Create a layout for a checkbox with a tooltip."""
    container = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout(container)
    layout.addWidget(checkbox)
    layout.addStretch()
    container.setToolTip(description)
    return container

def create_slider_layout(label, slider, description):
    """Create a layout for a label and slider with a tooltip."""
    container = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout(container)
    layout.addWidget(label)
    layout.addWidget(slider)
    container.setToolTip(description)
    return container

def create_combobox_layout(label, dropdown, slider, description):
    """Create a layout for a label, dropdown, and slider with a tooltip."""
    container = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout(container)
    layout.addWidget(label) 
    layout.addWidget(dropdown)
    layout.addWidget(slider)
    container.setToolTip(description)
    return container

def save_preferences(file_path, preferences):
    """Save preferences to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(preferences, f)
    except IOError as e:
        print(f"Error saving preferences: {e}")

def load_preferences(file_path):
    """Load preferences from a JSON file."""
    if not os.path.exists(file_path):
        return None  # No preferences file exists yet
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading preferences: {e}")
        return None

