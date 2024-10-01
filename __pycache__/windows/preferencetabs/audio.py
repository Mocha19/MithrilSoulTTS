# audio.py
# Last edit: 2024-09-30 19:08
# v1.05 (saved preferences to file)

import json
import os
from PyQt5 import QtWidgets, QtCore

PREFERENCES_FILE = 'audio_preferences.json'

def create_audio_tab(parent):
    """
    Create and return the audio settings tab.
    
    :param parent: The parent widget
    :return: QWidget containing the audio settings tab
    """
    audio_tab = QtWidgets.QWidget()

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

    # Noise Suppression
    parent.noise_checkbox = QtWidgets.QCheckBox("Noise Suppression")
    noise_container = create_checkbox_layout(parent.noise_checkbox, "Reduce background noise in your microphone input")

    # Echo Cancellation
    parent.echo_checkbox = QtWidgets.QCheckBox("Echo Cancellation")
    echo_container = create_checkbox_layout(parent.echo_checkbox, "Reduce echo in your microphone input")

    # Auto-Play TTS
    parent.autoplay_checkbox = QtWidgets.QCheckBox("Auto-Play TTS")
    autoplay_container = create_checkbox_layout(parent.autoplay_checkbox, "Play TTS when a message is received")

    # Real-Time Audio Stream
    parent.instant_checkbox = QtWidgets.QCheckBox("Instant Audio Stream")
    instant_container = create_checkbox_layout(parent.instant_checkbox, "Stream real-time audio")

    # Mic
    parent.mic_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    parent.mic_slider.setRange(0, 100)
    parent.mic_slider.setValue(50)
    parent.mic_label = QtWidgets.QLabel("Microphone:")
    parent.mic_dropdown = QtWidgets.QComboBox()
    parent.mic_dropdown.addItems(["Default Microphone", "Mic 1", "Mic 2"])
    mic_container = create_combobox_layout(parent.mic_label, parent.mic_dropdown, parent.mic_slider, "Choose the microphone input device")

    # Speaker
    parent.speaker_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    parent.speaker_slider.setRange(0, 100)
    parent.speaker_slider.setValue(50)
    parent.speaker_label = QtWidgets.QLabel("Speaker:")
    parent.speaker_dropdown = QtWidgets.QComboBox()
    parent.speaker_dropdown.addItems(["Default Speaker", "Speaker 1", "Speaker 2"])
    speaker_container = create_combobox_layout(parent.speaker_label, parent.speaker_dropdown, parent.speaker_slider, "Choose the audio output device")

    # Narrator (combined with Narrator Volume)
    parent.narrator_dropdown = QtWidgets.QComboBox()
    parent.narrator_dropdown.addItems(["Alloy", "Echo", "Fable", "Onyx", "Nova", "Shimmer"])
    parent.narrator_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    parent.narrator_slider.setRange(0, 100)
    parent.narrator_slider.setValue(50)
    parent.narrator_label = QtWidgets.QLabel("Narrator:")
    narrator_container = create_combobox_layout(parent.narrator_label, parent.narrator_dropdown, parent.narrator_slider, "Choose the default narrator and set its volume")

    # Narrator Speed (separate)
    parent.narrator_speed_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    parent.narrator_speed_slider.setRange(0, 100)
    parent.narrator_speed_slider.setValue(50)
    parent.narrator_speed_label = QtWidgets.QLabel("Narrator Speed:")
    narrator_speed_container = create_slider_layout(parent.narrator_speed_label, parent.narrator_speed_slider, "Choose the default narrator speed")

    # Connect signals
    parent.mic_slider.valueChanged.connect(lambda v: parent.mic_label.setText(f"Microphone: {v}%"))
    parent.speaker_slider.valueChanged.connect(lambda v: parent.speaker_label.setText(f"Speaker: {v}%"))
    parent.narrator_slider.valueChanged.connect(lambda v: parent.narrator_label.setText(f"Narrator: {v}%"))
    parent.narrator_speed_slider.valueChanged.connect(lambda v: parent.narrator_speed_label.setText(f"Narrator Speed: {v}%"))

    # Connect signals to save preferences
    parent.noise_checkbox.stateChanged.connect(lambda: save_audio_preferences(parent))
    parent.echo_checkbox.stateChanged.connect(lambda: save_audio_preferences(parent))
    parent.autoplay_checkbox.stateChanged.connect(lambda: save_audio_preferences(parent))
    parent.instant_checkbox.stateChanged.connect(lambda: save_audio_preferences(parent))
    parent.mic_slider.valueChanged.connect(lambda: save_audio_preferences(parent))
    parent.mic_dropdown.currentIndexChanged.connect(lambda: save_audio_preferences(parent))
    parent.speaker_slider.valueChanged.connect(lambda: save_audio_preferences(parent))
    parent.speaker_dropdown.currentIndexChanged.connect(lambda: save_audio_preferences(parent))
    parent.narrator_dropdown.currentIndexChanged.connect(lambda: save_audio_preferences(parent))
    parent.narrator_slider.valueChanged.connect(lambda: save_audio_preferences(parent))
    parent.narrator_speed_slider.valueChanged.connect(lambda: save_audio_preferences(parent))

    # Layout for Audio tab
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(noise_container)
    vbox.addWidget(echo_container)
    vbox.addWidget(autoplay_container)
    vbox.addWidget(instant_container)
    vbox.addSpacing(10)
    vbox.addWidget(mic_container)
    vbox.addWidget(speaker_container)
    vbox.addSpacing(10)
    vbox.addWidget(narrator_container)
    vbox.addWidget(narrator_speed_container)

    audio_tab.setLayout(vbox)

    # Load preferences
    load_audio_preferences(parent)

    return audio_tab

