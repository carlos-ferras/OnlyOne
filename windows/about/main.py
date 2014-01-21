import about 
from PyQt4 import QtGui, QtCore
import sys

class cMainAbout(about.Ui_Dialog):
		def __init__(self):
				self.Form = QtGui.QDialog()
				self.setupUi(self.Form)
				self.Form.show()


def main():
	app = QtGui.QApplication([""])
	f = cMainAbout()
	app.exec_()

if __name__=='__main__':
	main()