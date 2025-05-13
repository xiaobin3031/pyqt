from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QHBoxLayout, QStackedWidget

from todo.ToDo import ToDo


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")
        self.resize(500, 600)

        layout = QHBoxLayout(self)

        # navs
        self.list_widget = QListWidget()
        item = QListWidgetItem()
        item.setText("ToDo")
        self.list_widget.addItem(item)
        item = QListWidgetItem()
        item.setText("Email")
        self.list_widget.addItem(item)
        # self.list_widget.itemClicked.connect(self.nav_click)
        self.list_widget.currentRowChanged.connect(self.nav_row_change)

        # stacked
        self.center_widget = QStackedWidget()
        self.center_widget.addWidget(ToDo())
        # self.center_widget.addWidget(Email())

        layout.addWidget(self.list_widget, QtCore.Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.center_widget, QtCore.Qt.AlignmentFlag.AlignCenter)

    def nav_row_change(self, index):
        self.center_widget.setCurrentIndex(index)