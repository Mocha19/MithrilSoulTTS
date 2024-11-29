#this is the utils file

#this file is used to store utility functions that are used throughout the app.

import json
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

def create_checkbox(label, description, preferences, key):
    """Create a checkbox layout with a tooltip."""
    container = QtWidgets.QWidget()
    checkbox = QtWidgets.QCheckBox(label, container)
    checkbox.setChecked(preferences.get(key, False))
    checkbox.stateChanged.connect(lambda: save_preferences(preferences, key, checkbox.isChecked()))
    layout = QtWidgets.QHBoxLayout(container)
    layout.addWidget(checkbox)
    layout.addStretch()
    container.setToolTip(description)
    return container

def create_slider(label, min_value, max_value, description, preferences, key):
    container = QtWidgets.QWidget()
    left = QtWidgets.QLabel(label, container)
    right = QtWidgets.QSlider(Qt.Horizontal, container)
    right.setRange(min_value, max_value)
    initial_value = preferences.get(key, (min_value + max_value) // 2)
    right.setValue(initial_value)
    right.setTickPosition(QtWidgets.QSlider.TicksBelow)
    right.setTickInterval(5)
    
    value_label = QtWidgets.QLabel(str(initial_value), container)
    value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    value_label.setMinimumWidth(30)  # Ensure enough space for the value
    
    def update_value(value):
        value_label.setText(str(value))
        save_preference(preferences, key, value)
    
    right.valueChanged.connect(update_value)
    
    layout = QtWidgets.QHBoxLayout(container)
    layout.addWidget(left)
    layout.addStretch()
    layout.addWidget(right)
    layout.addWidget(value_label)
    
    container.setToolTip(description)
    return container

def create_combobox_layout(label_text, options, description, preferences, combo_key, slider_key):
    container = QtWidgets.QWidget()
    
    left = QtWidgets.QLabel(label_text, container)
    
    middle = QtWidgets.QComboBox(container)
    middle.addItems(options)
    middle.setCurrentIndex(preferences.get(combo_key, 0))
    middle.currentIndexChanged.connect(lambda index: save_preference(preferences, combo_key, index))
    
    right = QtWidgets.QSlider(Qt.Horizontal, container)
    right.setRange(0, 100)
    right.setValue(preferences.get(slider_key, 50))
    right.setTickPosition(QtWidgets.QSlider.TicksBelow)
    right.setTickInterval(10)
    
    value_label = QtWidgets.QLabel(str(right.value()), container)
    value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    value_label.setMinimumWidth(30)
    
    def update_slider_value(value):
        value_label.setText(str(value))
        save_preference(preferences, slider_key, value)
    
    right.valueChanged.connect(update_slider_value)
    
    layout = QtWidgets.QHBoxLayout(container)
    layout.addWidget(left)
    layout.addWidget(middle)
    layout.addWidget(right)
    layout.addWidget(value_label)
    
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

def save_preference(preferences, key, value):
    preferences[key] = value
    save_preferences(PREFERENCES_FILE, preferences)

