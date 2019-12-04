from PySide2 import QtWidgets, QtGui, QtCore
from functools import partial
from custom_ui.fenetrePrincipale import Ui_form_calculatrice

# Formate les nombres avec des espaces (ex : 76120 = 76 120)
def formatNumberResult(x):
	if isinstance(x, int):
		x = int(x)
	else:
		x = float(x)
	return '{:,}'.format(x).replace(',', ' ')

class Calculatrice(Ui_form_calculatrice, QtWidgets.QWidget):
	def __init__(self):
		super(Calculatrice, self).__init__()
		self.setupUi(self)
		self.modificationSetupUi()
		self.setupConnections()
		self.setupRaccourcisClavier()
		self.show()

	def modificationSetupUi(self):
		self.btns_nombres = [] # liste qui contient tout les chiffres de 0 à 9
		for i in range(self.gridLayout.count()):
			widget = self.gridLayout.itemAt(i).widget()
			if isinstance(widget, QtWidgets.QPushButton):
				widget.setStyleSheet('QPushButton:hover {color: #5b5c5c;}')
				if widget.text().isdigit(): 
					self.btns_nombres.append(widget) 

	def setupConnections(self):
		for btn in self.btns_nombres:
			btn.clicked.connect(partial(self.btnNombrePressed, btn.text()))

		self.btn_moins.clicked.connect(partial(self.btnOperationPressed, '-'))
		self.btn_plus.clicked.connect(partial(self.btnOperationPressed, '+'))
		self.btn_mult.clicked.connect(partial(self.btnOperationPressed, '*'))
		self.btn_div.clicked.connect(partial(self.btnOperationPressed, '/'))
		self.btn_point.clicked.connect(partial(self.btnOperationPressed, '.'))

		self.btn_egal.clicked.connect(self.calculOperation)
		self.btn_c.clicked.connect(self.supprimerResultat)

	def setupRaccourcisClavier(self):
		for btn in range(10):
			QtWidgets.QShortcut(QtGui.QKeySequence(btn), self, partial(self.btnNombrePressed, btn)) 

		QtWidgets.QShortcut(QtGui.QKeySequence('+'), self, partial(self.btnOperationPressed, '+'))
		QtWidgets.QShortcut(QtGui.QKeySequence('-'), self, partial(self.btnOperationPressed, '-'))
		QtWidgets.QShortcut(QtGui.QKeySequence('*'), self, partial(self.btnOperationPressed, '*'))
		QtWidgets.QShortcut(QtGui.QKeySequence('/'), self, partial(self.btnOperationPressed, '/'))
		QtWidgets.QShortcut(QtGui.QKeySequence('.'), self, partial(self.btnOperationPressed, '.'))
		
		QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close) 
		QtWidgets.QShortcut(QtGui.QKeySequence('Return'), self, self.calculOperation) 
		QtWidgets.QShortcut(QtGui.QKeySequence('Entrer'), self, self.calculOperation) 
		QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self, self.supprimerResultat) 

	def btnNombrePressed(self, bouton):
		"""Fonction activée quand l'utilisateur appuie sur un chiffre (0-9)"""
		resultat = self.le_resultat.text()
		if resultat == '0':
			self.le_resultat.setText(bouton)
		else:
			self.le_resultat.setText(resultat + bouton)

	def btnOperationPressed(self, operation):
		"""Fonction activée quand l'utilisateur appuie sur une touche d'opération (+, -, /, *)"""
		resultat = self.le_resultat.text()
		self.le_resultat.setText(resultat + " " + operation + " ")

	def supprimerResultat(self):
		"""On reset le texte des deux LineEdit"""
		self.le_resultat.setText('0')
		self.le_operation.setText('')

	def calculOperation(self):
		resultat = self.le_resultat.text()

		# On ajoute le nombre actuel dans le LineEdit resultat au LineEdit operation
		self.le_operation.setText(resultat)
		
		# On evalue (et calcule) le resultat de l'opération
		resultatOperation = eval(self.le_operation.text().replace(" ", ""))
		
		# On met le resultat final dans le LineEdit resultat
		self.le_resultat.setText(formatNumberResult(resultatOperation))

app = QtWidgets.QApplication([])
fenetre = Calculatrice()
app.exec_()