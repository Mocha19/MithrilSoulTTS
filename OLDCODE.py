#this is old codefrom teh last time it was all in one file. we have gone far since then.


from PyQt5 import QtWidgets, QtCore



import sys

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
        self.tabs.addTab(self.create_tts_tab(), "TTS")
        self.tabs.addTab(self.create_preferences_tab(), "Preferences")

        # Main layout for the entire window
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        # Apply the initial dark mode style
        self.apply_styles()

    # Method to create the TTS tab
    def create_tts_tab(self):
        tts_widget = QtWidgets.QWidget()

        # Create UI elements for TTS
        self.text_input = QtWidgets.QLineEdit(tts_widget)
        self.text_input.setPlaceholderText("Enter your command...")

        self.submit_button = QtWidgets.QPushButton('Submit', tts_widget)
        self.history_box = QtWidgets.QTextEdit(tts_widget)
        self.history_box.setReadOnly(True)

        # Volume slider and buttons
        self.volume = 50
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, tts_widget)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(self.volume)
        self.volume_slider.setTickInterval(10)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.volume_label = QtWidgets.QLabel(f"Volume: {self.volume}", tts_widget)
        self.listen_button = QtWidgets.QPushButton('Listen', tts_widget)
        self.speak_button = QtWidgets.QPushButton('Speak', tts_widget)

        # Layout for volume slider and buttons
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.volume_slider, stretch=2)
        hbox.addWidget(self.volume_label, stretch=1)
        hbox.addWidget(self.listen_button)
        hbox.addWidget(self.speak_button)

        # Layout for TTS tab
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.history_box)
        vbox.addWidget(QtWidgets.QLabel("Volume"))
        vbox.addLayout(hbox)

        tts_widget.setLayout(vbox)
        return tts_widget

    # Method to create the Preferences tab
    def create_preferences_tab(self):
        preferences_widget = QtWidgets.QWidget()

        # Auto-Play TTS toggle
        self.autoplay_toggle = QtWidgets.QCheckBox("Auto-Play TTS", preferences_widget)
        self.autoplay_toggle.stateChanged.connect(self.toggle_autoplay)

        # Volume sliders for Speakers and Mic
        self.speaker_volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.speaker_volume_slider.setRange(0, 100)
        self.speaker_volume_slider.setValue(50)
        self.speaker_volume_label = QtWidgets.QLabel(f"Speaker Volume: {self.speaker_volume_slider.value()}")
        self.speaker_volume_slider.valueChanged.connect(lambda value: self.speaker_volume_label.setText(f"Speaker Volume: {value}"))

        self.mic_volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.mic_volume_slider.setRange(0, 100)
        self.mic_volume_slider.setValue(50)
        self.mic_volume_label = QtWidgets.QLabel(f"Mic Volume: {self.mic_volume_slider.value()}")
        self.mic_volume_slider.valueChanged.connect(lambda value: self.mic_volume_label.setText(f"Mic Volume: {value}"))

        # Startup behavior checkboxes
        self.startup_checkbox = QtWidgets.QCheckBox("Launch at Startup", preferences_widget)
        self.tray_checkbox = QtWidgets.QCheckBox("Minimize to System Tray", preferences_widget)

        # Theme toggle (Dark Mode/Light Mode)
        self.theme_toggle = QtWidgets.QCheckBox("Dark Mode", preferences_widget)
        self.theme_toggle.setChecked(True)  # Default to dark mode
        self.theme_toggle.stateChanged.connect(self.toggle_theme)

        # Font size slider
        self.font_size_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.font_size_slider.setRange(8, 24)
        self.font_size_slider.setValue(self.font_size)
        self.font_size_slider.valueChanged.connect(self.change_font_size)
        self.font_size_label = QtWidgets.QLabel(f"Font Size: {self.font_size_slider.value()}")

        # Set fixed size policy for all widgets in Preferences to avoid stretching
        self.autoplay_toggle.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.speaker_volume_slider.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mic_volume_slider.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.startup_checkbox.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.tray_checkbox.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.theme_toggle.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.font_size_slider.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

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

        preferences_widget.setLayout(vbox)
        return preferences_widget

    # Toggle auto-play TTS
    def toggle_autoplay(self, state):
        if state == QtCore.Qt.Checked:
            self.listen_button.setVisible(False)
            self.speak_button.setVisible(False)
            self.auto_play_label = QtWidgets.QLabel("AutoSpeak Activated", self)
            self.auto_play_label.setStyleSheet("background-color: #444; color: lightgreen; font-size: 16px; padding: 10px;")
            self.auto_play_label.setAlignment(QtCore.Qt.AlignCenter)
            self.layout().addWidget(self.auto_play_label)
        else:
            self.listen_button.setVisible(True)
            self.speak_button.setVisible(True)
            self.layout().removeWidget(self.auto_play_label)
            self.auto_play_label.deleteLater()

    # Toggle dark/light mode
    def toggle_theme(self, state):
        self.is_dark_mode = state == QtCore.Qt.Checked
        self.apply_styles()

    # Adjust font size and maintain current theme
    def change_font_size(self, value):
        self.font_size = value
        self.font_size_label.setText(f"Font Size: {value}")
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
    # Connect events
        self.submit_button.clicked.connect(self.submit_text)
        self.text_input.returnPressed.connect(self.submit_text)

    def set_volume(self, value):
        self.volume = value
        self.volume_label.setText(f"Volume: {value}")

    def submit_text(self):
        user_input = self.text_input.text()
        if user_input:
            translated_text = "Processing text: " + user_input
            self.history_box.append(f"Input: {user_input}\nResponse: {translated_text}")

# Create the application and window
app = QtWidgets.QApplication(sys.argv)
window = TTSApp()
window.show()
sys.exit(app.exec_())
