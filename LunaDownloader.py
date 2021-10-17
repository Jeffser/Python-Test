import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from __feature__ import snake_case, true_property

if __name__=="__main__":
    app = QApplication(sys.argv)
    link = app.clipboard().text()
    texto = QLabel(link)
    texto.alignment = Qt.AlignCenter
    texto.show()
    sys.exit(app.exec_())
