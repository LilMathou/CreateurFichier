from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QSpinBox, QWidget, QPushButton, QFileDialog, \
    QComboBox, QLabel
import sys

class Formulaire(QWidget):
    def __init__(self):
        super().__init__()
        self.init_form()

    def init_form(self):
        self.setWindowTitle("Application de création de fichier")
        self.setGeometry(100, 100, 400, 300)

        self.chemin = None

        layout = QFormLayout()
        self.bouton_selection_dossier = QPushButton("Choisir un dossier", self)
        self.nom_fichier = QLineEdit()
        self.extensions_fichier = QComboBox()
        self.extensions_fichier.addItems([".sql", ".txt", ".json", ".py"])
        self.nombre_fichier = QSpinBox()
        self.nombre_fichier.setRange(1, 50)
        self.bouton_creation_fichier = QPushButton("Valider", self)
        self.texte_erreur = QLabel()

        layout.addRow(self.bouton_selection_dossier)
        layout.addRow("Nom", self.nom_fichier)
        layout.addRow("Extensions", self.extensions_fichier)
        layout.addRow("Nombre de fichier", self.nombre_fichier)
        layout.addRow(self.bouton_creation_fichier)
        layout.addRow(self.texte_erreur)

        self.setLayout(layout)

        self.bouton_selection_dossier.clicked.connect(self.ouvrir_dossier)
        self.bouton_creation_fichier.clicked.connect(self.creer_fichier)


    def ouvrir_dossier(self):
        chemin_dossier = QFileDialog.getExistingDirectory(self, "Choisir un dossier", "",)
        if chemin_dossier:
            self.chemin = chemin_dossier

    def creer_fichier(self):
        if self.chemin:
            for i in range(1, int(self.nombre_fichier.text())+1):
                with open(f"{self.chemin}/{self.nom_fichier.text()}{i}{self.extensions_fichier.currentText()}", "w") as fichier:
                    fichier.write(f"--{self.nom_fichier.text()}{i}\n")
        else:
            self.texte_erreur.setText("Dossier non selectionné")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Formulaire()
    window.show()
    sys.exit(app.exec())