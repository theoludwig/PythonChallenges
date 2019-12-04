from PySide2 import QtWidgets # pip install PySide2

fenetres = [] # liste qui contient toutes les fenêtres ouvertes 

def mettreAJourNombreFenetre():
    for fenetre in fenetres:
        fenetre.resultatNombreFenetre.setText(f'Nombre de fenêtres : {len(fenetres)}')

def creerFenetre():
    fenetres.append(Fenetre())
    mettreAJourNombreFenetre()

class Fenetre(QtWidgets.QWidget):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.setWindowTitle('Application')
        self.resize(280, 50)
        layout = QtWidgets.QVBoxLayout(self)
        button = QtWidgets.QPushButton('Cliquez sur le bouton')
        self.resultatNombreFenetre = QtWidgets.QLineEdit(f'Nombre de fenêtres : 0')

        layout.addWidget(button)
        layout.addWidget(self.resultatNombreFenetre)
        button.clicked.connect(creerFenetre)
        self.show()

    def closeEvent(self, event):
        del fenetres[fenetres.index(self)]
        mettreAJourNombreFenetre()
        event.accept()

app = QtWidgets.QApplication([])
creerFenetre()
app.exec_()