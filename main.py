from best_alternative import BestAlternative
from data import data
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        table = Table(2, 2)

        best_alternative = BestAlternative(data)
        optimal_alternative = best_alternative.get_best_alternative()

        optimal_alternative_label = QLabel(optimal_alternative)

        layout.addWidget(table)
        layout.addWidget(optimal_alternative_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
