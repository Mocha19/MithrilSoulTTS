from PyQt5 import QtWidgets, QtCore

class PreferencesWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_app = parent  # Store a reference to the parent app
        self.init_ui()

    def init_ui(self):
        # Auto-Play TTS toggle
        self.autoplay_toggle = QtWidgets.QCheckBox("Auto-Play TTS", self)
        self.autoplay_toggle.stateChanged.connect(self.toggle_autoplay)

        # Volume sliders for Speakers and Mic
        self.speaker_volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.speaker_volume_slider.setRange(0, 100)
        self.speaker_volume_slider.setValue(50)
        self.speaker_volume_label = QtWidgets.QLabel(f"Speaker Volume: {self.speaker_volume_slider.value()}", self)
        self.speaker_volume_slider.valueChanged.connect(lambda value: self.speaker_volume_label.setText(f"Speaker Volume: {value}"))

        self.mic_volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.mic_volume_slider.setRange(0, 100)
        self.mic_volume_slider.setValue(50)
        self.mic_volume_label = QtWidgets.QLabel(f"Mic Volume: {self.mic_volume_slider.value()}", self)
        self.mic_volume_slider.valueChanged.connect(lambda value: self.mic_volume_label.setText(f"Mic Volume: {value}"))

        # Startup behavior checkboxes
        self.startup_checkbox = QtWidgets.QCheckBox("Launch at Startup", self)
        self.tray_checkbox = QtWidgets.QCheckBox("Minimize to System Tray", self)

        # Theme toggle (Dark Mode/Light Mode)
        self.theme_toggle = QtWidgets.QCheckBox("Dark Mode", self)
        self.theme_toggle.setChecked(True)  # Default to dark mode
        self.theme_toggle.stateChanged.connect(lambda state: self.parent_app.toggle_theme(state))

        # Font size slider
        self.font_size_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.font_size_slider.setRange(8, 24)
        self.font_size_slider.setValue(self.parent_app.font_size)
        self.font_size_slider.valueChanged.connect(lambda value: self.parent_app.change_font_size(value))
        self.font_size_label = QtWidgets.QLabel(f"Font Size: {self.font_size_slider.value()}", self)

        # Layout for Preferences tab
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.autoplay_toggle)
        vbox.addWidget(self.speaker_volume_label)
        vbox.addWidget(self.speaker_volume_slider)
        vbox.addWidget(self.mic_volume_label)
        vbox.addWidget(self.mic_volume_slider)
        vbox.addWidget(self.startup_checkbox)
        vbox.addWidget(self.tray_checkbox)
        vbox.addWidget(self.theme_toggle)
        vbox.addWidget(self.font_size_label)
        vbox.addWidget(self.font_size_slider)

        # Add a stretch at the end to push settings to the top and avoid gaps
        vbox.addStretch()

        self.setLayout(vbox)

    # Toggle auto-play TTS
    def toggle_autoplay(self, state):
        # Implementation of auto-play logic goes here
        pass
