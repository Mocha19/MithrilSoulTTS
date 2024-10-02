import sys
from PyQt5 import QtWidgets
from oldMocha.app import TTSApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TTSApp()
    window.show()
    sys.exit(app.exec_())