def save_audio_preferences(parent):
    """Save audio preferences to a JSON file."""
    preferences = {
        'noise_suppression': parent.noise_checkbox.isChecked(),
        'echo_cancellation': parent.echo_checkbox.isChecked(),
        'auto_play_tts': parent.autoplay_checkbox.isChecked(),
        'instant_audio_stream': parent.instant_checkbox.isChecked(),
        'mic_volume': parent.mic_slider.value(),
        'mic_device': parent.mic_dropdown.currentIndex(),
        'speaker_volume': parent.speaker_slider.value(),
        'speaker_device': parent.speaker_dropdown.currentIndex(),
        'narrator': parent.narrator_dropdown.currentIndex(),
        'narrator_volume': parent.narrator_slider.value(),
        'narrator_speed': parent.narrator_speed_slider.value()
    }
    
    with open(PREFERENCES_FILE, 'w') as f:
        json.dump(preferences, f)

def load_audio_preferences(parent):
    """Load audio preferences from a JSON file and apply them."""
    if not os.path.exists(PREFERENCES_FILE):
        return  # No preferences file exists yet
    
    with open(PREFERENCES_FILE, 'r') as f:
        preferences = json.load(f)
    
    parent.noise_checkbox.setChecked(preferences.get('noise_suppression', False))
    parent.echo_checkbox.setChecked(preferences.get('echo_cancellation', False))
    parent.autoplay_checkbox.setChecked(preferences.get('auto_play_tts', False))
    parent.instant_checkbox.setChecked(preferences.get('instant_audio_stream', False))
    parent.mic_slider.setValue(preferences.get('mic_volume', 50))
    parent.mic_dropdown.setCurrentIndex(preferences.get('mic_device', 0))
    parent.speaker_slider.setValue(preferences.get('speaker_volume', 50))
    parent.speaker_dropdown.setCurrentIndex(preferences.get('speaker_device', 0))
    parent.narrator_dropdown.setCurrentIndex(preferences.get('narrator', 0))
    parent.narrator_slider.setValue(preferences.get('narrator_volume', 50))
    parent.narrator_speed_slider.setValue(preferences.get('narrator_speed', 50))

    # Update labels
    parent.mic_label.setText(f"Microphone: {parent.mic_slider.value()}%")
    parent.speaker_label.setText(f"Speaker: {parent.speaker_slider.value()}%")
    parent.narrator_label.setText(f"Narrator: {parent.narrator_slider.value()}%")
    parent.narrator_speed_label.setText(f"Narrator Speed: {parent.narrator_speed_slider.value()}%")