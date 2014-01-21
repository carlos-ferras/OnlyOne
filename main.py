#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import threading
import string as s
import action.action
import windows.main as win
import windows.about.main as win2



function=action.action.action()

class TestItem():
    def __init__(self, tupla,grupo, checked):
        self.checked = checked
        self.name = tupla
	self.grupo=grupo

class StbTreeView(QAbstractListModel):
	
    def __init__(self, args, parent=None):
        super(StbTreeView, self).__init__(parent)
	self.grupos=len(args)
        self.args = []
	pos=0
	self.marc=[]
	self.noMarc=[]
	self.indice=0
	self.cantGrupos=0
        for grupo in args:
		for tupla in grupo:
			self.args.append(TestItem(tupla,pos, False))
			self.noMarc.append(self.indice)
			self.indice=self.indice+1
		self.args.append(TestItem([win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'),"","",""],pos, False))
		pos=pos+1
	del self.args[len(self.args)-1]

    def rowCount(self, parent):
        return len(self.args)

    def flags(self, index):
        return  Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            return  self.args[row].name[0]+win._fromUtf8("▆▆▆")+self.args[row].name[2]+win._fromUtf8("▆▆▆")+self.args[row].name[3]+win._fromUtf8("▆▆▆")+self.args[row].name[1]

        if role == Qt.CheckStateRole:
            row = index.row()
            if self.args[row].checked == False:
		if self.args[row].name[0]!=win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
			function.Desmarcar(self.args[row].name)
			esta=False
			for k in self.noMarc:
				if k==row:
					esta=True
			if esta==False:
				self.noMarc.append(row)
			for k in range(len(self.marc)):
				if self.marc[k]==row:
					del self.marc[k]
					break
			return QVariant(Qt.Unchecked)
		else:
			return -1
            else:
		if self.args[row].name[0]!=win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
			function.Marcar(self.args[row].name)
			esta=False
			for k in self.marc:
				if k==row:
					esta=True
			if esta==False:
				self.marc.append(row)
			for k in range(len(self.noMarc)):
				if self.noMarc[k]==row:
					del self.noMarc[k]
					break
			return QVariant(Qt.Checked)
		else:
			return -1

    def setData(self, index, value, role):
        if role == Qt.CheckStateRole:
            row = index.row()
            self.args[row].checked = not self.args[row].checked             
        return True
	
    def actCantGrupos(self):
	    self.cantGrupos=0
	    try:
		cambio=[self.args[0].grupo]
		if cambio[0]>0:
			self.cantGrupos=1
		for i in range(len(self.args)):
		    find=False
		    for j in cambio:
			    if j==self.args[i].grupo:
				find=True
		    if find==False:
			    cambio.append(self.args[i].grupo)
			    self.cantGrupos=self.cantGrupos+1
	    except:
		    pass
			    
    def organizarGrupos(self):
	    for i in range(len(self.args)):
		    grupI=self.args[i].grupo
		    for j in range(i,len(self.args)):
			    grupJ=self.args[j].grupo
			    if grupI>grupJ:
				    tem=self.args[i]
				    self.args[i]=self.args[j]
				    self.args[j]=tem
				    for k in range(len(self.noMarc)):
					    if self.noMarc[k]==i:
						    self.noMarc[k]=j
					    if self.noMarc[k]==j:
						    self.noMarc[k]=i
				    for k in range(len(self.marc)):
					    if self.marc[k]==i:
						    self.marc[k]=j
					    if self.marc[k]==j:
						    self.marc[k]=i
						    
    def ponerSeparador(self):
	    new=[]
	    try:
		    actual=self.args[0].grupo
	    except:
		    return -1
	    for i in range(len(self.args)):
		    if self.args[i].name[0]==win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
			    continue
		    if actual==self.args[i].grupo:
			    new.append(self.args[i])
		    else:
			     new.append(TestItem([win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'),"","",""],actual, False))
			     actual=self.args[i].grupo
			     new.append(self.args[i])
	    self.args=new
						    
	
    def marcar(self):
	    self.marc=[]
	    for i in range(len(self.args)):
		    if self.args[i].name[0]==win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
			    continue
		    self.args[i].checked=True
		    self.marc.append(i)
	    self.noMarc=[]
            
	    
    def desmarcar(self):
	    self.noMarc=[]
	    for i in range(len(self.args)):
		    if self.args[i].name[0]==win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
			    continue
		    self.args[i].checked=False
		    self.noMarc.append(i)
	    self.marc=[]
	    
		    
    def dejarUno(self):
	    leng=self.grupos
	    pos=0
	    self.marc=[]
	    self.noMarc=[]
	    try:
		    self.args[0].checked=False
	    except:
		    return -1
	    self.noMarc.append(0)
	    for i in range(1,len(self.args)):
		    if pos==self.args[i].grupo:
			    if self.args[i].name[0]==win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
				    continue
			    self.args[i].checked=True
			    self.marc.append(i)
		    else:
			    self.args[i].checked=False
			    self.noMarc.append(i)
			    pos=pos+1
			    
    def marcarEncontrados(self,encontrados):
	    for i in range(len(self.args)):
		    if self.args[i].name[0]==win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'):
			    continue
		    for j in range(len(encontrados)):
			    if self.args[i].name[0]==encontrados[j][0]:
					esta=False
					for k in self.marc:
						if k==i:
							esta=True
					if esta==False:
						self.marc.append(i)
					for k in range(len(self.noMarc)):
						if self.noMarc[k]==i:
							del self.noMarc[k]
							break
					self.args[i].checked=True
					
    def oTipo(self,org):
	organizados=org
	
	pos=0
	self.marc=[]
	self.noMarc=[]
	self.indice=0
	
	borrar=[]
	
	for i in range(len(organizados)):
		for j in range(len(organizados[i])):
			esta=False
			for k in range(len(self.args)):
				if organizados[i][j][0]==self.args[k].name[0]:
					esta=True
					break
			if esta==False:
				borrar.append([i,j])
	for i in borrar:
		del organizados[i[0]][i[1]]
	
	self.args = []		
	
        for grupo in organizados:
		for tupla in grupo:
			self.args.append(TestItem(tupla,pos, False))
			self.noMarc.append(self.indice)
			self.indice=self.indice+1
		self.args.append(TestItem([win._fromUtf8('▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆'),"","",""],pos, False))
		pos=pos+1
	del self.args[len(self.args)-1]

			    
    def actualizarListaConMarcados(self):
	    new=[]
	    for i in self.marc:
		    new.append(self.args[i])
	    self.args=new
	    self.marc=[]
	    for i in range(len(new)):
		    self.marc.append(i)	    
	    self.noMarc=[]
	    self.actCantGrupos()
	    self.organizarGrupos()	   
	    self.ponerSeparador()
	    
    def actualizarListaConNoMarcados(self):
	    new=[]
	    for i in self.noMarc:
		    new.append(self.args[i])
	    self.args=new
	    self.noMarc=[]
	    for i in range(len(new)):
		    self.noMarc.append(i)	    
	    self.marc=[]
	    self.actCantGrupos()
	    self.organizarGrupos()
	    self.ponerSeparador()

class cMainWindow(win.Ui_MainWindow):
	def __init__(self):
		self.form1 =QMainWindow()
		self.setupUi(self.form1)
		self.form1.show()	
		self.form1.setStyleSheet("font-size: 13px;")
		self.pushButton_6.clicked.connect(self.RealizarBusqueda)
		self.pushButton_7.clicked.connect(self.AdicionarTipos)
		self.toolButton.clicked.connect(self.fuenteMas)
		self.toolButton_2.clicked.connect(self.fuenteMenos)
		self.pushButton_5.clicked.connect(self.language)
		self.pushButton_40.clicked.connect(self.spanish)
		self.pushButton_41.clicked.connect(self.english)
		self.pushButton_42.clicked.connect(self.chinese)
		self.pushButton_43.clicked.connect(self.japanese)
		self.pushButton_45.clicked.connect(self.german)
		self.pushButton_48.clicked.connect(self.russian)
		self.pushButton_47.clicked.connect(self.italian)
		self.pushButton_49.clicked.connect(self.portuguese)
		self.pushButton_46.clicked.connect(self.french)
		self.pushButton_44.clicked.connect(self.arabic)
		
		self.lineEdit_2.textChanged.connect(self.EvtText)
		self.listWidget.clicked.connect( self.escoger)
		self.lineEdit_3.textChanged.connect(self.EvtText2)
		self.listWidget_2.clicked.connect( self.escoger2)
		self.pushButton_88.clicked.connect( self.addConE)
		self.pushButton_85.clicked.connect( self.addSinE)
		
		self.pushButton_10.clicked.connect(self.MarcarTodos)
		self.pushButton_10.setEnabled(False)
		self.pushButton_11.clicked.connect(self.MarcarTodosMenosUno)
		self.pushButton_11.setEnabled(False)
		self.pushButton_12.clicked.connect(self.DesmarcarTodos)
		self.pushButton_12.setEnabled(False)
		self.pushButton_66.clicked.connect(self.Encontrar)
		self.pushButton_66.setEnabled(False)
		self.pushButton_13.clicked.connect(self.MarcarEncontrados)
		self.pushButton_13.setEnabled(False)

		self.pushButton_14.clicked.connect(self.BorrarMarcados)
		self.pushButton_14.setEnabled(False)
		self.pushButton_15.clicked.connect(self.BorrarNoMarcados)
		self.pushButton_15.setEnabled(False)
		self.pushButton_16.clicked.connect(self.BorrarTemporales)
		self.pushButton_16.setEnabled(False)
		self.pushButton_17.clicked.connect(self.BorrarDirectoriosVacios)
		self.pushButton_17.setEnabled(False)
		
		self.pushButton_9.clicked.connect(self.oPeso)
		self.pushButton_9.setEnabled(False)
		self.pushButton_8.clicked.connect(self.oTipo)
		self.pushButton_8.setEnabled(False)
		self.pushButton_18.clicked.connect(self.oModif)
		self.pushButton_18.setEnabled(False)
		
		self.porPeso="mayor"
		self.porFecha="mayor"
		
		self.lang=0
		self.cantCE=0
		self.cantSE=0
				
		self.pushButton.clicked.connect(self.about)
		self.pushButton_2.clicked.connect(self.help)
		self.pushButton_3.clicked.connect(self.face)
		
		self.treeView.clicked.connect(self.data)
	
	def help(self):
		pass
	
	def face(self):
		import webbrowser
		webbrowser.open('https://www.facebook.com/freeonlyone?ref=ts&fref=ts')
	
	def  about(self):
		_fromUtf8 = QString.fromUtf8
		self.groupBox_343 = QGroupBox()
		self.groupBox_343.setGeometry(QRect(200, 300, 687, 276))
		self.groupBox_343.setMinimumSize(QSize(687, 276))
		self.groupBox_343.setMaximumSize(QSize(687, 276))
		self.groupBox_343.setStyleSheet(_fromUtf8("background-color:#f7f7f7;\n"
"color:#a5a5a5;"))
		self.groupBox_343.setTitle(_fromUtf8(""))
		self.groupBox_343.setObjectName(_fromUtf8("groupBox_343"))
		self.label_344 = QLabel(self.groupBox_343)
		self.label_344.setGeometry(QRect(0, 40, 181, 171))
		self.label_344.setText(_fromUtf8(""))
		self.label_344.setPixmap(QPixmap(_fromUtf8("img/logo.png")))
		self.label_344.setScaledContents(True)
		self.label_344.setObjectName(_fromUtf8("label_344"))
		self.label_345 = QLabel(self.groupBox_343)
		self.label_345.setGeometry(QRect(200, 0, 191, 51))
		font = QFont()
		font.setFamily(_fromUtf8("Century Schoolbook L"))
		font.setPointSize(30)
		font.setBold(True)
		font.setWeight(75)
		self.label_345.setFont(font)
		self.label_345.setStyleSheet(_fromUtf8("color:#555555;"))
		self.label_345.setObjectName(_fromUtf8("label_345"))
		self.textEdit_346 = QTextEdit(self.groupBox_343)
		self.textEdit_346.setGeometry(QRect(190, 50, 491, 171))
		sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(3)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.textEdit_346.sizePolicy().hasHeightForWidth())
		self.textEdit_346.setSizePolicy(sizePolicy)
		self.textEdit_346.setMinimumSize(QSize(491, 171))
		self.textEdit_346.setMaximumSize(QSize(491, 171))
		font = QFont()
		font.setFamily(_fromUtf8("FreeSerif"))
		font.setPointSize(10)
		font.setBold(False)
		font.setWeight(50)
		self.textEdit_346.setFont(font)
		self.textEdit_346.setStyleSheet(_fromUtf8("color:#111111;"))
		self.textEdit_346.setFrameShape(QFrame.NoFrame)
		self.textEdit_346.setFrameShadow(QFrame.Plain)
		self.textEdit_346.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.textEdit_346.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.textEdit_346.setReadOnly(True)
		self.textEdit_346.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
		self.textEdit_346.setObjectName(_fromUtf8("textEdit_346"))
		self.groupBox_347 = QGroupBox(self.groupBox_343)
		self.groupBox_347.setGeometry(QRect(0, 230, 691, 41))
		self.groupBox_347.setStyleSheet(_fromUtf8("background-color:#ebebeb;"))
		self.groupBox_347.setTitle(_fromUtf8(""))
		self.groupBox_347.setObjectName(_fromUtf8("groupBox_347"))
		self.pushButton_348 = QPushButton(self.groupBox_347)
		self.pushButton_348.setGeometry(QRect(0, 10, 201, 27))
		font = QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_348.setFont(font)
		self.pushButton_348.setStyleSheet(_fromUtf8("color:#338ae9;\n"
"border-radius:15px;\n"
""))
		self.pushButton_348.setCheckable(False)
		self.pushButton_348.setDefault(False)
		self.pushButton_348.setFlat(False)
		self.pushButton_348.setObjectName(_fromUtf8("pushButton_348"))
		self.pushButton_349 = QPushButton(self.groupBox_347)
		self.pushButton_349.setGeometry(QRect(500, 10, 181, 27))
		font = QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_349.setFont(font)
		self.pushButton_349.setLayoutDirection(Qt.RightToLeft)
		self.pushButton_349.setStyleSheet(_fromUtf8("color:#338ae9;\n"
"border-radius:15px;\n"
""))
		self.pushButton_349.setCheckable(False)
		self.pushButton_349.setDefault(False)
		self.pushButton_349.setFlat(False)
		self.pushButton_349.setObjectName(_fromUtf8("pushButton_349"))
		self.pushButton_350 = QPushButton(self.groupBox_347)
		self.pushButton_350.setGeometry(QRect(220, 10, 261, 27))
		font = QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_350.setFont(font)
		self.pushButton_350.setStyleSheet(_fromUtf8("color:#338ae9;\n"
"border-radius:15px;\n"
""))
		self.pushButton_350.setCheckable(False)
		self.pushButton_350.setDefault(False)
		self.pushButton_350.setFlat(False)
		self.pushButton_350.setObjectName(_fromUtf8("pushButton_350"))


		self.label_345.setText(QApplication.translate("Dialog", "OnlyOne", None, QApplication.UnicodeUTF8))
		self.textEdit_346.setHtml(QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'FreeSerif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Novason\'; font-size:12pt; font-weight:600;\">OnlyOne, gana espacio en menos tiempo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Novason\'; font-size:12pt; font-weight:600;\">1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Novason\';\">OnlyOne es una herramienta que todos necesitamos, diseñada para las manos del usuario más inexperto, encuentre los ficheros repetidos dentro de sus directorios con más información, elimínelos, no son necesarios....solo ocupan nuestro espacio.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Novason\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Novason\'; font-size:8pt; font-weight:600;\">Desarrollado por Carlos Manuel Ferrás, Pavel Rolando Rondón, Alfredo Ríos Fuentes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Novason\'; font-size:8pt; font-weight:600;\">Universidad de las Ciencias Informáticas</span></p></body></html>", None, QApplication.UnicodeUTF8))
		self.pushButton_348.setText(QApplication.translate("Dialog", "Infoprmación de licencia", None, QApplication.UnicodeUTF8))
		self.pushButton_349.setText(QApplication.translate("Dialog", "Descripción detallada", None, QApplication.UnicodeUTF8))
		self.pushButton_350.setText(QApplication.translate("Dialog", "Contácte con los desarolladores", None, QApplication.UnicodeUTF8))
		
		self.groupBox_343.setWindowTitle(QApplication.translate("", "OnlyOne", None, QApplication.UnicodeUTF8))
		self.groupBox_343.show()
		self.pushButton_348.clicked.connect(self.licencia)
		self.pushButton_349.clicked.connect(self.descripcion)
		self.pushButton_350.clicked.connect(self.contacto)
		
	def licencia(self):
		pass
		
	def descripcion(self):
		pass
		
	def contacto(self):
		pass
	
	def oTipo(self):
		function.OrganizarTipo()
		self.model.oTipo(function.getRepetidos())
		
	def oModif(self):
		function.OrganizarFecha(self.porFecha)
		if (self.porFecha=="mayor"):
			self.porFecha="menor"
		else:
			self.porFecha="mayor"
		self.model.oTipo(function.getRepetidos())

	
	def oPeso(self):
		function.OrganizarPeso(self.porPeso)
		if (self.porPeso=="mayor"):
			self.porPeso="menor"
		else:
			self.porPeso="mayor"
		self.model.oTipo(function.getRepetidos())
		
		
	def Error(self,error):
		_fromUtf8 = QString.fromUtf8
		self.groupBox_777 = QGroupBox()
		self.groupBox_777.setGeometry(QRect(270, 150, 391, 211))
		self.groupBox_777.setMinimumSize(QSize(391, 211))
		self.groupBox_777.setMaximumSize(QSize(391, 211))
		self.groupBox_777.setStyleSheet(_fromUtf8("background-color:#ebebeb;"))
		self.groupBox_777.setTitle(_fromUtf8(""))
		self.groupBox_777.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
		self.groupBox_777.setFlat(True)
		self.groupBox_777.setCheckable(False)
		self.groupBox_777.setObjectName(_fromUtf8("groupBox_777"))
		self.label_777 = QLabel(self.groupBox_777)
		self.label_777.setGeometry(QRect(0, 0, 391, 31))
		font = QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label_777.setFont(font)
		self.label_777.setStyleSheet(_fromUtf8("background-color:#ebebeb;color:red;"))
		self.label_777.setFrameShape(QFrame.WinPanel)
		self.label_777.setFrameShadow(QFrame.Raised)
		self.label_777.setText(_fromUtf8(""))
		self.label_777.setAlignment(Qt.AlignCenter)
		self.label_777.setObjectName(_fromUtf8("label_777"))
		self.plainTextEdit_777 = QPlainTextEdit(self.groupBox_777)
		self.plainTextEdit_777.setGeometry(QRect(0, 30, 391, 155))
		font = QFont()
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(50)
		font.setStrikeOut(False)
		self.plainTextEdit_777.setFont(font)
		self.plainTextEdit_777.setMouseTracking(False)
		self.plainTextEdit_777.setContextMenuPolicy(Qt.DefaultContextMenu)
		self.plainTextEdit_777.setStyleSheet(_fromUtf8("background-color:#f7f7f7;border-color:red;"))
		self.plainTextEdit_777.setInputMethodHints(Qt.ImhNone)
		self.plainTextEdit_777.setFrameShape(QFrame.WinPanel)
		self.plainTextEdit_777.setFrameShadow(QFrame.Sunken)
		self.plainTextEdit_777.setLineWidth(1)
		self.plainTextEdit_777.setMidLineWidth(0)
		self.plainTextEdit_777.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.plainTextEdit_777.setPlainText(_fromUtf8(""))
		self.plainTextEdit_777.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
		self.plainTextEdit_777.setBackgroundVisible(False)
		self.plainTextEdit_777.setCenterOnScroll(False)
		self.plainTextEdit_777.setObjectName(_fromUtf8("plainTextEdit_777"))
		
		lista=s.split(error,":")
		self.label_777.setText(win._fromUtf8("ErrorArchivosNoBorrados:"))
		self.plainTextEdit_777.appendPlainText("No se pudo borrar los siguientes archivos:\n")
		errores=s.split(lista[2],"***")
		for e in errores:
			self.plainTextEdit_777.appendPlainText(win._fromUtf8(e+"\n"))
			
		self.groupBox_777.setWindowTitle(QApplication.translate("", "Error", None, QApplication.UnicodeUTF8))
		self.groupBox_777.show()
		
	
	def BorrarMarcados(self):
		if self.model.marc!=[]:
			self.model.actualizarListaConNoMarcados()
			error=function.BorrarMarcados()
			self.data()
			if error!='':
				self.Error(error)
			self.label_8.setText(win._fromUtf8(str(self.model.cantGrupos+1)))
			self.label_9.setText(win._fromUtf8(str(len(self.model.args)-self.model.cantGrupos)))
			
		
			
	def BorrarNoMarcados(self):
		if self.model.noMarc!=[]:
			self.model.actualizarListaConMarcados()
			error=function.BorrarNoMarcados()
			self.data()
			if error!='':
				self.Error(error)
			self.label_8.setText(win._fromUtf8(str(self.model.cantGrupos+1)))
			self.label_9.setText(win._fromUtf8(str(len(self.model.args)-self.model.cantGrupos)))
		
	def BorrarTemporales(self):
		error=function.BorrarTemporales()
		self.data()
		if error!='':
			self.Error(error)
		
	def BorrarDirectoriosVacios(self):
		error=function.BorrarDirectoriosVacios()
		self.data()
		if error!='':
			self.Error(error)
		
	def MarcarTodosMenosUno(self):
		self.model.dejarUno()
		function.MarcarTodosMenosUno()
		self.data()
		
	def MarcarTodos(self):
		self.model.marcar()
		function.MarcarTodos()
		self.data()
		
	def DesmarcarTodos(self):
		self.model.desmarcar()
		function.DesmarcarTodos()
		self.data()
		
	def Encontrar(self):
		function.Encontrar(self.lineEdit.text())
		self.data()
		self.pushButton_13.setEnabled(True)
		
	def MarcarEncontrados(self):
		function.MarcarEncontrados()
		self.model.marcarEncontrados(function.getEncontrado())
		self.data()
		
	def addConE(self):
		function.AnadirConExten(self.lineEdit_2.text())
		self.item =QListWidgetItem()
		self.listWidget_3.addItem(self.item)
		self.item = self.listWidget_3.item(self.cantCE)
		self.cantCE=self.cantCE+1
		self.item.setText(QApplication.translate("MainWindow",self.lineEdit_2.text(), None, QApplication.UnicodeUTF8))
		self.lineEdit_2.setText("")		
		
	def addSinE(self):
		function.AnadirSinExten(self.lineEdit_3.text())
		self.item = QListWidgetItem()
		self.listWidget_4.addItem(self.item)
		self.item = self.listWidget_4.item(self.cantSE)
		self.cantSE=self.cantSE+1
		self.item.setText(QApplication.translate("MainWindow",self.lineEdit_3.text(), None, QApplication.UnicodeUTF8))
		self.lineEdit_3.setText("")

		
	def EvtText2(self):
		if(self.lineEdit_3.text()):
			search=self.lineEdit_3.text()
		else:
			search="no existe"
		p=0
		lista=function.getMimeTypes(str(search))
		if (lista!=[]):
			self.listWidget_2.setVisible(True)
			for i in range(len(lista)):
				self.item = QListWidgetItem()
				self.listWidget_2.addItem(self.item)
				self.item = self.listWidget_2.item(p)
				p=p+1
				tipo=s.split( str(lista[i]),"'")
				self.item.setText(QApplication.translate("MainWindow",tipo[1], None,QApplication.UnicodeUTF8))
		else:
			self.listWidget_2.setVisible(False)
			
	def escoger2(self):
		self.lineEdit_3.setText(self.listWidget_2.currentItem().text())
		self.listWidget_2.setVisible(False)
	
		
	def EvtText(self):		
		if(self.lineEdit_2.text()):
			search=self.lineEdit_2.text()
		else:
			search="no existe"
		p=0
		lista=function.getMimeTypes(str(search))
		p=0
		lista=function.getMimeTypes(str(search))
		if (lista!=[]):
			self.listWidget.setVisible(True)
			for i in range(len(lista)):
				self.item = QListWidgetItem()
				self.listWidget.addItem(self.item)
				self.item = self.listWidget.item(p)
				p=p+1
				tipo=s.split( str(lista[i]),"'")
				self.item.setText(QApplication.translate("MainWindow",tipo[1], None, QApplication.UnicodeUTF8))
		else:
			self.listWidget.setVisible(False)
			
	def escoger(self):
		self.lineEdit_2.setText(self.listWidget.currentItem().text())
		self.listWidget.setVisible(False)

		
	def fuenteMas(self):
		self.form1.setStyleSheet("font-size: 15px;")
		self.form1.show()
	def fuenteMenos(self):
		self.form1.setStyleSheet("font-size: 13px;")
		self.form1.show()
		
	def language(self):
		if(self.lang==1):
			self.groupBox_55.setVisible(False)
			self.lang=0
		else:
			self.groupBox_55.setVisible(True)
			self.lang=1
	
	def spanish(self):
		function.Traducir("spanish")
		self.groupBox_55.setVisible(False)
	def chinese(self):
		function.Traducir("chinese")
		self.groupBox_55.setVisible(False)
	def japanese(self):
		function.Traducir("japanese")
		self.groupBox_55.setVisible(False)
	def russian(self):
		function.Traducir("russian")
		self.groupBox_55.setVisible(False)
	def italian(self):
		function.Traducir("italian")
		self.groupBox_55.setVisible(False)
	def arabic(self):
		function.Traducir("arabic")
		self.groupBox_55.setVisible(False)
	def english(self):
		function.Traducir("english")
		self.groupBox_55.setVisible(False)
	def portuguese(self):
		function.Traducir("portuguese")
		self.groupBox_55.setVisible(False)
	def french(self):
		function.Traducir("french")
		self.groupBox_55.setVisible(False)
	def german(self):
		function.Traducir("german")
		self.groupBox_55.setVisible(False)
		
	def data(self):
		self.label_10.setText(win._fromUtf8(str(len(self.model.marc))))
		self.label_11.setText(win._fromUtf8(str(function.PesoArchivosNoMarcados())))
		self.label_12.setText(win._fromUtf8(str(function.PesoArchivosMarcados())))
		self.label_13.setText(win._fromUtf8(str(function.PesoTotal())))
		self.label_98.setVisible(True)
		self.label_99.setText(win._fromUtf8(str(function.TiempoDemora())))
		self.label_988.setVisible(True)
		self.label_999.setText(win._fromUtf8(str(function.CantidadArchivosRevisados())))
		self.label_9888.setVisible(True)
		self.label_9999.setText(win._fromUtf8(str(len(function.getDirVacios()))))
		self.label_98888.setVisible(True)
		self.label_99999.setText(win._fromUtf8(str(len(function.getArchivosAbiertos()))))

	def RealizarBusqueda(self):
		if self.doubleSpinBox.value()>0:
			function.AnadirMayork(self.doubleSpinBox.value())
		if self.doubleSpinBox_2.value()>0:
			function.AnadirMenork(self.doubleSpinBox_2.value())
		if len(str(self.kurlrequester_2.text()))!=0:
			function.AnadirExcDir(str(self.kurlrequester_2.text()))
		#self.kpixmapsequencewidget.setVisible(True)
		function.RealizarBusqueda(str(self.kurlrequester.text()))
		
		self.model = StbTreeView(function.getRepetidos(),self.centralwidget)
		self.treeView.show()
		self.treeView.header().hide() 
		self.treeView.setModel(self.model)
		self.treeView.setAlternatingRowColors(True)

		self.label_8.setText(win._fromUtf8(str(function.CantidadGrupos_Archivos()[0])))
		self.label_9.setText(win._fromUtf8(str(function.CantidadGrupos_Archivos()[1])))
		self.data()
		function.reiniciarFiltros()
		
		self.pushButton_10.setEnabled(True)
		self.pushButton_11.setEnabled(True)
		self.pushButton_12.setEnabled(True)
		self.pushButton_66.setEnabled(True)
		self.pushButton_14.setEnabled(True)
		self.pushButton_15.setEnabled(True)
		self.pushButton_16.setEnabled(True)
		self.pushButton_17.setEnabled(True)
		
		self.pushButton_9.clicked.connect(self.oPeso)
		self.pushButton_9.setEnabled(False)
		self.pushButton_8.clicked.connect(self.oTipo)
		self.pushButton_8.setEnabled(False)
		self.pushButton_18.clicked.connect(self.oModif)
		self.pushButton_18.setEnabled(False)
                #self.kpixmapsequencewidget.setVisible(False)		
		
		
	def AdicionarTipos(self):
		function.AdicionarTipos()
		
		
def main():
	app = QApplication(sys.argv)
	f = cMainWindow()
	app.exec_()
	
if __name__=='__main__':
	main()
	


#function.Marcar(objeto.noMarcados[1])
#function.Desmarcar(objeto.marcados[0])
#function.MarcarTodosMenosUno()
#function.MarcarTodos()
#function.DesmarcarTodos() 
#function.Encontrar("cadena")
#function.MarcarEncontrados()

#function.OrganizarPeso("mayor")
#function.OrganizarFecha("mayor")
#function.OrganizarTipo()	

#print function.PesoGrupo(objeto.repetidos[0])
#print function.FechaGrupo(objeto.repetidos[0])
#print function.TipoGrupo(objeto.repetidos[0])

#print "se han revisado: ", function.CantidadArchivosRevisados() ," archivos"


#function.OrganizarPeso("mayor")
#function.OrganizarFecha("mayor")
#function.OrganizarTipo()

#function.getMarcados()
#function.getNoMarcados()
#function objeto.getRepetidos()
#function.getEncontrado()
#function.getTotalArchivos()
#function objeto.getArchivosAbiertos()
#print function.getDirVacios()
#print function.getMimeTypes(self,"busqueda")
