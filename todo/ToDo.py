from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QScrollArea, QTextEdit, QLabel, \
    QHBoxLayout
from PySide6.QtCore import Qt, QSize


class ToDoItem(QWidget):
    """
    列表的item，需要自定义
    """

    def __init__(self, title_name):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.head = QWidget()
        self.head.setFixedHeight(30)
        title_label = QLabel(title_name)
        head_layout = QHBoxLayout(self.head)
        head_layout.addWidget(title_label, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.head, Qt.AlignmentFlag.AlignTop)

        self.detail = QListWidget()
        item = QListWidgetItem()
        item.setText("我是测试")
        item.setSizeHint(QSize(100, 30))
        self.detail.addItem(item)
        layout.addWidget(self.detail, Qt.AlignmentFlag.AlignCenter)

    def add_item(self, text):
        """
        添加item
        :param text:
        :return:
        """

class ToDoTitleEdit(QTextEdit):
    def __init__(self, scroll_view:QScrollArea):
        super().__init__()
        self.scroll_view = scroll_view

    def keyPressEvent(self, e):
        if e.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            # 插入新的Item
            text = self.toPlainText()
            if text is not None and text != '' and text.strip() != '':
                self.scroll_view.layout().addWidget(ToDoItem(text))
            self.clear()
        else:
            super().keyPressEvent(e)

class ToDo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        scroll_view = QScrollArea()
        scroll_view.setLayout(QVBoxLayout(scroll_view))
        layout.addWidget(scroll_view, Qt.AlignmentFlag.AlignCenter)

        group_edit = ToDoTitleEdit(scroll_view)
        group_edit.setFixedHeight(30)
        layout.addWidget(group_edit, Qt.AlignmentFlag.AlignBottom)
