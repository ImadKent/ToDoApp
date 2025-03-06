from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QLineEdit, QGridLayout, QPushButton, QListWidget)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My ToDo App")

        # Layout
        self.parent_layout = QGridLayout()

        # Entry Field
        self.entry = QLineEdit()

        # Buttons
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_item)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_item)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_item)

        # List Widget
        self.list_widget = QListWidget()

        # Set buttons on layout
        self.parent_layout.addWidget(self.entry, 0, 0)
        self.parent_layout.addWidget(self.list_widget, 1, 0, )
        self.parent_layout.addWidget(self.add_button, 0, 1)
        self.parent_layout.addWidget(self.delete_button, 1, 1)
        self.parent_layout.addWidget(self.edit_button, 0, 2)

        container = QWidget()
        container.setLayout(self.parent_layout)
        self.setCentralWidget(container)

    def add_item(self):
        """Ajoute un élément à la liste."""
        text = self.entry.text()
        if text:  # Vérifie que l'entrée n'est pas vide
            self.list_widget.addItem(text)
            self.entry.clear()

    def delete_item(self):
        """Supprime l'élément sélectionné."""
        current_row = self.list_widget.currentRow()
        if current_row >= 0:  # Vérifie qu'il y a bien un élément sélectionné
            self.list_widget.takeItem(current_row)

    def edit_item(self):
        """Modifie l'élément sélectionné avec le texte de l'entrée."""
        current_item = self.list_widget.currentItem()
        if current_item:
            current_item.setText(self.entry.text())  # Change le texte de l'élément
        self.entry.clear()

# Exécution de l'application
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())
