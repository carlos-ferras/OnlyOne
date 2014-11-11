#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Para probar en windows

import re
import ayuda
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import subprocess
import platform
import threading
import string as s
import windows.main as win
from functools import partial
from config import config
import shutil
import time
from dateutil import parser
import datetime
from metaData import metaData
metaData=metaData()
import os
#os.chdir('/usr/share/onlyone')

class makeSearch(QThread):
                taskFinished = pyqtSignal()
		posibles_repetidos= pyqtSignal()
		s_grupos= pyqtSignal()
		total_revisados=pyqtSignal()
		total_temp=pyqtSignal()
		dir_vacions=pyqtSignal()
		rev_sig=pyqtSignal()
		def __init__(self,hash, direcciones,excDir,conExten,sinExten,menork,mayork, parent=None):
			QThread.__init__(self, parent)
			self.hash=hash
			self.totalArchivos=0
			self.archivosAbiertos=[]
			self.dirVacios=[]
			self.repetidos=[]
			self.datos=[]
			self.tiempoDemora=0
			
			self.direcciones=direcciones
			self.excDir=excDir
			self.conExten=conExten
			self.sinExten=sinExten
			self.menork=menork
			self.mayork=mayork
			
			self.data=[]
			
			self.terminated.connect(self.review)
			
                def get_file_checksum(self,filename):
			    h = self.hash.new()
			    chunk_size = 3000
			    try:
				    with open(filename, 'rb') as f:
					while True:
					    chunk = f.read(chunk_size)
					    if len(chunk) == 0:
						break
					    h.update(chunk)
				    return h.hexdigest()
			    except:
				    return -1
		
		def run(self):
			self.horaInicio=datetime.datetime.fromtimestamp(time.time())				    
			self.toCompare = {}
			for dir in self.direcciones:
				if platform.system() == "Windows":
					dir=dir.decode('utf-8')
				for path, dirs, files in os.walk( dir):
					def coinciden(n):
						if platform.system() == "Windows":
							n=n.decode('utf-8')
						return path.startswith(n)			
					lista = filter(coinciden,self.excDir)
					if len(lista)>0:
						continue					
					if len(files)==0 and len(dirs)==0:
						self.dirVacios.append(path)
						self.dir_vacions.emit()
						continue	
					for filename in files:
						self.totalArchivos+=1
						self.total_revisados.emit()						
						filepath = os.path.join( path, filename )
						if os.path.exists(filepath):
							meta=os.stat( filepath )
							filesize = metaData.peso(meta.st_size)	
							modificado = parser.parse(time.ctime(meta.st_mtime))	
							tipo=str(metaData.extencion(filepath))
							try:
								if(filename[len(filename)-1]=="~") or (filename.split('.')[-1]=="pyc") or (filename.split('.')[-1]=="pure") or (filename.split('.')[-1]=="swp") or (filename.split('.')[-1]=="lo") or (filename.split('.')[-1]=="o") or (filename.split('.')[-1]=="tmp") or (filename.split('.')[-1]=="v") or (str(filename.split('.')[-1]).lower()=="bak") or (str(filename).lower()=="thumbs.db") or (filename.split('.')[-1]=="log") or (filename.split('.')[-1]=="diz") or (filename.split('.')[-1]=="ion"):
									self.archivosAbiertos.append([filepath,modificado,filesize,tipo])
									self.total_temp.emit()
									continue
							except:
								pass
							if not str(tipo)+'\n' in self.sinExten:
								if(self.conExten!=[]):
									if str(tipo)+'\n' in self.conExten:
										self.toCompare.setdefault( str(str(filesize)+'-!#!-'+str(tipo)), [] ).append( [filepath,modificado,filesize,tipo])
										if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])>1:
											self.posibles_repetidos.emit()
											if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])==2:
												self.posibles_repetidos.emit()
												self.s_grupos.emit()
								elif(self.menork!=0L):
									if((meta.st_size>self.mayork)and(meta.st_size<self.menork)):
										self.toCompare.setdefault( str(str(filesize)+'-!#!-'+str(tipo)), [] ).append( [filepath,modificado,filesize,tipo])
										if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])>1:
											self.posibles_repetidos.emit()
											if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])==2:
												self.posibles_repetidos.emit()
												self.s_grupos.emit()
								elif(self.menork==0L):
									if(meta.st_size>self.mayork):
										self.toCompare.setdefault( str(str(filesize)+'-!#!-'+str(tipo)), [] ).append( [filepath,modificado,filesize,tipo])
										if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])>1:
											self.posibles_repetidos.emit()
											if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])==2:
												self.posibles_repetidos.emit()
												self.s_grupos.emit()
								elif((self.conExten!=[])and(self.menork!=0L)):
									if((meta.st_size>self.mayork)and(meta.st_size<self.menork)):
										if str(tipo)+'\n' in self.conExten:
											self.toCompare.setdefault( str(str(filesize)+'-!#!-'+str(tipo)), [] ).append( [filepath,modificado,filesize,tipo])
											if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])>1:
												self.posibles_repetidos.emit()
												if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])==2:
													self.posibles_repetidos.emit()
													self.s_grupos.emit()
								elif((self.conExten!=[])and(self.menork==0L)):
									if(meta.st_size>self.mayork):
										if str(tipo)+'\n' in self.conExten:
											self.toCompare.setdefault( str(str(filesize)+'-!#!-'+str(tipo)), [] ).append( [filepath,modificado,filesize,tipo])			
											if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])>1:
												self.posibles_repetidos.emit()
												if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])==2:
													self.posibles_repetidos.emit()
													self.s_grupos.emit()
								else:
									self.toCompare.setdefault( str(str(filesize)+'-!#!-'+str(tipo)), [] ).append( [filepath,modificado,filesize,tipo])					
									if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])>1:
											self.posibles_repetidos.emit()
											if len(self.toCompare[str(str(filesize)+'-!#!-'+str(tipo))])==2:
												self.posibles_repetidos.emit()
												self.s_grupos.emit()
				
			self.review()			
		def review(self):
			self.rev_sig.emit()
			for files in [ flist for flist in self.toCompare.values() if len(flist)>1]:
				duplicates = {}
				for filepath in files:
					filehash = self.get_file_checksum(filepath[0])
					if filehash not in duplicates:
						duplicates.setdefault(filehash, []).append (filepath)
					else:
						duplicates[filehash].append(filepath)
				fils=[ duplicate for duplicate in  duplicates.values() if len(duplicate)>1]
				if len(fils)>0:
					group= fils[0]
					self.repetidos.append(group)
			
			#hora de Fin
			self.horaFin=datetime.datetime.fromtimestamp(time.time())
			self.tiempoDemora=self.horaFin-self.horaInicio
			
			self.data=[self.direcciones,self.totalArchivos,self.archivosAbiertos,self.dirVacios,self.repetidos,self.tiempoDemora]
			try:
				import dbus
				bus = dbus.SessionBus()
				notify_object = bus.get_object('org.freedesktop.Notifications','/org/freedesktop/Notifications')
				notify_interface = dbus.Interface(notify_object,'org.freedesktop.Notifications')
				notify_id = notify_interface.Notify("OnlyOne", 0, "pixmaps/onlyone/logo.png", "OnlyOne",str(QApplication.translate("MainWindow",'Escaneo Terminado')), "",{},10000)
			except:
				pass
			self.taskFinished.emit() 

 
class addFileTypes(QThread):
                taskFinished = pyqtSignal()
		def __init__(self,dir, parent=None):
			QThread.__init__(self, parent)	
			self.dir=dir
			self.cantidad=0
                def run(self):			
			self.cantidad=metaData.adicionarTipos(self.dir)
			self.taskFinished.emit() 


def pesoEnByte(peso):
		"""devuelve cuanto pesan en byte el peso pasado por parametro"""
		p=0    
		SUFIJOS = [ "KB" , "MB" , "GB" , "TB" , "PB" , "EB" , "ZB" ,"YB" ]
		multiplo=1024.0    
		partes=s.split(peso)  
		tamano=float(partes[0])
		for sufijo in SUFIJOS:				
			tamano *= multiplo
			if (sufijo==partes[1]):
				p+=tamano
				break
		return p
		
 
class cMainWindow(win.Ui_MainWindow):
	def __init__(self):
		self.form1 =QMainWindow()
		self.setupUi(self.form1)
		self.form1.showMaximized()

		self.config=config()
		conf=self.config.load()
		if conf:
			self.fileLocation=conf[0]
			if self.fileLocation=='None':
				self.fileLocation=''
			self.opacity=float(conf[1])
			self.lang=conf[2]			
			self.form1.setWindowOpacity(self.opacity)
		else:
			self.fileLocation=''
			self.opacity=1				
			self.lang='es'
		self.form1.setWindowOpacity(self.opacity)		
		#aux
		self.porPeso="mayor"
		self.porFecha="mayor"
		self.cantCE=0
		self.cantSE=0
		self.exc=0
		self.con=0
		#salida
		self.totalArchivos=0
		self.archivosAbiertos=[]
		self.dirVacios=[]
		self.repetidos=[]
		self.tiempoDemora=0
		self.encontrado=[]
		#entrada
		self.direcciones=[]
		self.excDir=[]
		self.conExten=[]
		self.sinExten=['']
		self.menork=0
		self.mayork=0
		
		self.form1.closeEvent=self.onCloseEvent		
		self.pushButton_6.clicked.connect(self.scanner)
		self.pushButton_666.clicked.connect(self.cancelar)
		
		self.pushButton_7.clicked.connect(self.adicionarTiposArchivo)
		
		self.pushButton_0.clicked.connect(self.twitter)
		self.toolButton.clicked.connect(self.fuenteMas)
		self.toolButton_2.clicked.connect(self.fuenteMenos)
		self.pushButton_5.clicked.connect(self.language)
		self.pushButton_55.clicked.connect(self.setOpacity)
		self.pushButton_555.clicked.connect(self.defaultLocation)
		
		self.lineEdit_2.textChanged.connect(self.EvtText)
		self.listWidget.clicked.connect( self.escoger)
		self.lineEdit_3.textChanged.connect(self.EvtText2)
		self.listWidget_2.clicked.connect( self.escoger2)
		self.pushButton_88.clicked.connect( self.addConE)
		self.pushButton_85.clicked.connect( self.addSinE)
		self.pushButton_87.clicked.connect( self.limpiar1)
		self.pushButton_89.clicked.connect( self.limpiar2)
		
		self.pushButton_10.clicked.connect(self.MarcarTodos)
		self.pushButton_10.setEnabled(False)
		self.pushButton_11.clicked.connect(self.MarcarTodosMenosUno)
		self.pushButton_11.setEnabled(False)
		self.pushButton_12.clicked.connect(self.DesmarcarTodos)
		self.pushButton_12.setEnabled(False)
		self.pushButton_66.clicked.connect(self.Encontrar)
		self.pushButton_66.setEnabled(False)
		self.pushButton_13.clicked.connect(self.searsh_options)
		self.pushButton_13.setEnabled(False)
		
		#FALTAN FUNCIONES
		#menos el mas nuevo
		self.pushButton_74.clicked.connect(self.MarcarTodosMenosMasNuevo)
		self.pushButton_74.setEnabled(False)
		#menos el mas viejo
		self.pushButton_75.clicked.connect(self.MarcarTodosMenosMasViejo)
		self.pushButton_75.setEnabled(False)
		
		self.pushButton_14.clicked.connect(self.BorrarMarcados)
		self.pushButton_14.setEnabled(False)
		self.pushButton_15.clicked.connect(self.BorrarNoMarcados)
		self.pushButton_15.setEnabled(False)
		self.pushButton_16.clicked.connect(self.BorrarTemporales)
		self.pushButton_16.setEnabled(False)
		self.pushButton_17.clicked.connect(self.BorrarDirectoriosVacios)
		self.pushButton_17.setEnabled(False)
		self.pushButton_09.clicked.connect(self.BorrarDirectoriosVacios)
		self.pushButton_0999.clicked.connect(partial(self.BorrarEnPanel,True))
		
		self.pushButton.clicked.connect(self.about)
		self.pushButton_2.clicked.connect(self.help)
		self.pushButton_3.clicked.connect(self.face)
		
		self.pushButton_kurlrequester.clicked.connect(self.location)
		self.kurlrequester.customContextMenuRequested.connect(self.popup3)	
		self.pushButton_kurlrequester_2.clicked.connect(self.addExcluir)
		self.kurlrequester_2.customContextMenuRequested.connect(self.popup)
		self.treeView.customContextMenuRequested.connect(self.rigth_popup)
		self.treeView.pressed.connect(self.marcarDesmarcar)
		self.listWidget_09.customContextMenuRequested.connect(self.panel_popup)
		self.pushButton_099.clicked.connect(self.BorrarEnPanel)
		self.pushButton_09999.clicked.connect(self.BorrarEnPanel)
		self.label_9888.clicked.connect(partial(self.panel, 1))
		self.label_98888.clicked.connect(partial(self.panel,2))
		self.panelActivo=None
		self.comboBox_099999.currentIndexChanged.connect(self.cb_change)
		
	
	def panel_popup(self,pos):
		if len(self.listWidget_09.selectedIndexes())>0:
			menu = QMenu()
			action = QAction(self.form1)
			action.setIconVisibleInMenu(True)		
			icon2 = QIcon()
			icon2.addPixmap(QPixmap("pixmaps/onlyone/copy.png"), QIcon.Normal, QIcon.Off)
			action.setIcon(icon2)
			action.setText(QApplication.translate("MainWindow",'Copiar'))
			action.triggered.connect(self.right_copy2)
			menu.addAction(action)
			if self.panelActivo==1:
				action = QAction(self.form1)
				action.setIconVisibleInMenu(True)	
				icon2 = QIcon()
				icon2.addPixmap(QPixmap("pixmaps/onlyone/open_file.png"), QIcon.Normal, QIcon.Off)
				action.setIcon(icon2)
				action.setText(QApplication.translate("MainWindow",'Abrir'))
				action.triggered.connect(partial(self.right_open,self.listWidget_09.item(self.listWidget_09.selectedIndexes()[0].row()).text().toUtf8().data()))
				menu.addAction(action)				
			if self.panelActivo==2:	
				action = QAction(self.form1)
				action.setIconVisibleInMenu(True)	
				icon2 = QIcon()
				icon2.addPixmap(QPixmap("pixmaps/onlyone/open_dir.png"), QIcon.Normal, QIcon.Off)
				action.setIcon(icon2)
				action.setText(QApplication.translate("MainWindow",'Abrir contenedor'))
				action.triggered.connect(partial(self.right_open,os.path.dirname(self.listWidget_09.item(self.listWidget_09.selectedIndexes()[0].row()).text().toUtf8().data())))
				menu.addAction(action)				
			action = QAction(self.form1)
			action.setIconVisibleInMenu(True)
			icon2 = QIcon()
			icon2.addPixmap(QPixmap("pixmaps/onlyone/f6447422.png"), QIcon.Normal, QIcon.Off)
			action.setIcon(icon2)
			action.setText(QApplication.translate("MainWindow",'Eliminar'))
			action.triggered.connect(self.BorrarEnPanel)
			menu.addAction(action)
			action = menu.exec_(self.listWidget_09.mapToGlobal(pos))
			
	def right_open(self,path):
		if platform.system() == "Windows":
			os.startfile(path)
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", path])
		else:
			subprocess.Popen(["xdg-open", path])

		
	def right_copy2(self):	
		indexs=self.listWidget_09.item(self.listWidget_09.selectedIndexes()[0].row()).text()		
		clipboard=QApplication.clipboard()
		clipboard.setText(indexs)
	
	
	def panel(self,option):		
		if self.widget_09.isVisible() and self.panelActivo==option:
			self.widget_09.setVisible(False)
			self.panelActivo=None
		else:
			self.widget_09.setVisible(True)
			self.panelActivo=option
			if option==1:
				self.label_0999.setHidden(True)
				self.label_09999.setHidden(True)
				self.frame_999.setHidden(True)					
				self.pushButton_0999.setVisible(False)
				self.pushButton_09999.setVisible(False)
				self.pushButton_09.setVisible(True)
				self.pushButton_099.setVisible(True)				
				self.label_09.setText(QApplication.translate("MainWindow", "Directorios Vacios", None, QApplication.UnicodeUTF8))
				self.label_099.setText(self.label_9999.text())
				
				for i in range(self.listWidget_09.count()):
					self.listWidget_09.item(i).setHidden(True)
				for dir in self.dirVacios:
					self.listWidget_09.addItem(win._fromUtf8(dir.decode('utf-8')))
				
			elif option==2:
				self.label_0999.setHidden(False)
				self.label_09999.setHidden(False)
				self.frame_999.setHidden(False)
				self.pushButton_09.setVisible(False)
				self.pushButton_099.setVisible(False)
				self.pushButton_0999.setVisible(True)
				self.pushButton_09999.setVisible(True)
				self.label_09.setText(QApplication.translate("MainWindow", "Archivos Temporales", None, QApplication.UnicodeUTF8))
				self.label_099.setText(self.label_99999.text())
				self.layout_09.addWidget(self.listWidget_09,2,0,18,10)
				
				suma=0				
				for i in range(self.listWidget_09.count()):
					self.listWidget_09.item(i).setHidden(True)
				for dir in self.archivosAbiertos:
					cbt=str(self.comboBox_099999.currentText())
					if cbt!='All':
						dirn=win._fromUtf8(dir[0].decode('utf-8')).toUtf8().data()
						if cbt=='*~':
							ext='*'+dirn[-1]
						else:
							ext=dirn.split('.')[-1]
						if ext== cbt.split('.')[-1]:
							suma+=pesoEnByte(dir[2])
							self.listWidget_09.addItem(win._fromUtf8(dir[0].decode('utf-8')))
					else:
						suma+=pesoEnByte(dir[2])
						self.listWidget_09.addItem(win._fromUtf8(dir[0].decode('utf-8')))
				self.label_09999.setText(metaData.peso(suma))
			
	
	def cb_change(self):
		suma=0
		for i in range(self.listWidget_09.count()):
			self.listWidget_09.item(i).setHidden(True)
		for dir in self.archivosAbiertos:
			cbt=str(self.comboBox_099999.currentText())
			if cbt!='All':
				dirn=win._fromUtf8(dir[0].decode('utf-8')).toUtf8().data()
				if cbt=='*~':
					ext='*'+dirn[-1]
				else:
					ext=dirn.split('.')[-1]
				if ext== cbt.split('.')[-1]:
					suma+=pesoEnByte(dir[2])
					self.listWidget_09.addItem(win._fromUtf8(dir[0].decode('utf-8')))
			else:
				suma+=pesoEnByte(dir[2])
				self.listWidget_09.addItem(win._fromUtf8(dir[0].decode('utf-8')))
		self.label_09999.setText(metaData.peso(suma))
	

	def BorrarEnPanel(self,all=False):
		"""Manda a borrar todos los directorios vacios encontrados y actualiza la informacion grafica"""
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(QApplication.translate('MainWindow','¿Está seguro de que desea eliminar los directorios vacios?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			self.form1.setCursor(Qt.WaitCursor)
			archivo=True
			errores=''
			delete=[]
			delete2=[]
			cont=0
			for i in range(self.listWidget_09.count()):
				if not self.listWidget_09.item(i).isHidden():
					if all:
						if os.path.isfile(self.listWidget_09.item(i).text().toUtf8().data()):
							try:								
								delFile=[flist for flist in self.archivosAbiertos if flist[0]==self.listWidget_09.item(i).text().toUtf8().data()][0]
								os.remove(self.listWidget_09.item(i).text().toUtf8().data())
								delete2.append(self.archivosAbiertos.index(delFile))
								delete.append(self.listWidget_09.item(i))
							except:
								errores=errores+self.listWidget_09.item(i).text().toUtf8().data()+"***"
						else:
							archivo=False
							try:
								shutil.rmtree(self.listWidget_09.item(i).text().toUtf8().data())
								delete2.append(cont)
								delete.append(self.listWidget_09.item(i))
							except:
								errores=errores+self.listWidget_09.item(i).text().toUtf8().data()+"***"
					elif self.listWidget_09.item(i).isSelected():
						if os.path.isfile(self.listWidget_09.item(i).text().toUtf8().data()):
							try:
								delFile=[flist for flist in self.archivosAbiertos if flist[0]==self.listWidget_09.item(i).text().toUtf8().data()][0]
								os.remove(self.listWidget_09.item(i).text().toUtf8().data())
								delete2.append(self.archivosAbiertos.index(delFile))
								delete.append(self.listWidget_09.item(i))
								
							except:
								errores=errores+self.listWidget_09.item(i).text().toUtf8().data()+"***"
						else:
							archivo=False
							try:
								shutil.rmtree(self.listWidget_09.item(i).text().toUtf8().data())
								delete2.append(cont)
								delete.append(self.listWidget_09.item(i))
							except:
								errores=errores+self.listWidget_09.item(i).text().toUtf8().data()+"***"
					cont+=1			
			for i in range(len(delete))[::-1]:
				delete[i].setHidden(True)			
			if not archivo:
				for i in range(len(delete2))[::-1]:
					del self.dirVacios[delete2[i]]
			else:	
				for i in range(len(delete2))[::-1]:
					del self.archivosAbiertos[delete2[i]]			
			suma=0
			for file in self.archivosAbiertos:
				suma+=pesoEnByte(file[2])
			self.label_09999.setText(metaData.peso(suma))
			self.data()
			self.form1.setCursor(Qt.ArrowCursor)
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow",'Operación terminada')))
			if errores!='':
				if not archivo:
					self.Error('ErrorDirectoriosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes directorios:') +' '+errores)
				else:
					self.Error('ErrorArchivosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes archivos:')  +' '+errores)
	

					
	def searsh_options(self,pos):
		menu = QMenu()		
		action = QAction(self.form1)
		action.setIconVisibleInMenu(True)
		icon2 = QIcon()
		icon2.addPixmap(QPixmap("pixmaps/onlyone/f8576560.png"), QIcon.Normal, QIcon.Off)
		action.setIcon(icon2)
		action.setText(QApplication.translate("MainWindow",'Marcar Todos'))
		action.triggered.connect(self.MarcarEncontrados)
		menu.addAction(action)
		action = QAction(self.form1)
		action.setIconVisibleInMenu(True)
		icon2 = QIcon()
		icon2.addPixmap(QPixmap("pixmaps/onlyone/este.png"), QIcon.Normal, QIcon.Off)
		action.setIcon(icon2)
		action.setText(QApplication.translate("MainWindow",'Desarcar Todos'))
		action.triggered.connect(self.DesmarcarEncontrados)
		menu.addAction(action)	
		action = QAction(self.form1)
		action.setIconVisibleInMenu(True)
		icon2 = QIcon()
		icon2.addPixmap(QPixmap("pixmaps/onlyone/f8576576.png"), QIcon.Normal, QIcon.Off)
		action.setIcon(icon2)
		action.setText(QApplication.translate("MainWindow",'Marcar todos menos uno de cada grupo'))
		action.triggered.connect(self.MarcarEncontradosMenosUno)
		menu.addAction(action)
		action = menu.exec_(QCursor.pos())
	
	
	def rigth_popup(self,pos):
		menu = QMenu()
		if len(self.treeView.selectedIndexes())>0:
			if len(self.treeView.selectedIndexes())==1:
				action = QAction(self.form1)
				action.setIconVisibleInMenu(True)		
				icon2 = QIcon()
				icon2.addPixmap(QPixmap("pixmaps/onlyone/copy.png"), QIcon.Normal, QIcon.Off)
				action.setIcon(icon2)
				action.setText(QApplication.translate("MainWindow",'Copiar'))
				action.triggered.connect(self.right_copy)
				menu.addAction(action)			
				action = QAction(self.form1)
				action.setIconVisibleInMenu(True)	
				icon2 = QIcon()
				icon2.addPixmap(QPixmap("pixmaps/onlyone/open_file.png"), QIcon.Normal, QIcon.Off)
				action.setIcon(icon2)
				action.setText(QApplication.translate("MainWindow",'Abrir'))
				action.triggered.connect(partial(self.right_open,self.model.arraydata[self.treeView.selectedIndexes()[0].row()].column(self.treeView.selectedIndexes()[0].column())))
				menu.addAction(action)		
				action = QAction(self.form1)
				action.setIconVisibleInMenu(True)	
				icon2 = QIcon()
				icon2.addPixmap(QPixmap("pixmaps/onlyone/open_dir.png"), QIcon.Normal, QIcon.Off)
				action.setIcon(icon2)
				action.setText(QApplication.translate("MainWindow",'Abrir contenedor'))
				action.triggered.connect(partial(self.right_open,os.path.dirname(self.model.arraydata[self.treeView.selectedIndexes()[0].row()].column(self.treeView.selectedIndexes()[0].column()))))
				menu.addAction(action)		
			action = QAction(self.form1)
			action.setIconVisibleInMenu(True)	
			icon2 = QIcon()
			icon2.addPixmap(QPixmap("pixmaps/onlyone/f6447422.png"), QIcon.Normal, QIcon.Off)
			action.setIcon(icon2)
			action.setText(QApplication.translate("MainWindow",'Elininar'))
			action.triggered.connect(self.rigth_delete)
			menu.addAction(action)
			
			action = menu.exec_(self.treeView.mapToGlobal(pos))
		
	
	def right_copy(self):	
		indexs=win._fromUtf8(self.model.arraydata[self.treeView.selectedIndexes()[0].row()].column(self.treeView.selectedIndexes()[0].column()))		
		clipboard=QApplication.clipboard()
		clipboard.setText(indexs)

	
	def rigth_delete(self):
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(QApplication.translate('MainWindow','¿Está seguro de que desea eliminar los archivos seleccionados?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			indexs=[]
			for index in self.treeView.selectedIndexes():
				pos=0
				for i in indexs:
					if i>index.row():
						break
					pos+=1
				indexs.insert(pos,index.row())		
			self.model.removeRows3(indexs)
			self.data()
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow",'Operación terminada')))
			if self.model.errores!='':
				self.Error('ErrorArchivosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes archivos:')  +' '+ self.model.errores)
			
	
	def popup(self,pos):
		if len(self.kurlrequester_2.selectedIndexes())>0:
			menu = QMenu()
			action = QAction(self.form1)
			action.setIconVisibleInMenu(True)
			icon2 = QIcon()
			icon2.addPixmap(QPixmap("pixmaps/onlyone/f6447422.png"), QIcon.Normal, QIcon.Off)
			action.setIcon(icon2)
			action.setText(QApplication.translate("MainWindow",'Eliminar'))
			action.triggered.connect(self.eliminar2)
			menu.addAction(action)
			action = menu.exec_(self.kurlrequester_2.mapToGlobal(pos))
			
	
	def popup3(self,pos):
		if len(self.kurlrequester.selectedIndexes())>0:
			menu = QMenu()
			action = QAction(self.form1)
			action.setIconVisibleInMenu(True)
			icon2 = QIcon()
			icon2.addPixmap(QPixmap("pixmaps/onlyone/f6447422.png"), QIcon.Normal, QIcon.Off)
			action.setIcon(icon2)
			action.setText(QApplication.translate("MainWindow",'Eliminar'))
			action.triggered.connect(self.eliminar)
			menu.addAction(action)
			action = menu.exec_(self.kurlrequester.mapToGlobal(pos))
	
	def eliminar(self):
		for item in self.kurlrequester.selectedItems():
			item.setHidden(True)
			
	def eliminar2(self):
		for item in self.kurlrequester_2.selectedItems():
			item.setHidden(True)
	
	
	def location(self):
		fileLocation=QFileDialog.getExistingDirectory (self.form1,QApplication.translate("MainWindow", 'Abrir'), self.fileLocation)
		if fileLocation:
			item_99 = QListWidgetItem()
			self.kurlrequester.addItem(item_99)
			self.item = self.kurlrequester.item(self.con)
			self.con+=1
			item_99.setText(fileLocation)
	
	
	def addExcluir(self):
		fileLocation=QFileDialog.getExistingDirectory (self.form1,QApplication.translate("MainWindow", 'Abrir'), self.fileLocation)
		if fileLocation:
			item_99 = QListWidgetItem()
			self.kurlrequester_2.addItem(item_99)
			self.item = self.kurlrequester_2.item(self.exc)
			self.exc+=1
			item_99.setText(fileLocation)
		
	
	def help(self):
		try:
			assistant=ayuda.Assistant()
			assistant.startAssistant()
		except:
			pass
	
	
	def face(self):
		import webbrowser
		webbrowser.open('https://www.facebook.com/freeonlyone')
	
	
	def  about(self):
		import windows.about as about
		about.about()
	
	
	def BorrarMarcados(self):
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(QApplication.translate('MainWindow','¿Está seguro de que desea eliminar los archivos marcados?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			self.form1.setCursor(Qt.WaitCursor)
			self.model.removeRows2(True)
			self.data()
			self.form1.setCursor(Qt.ArrowCursor)	
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow",'Operación terminada')))
			if self.model.errores!='':
				self.Error('ErrorArchivosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes archivos:')  +' '+ self.model.errores)
			     
		
	def BorrarNoMarcados(self):
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(Application.translate('MainWindow','¿Está seguro de que desea eliminar los archivos no marcados?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			self.form1.setCursor(Qt.WaitCursor)
			self.model.removeRows2(False)
			self.data()
			self.form1.setCursor(Qt.ArrowCursor)	
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow",'Operación terminada')))
			if  self.model.errores!='':
				self.Error('ErrorArchivosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes archivos:')  +' '+ self.model.errores)
			     
		
	def BorrarTemporales(self):
		"""Manda a borrar todos los archivos temporales encontrados y actualiza la informacion grafica"""
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(QApplication.translate('MainWindow','¿Está seguro de que desea eliminar los archivos temporales?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			self.form1.setCursor(Qt.WaitCursor)
			errores=''
			for direccion in self.archivosAbiertos:    
				if os.path.isfile(direccion[0]):
					try:
						os.remove(direccion[0])
					except:
						errores=errores+str(direccion[0])+"***"
				else:
					errores=errores+direccion+"***"
			self.archivosAbiertos=[]
			for i in range(self.listWidget_09.count()):
				self.listWidget_09.item(i).setHidden(True)
			self.label_09999.setText(metaData.peso(0))
			self.data()
			self.form1.setCursor(Qt.ArrowCursor)	
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow",'Operación terminada')))
			if errores!='':
				self.Error('ErrorArchivosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes archivos:')  +' '+errores)
		

	def BorrarDirectoriosVacios(self):
		"""Manda a borrar todos los directorios vacios encontrados y actualiza la informacion grafica"""
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(QApplication.translate('MainWindow','¿Está seguro de que desea eliminar los directorios vacios?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			self.form1.setCursor(Qt.WaitCursor)
			errores=''		
			for dir in self.dirVacios:
				try:
					shutil.rmtree(dir)
				except:
					errores=errores+dir+"***"
			self.dirVacios=[]			
			for i in range(self.listWidget_09.count()):
				self.listWidget_09.item(i).setHidden(True)			
			self.data()
			self.form1.setCursor(Qt.ArrowCursor)
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow",'Operación terminada')))
			if errores!='':
				self.Error('ErrorDirectoriosNoBorrados: '+QApplication.translate("MainWindow",'No se pudo borrar los siguientes directorios:') +' '+errores)
			
	
	def MarcarTodos(self):
		"""Marca todos los archivos y los muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.marcar()
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)	
	
	
	def MarcarTodosMenosUno(self):
		"""Marca todos los archivos menos uno de cada grupo y los muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.dejarUno()
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
		
		
	def MarcarTodosMenosMasNuevo(self):
		"""Marca todos los archivos menos uno de cada grupo y los muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.dejarNuevo()
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
		
		
	def MarcarTodosMenosMasViejo(self):
		"""Marca todos los archivos menos uno de cada grupo y los muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.dejarViejo()
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
	
	
	def DesmarcarTodos(self):
		"""Desmarca todos los archivos y los muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.desmarcar()
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
		
		
	def Encontrar(self):
		self.form1.setCursor(Qt.WaitCursor)
		self.encontrado=[]
		for item in self.model.arraydata:
			esta=s.find(item.data[0],self.lineEdit.text())		
			if (esta!=-1):
					self.encontrado.append(item.data[0])
					item.encontrado=True
			else:
				item.encontrado=False
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
		QMessageBox.about(self.form1, "OnlyOne", str(QApplication.translate("MainWindow",'Se han encontrado %s coincidencias'))%(len(self.encontrado))) 
		self.pushButton_13.setEnabled(True)
	
	
	def MarcarEncontrados(self):
		"""De la busqueda realizada si hay coincidencia, marca todas estas y lo muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.marcarEncontrados(self.encontrado)
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
		
	
	def DesmarcarEncontrados(self):
		"""De la busqueda realizada si hay coincidencia, marca todas estas y lo muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.desmarcarEncontrados(self.encontrado)
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
		
		
	def MarcarEncontradosMenosUno(self):
		"""De la busqueda realizada si hay coincidencia, marca todas estas y lo muestra graficamente"""
		self.form1.setCursor(Qt.WaitCursor)
		self.model.dejarUnEncontrados(self.encontrado)
		self.data()
		self.form1.setCursor(Qt.ArrowCursor)
	
	def limpiar1(self):
		self.listWidget_3.clear()
		self.conExten=[]
		self.cantCE=0
		
		
	def limpiar2(self):
		self.listWidget_4.clear()
		self.sinExten=[]
		self.cantSE=0	
		
	
	def addConE(self):
		"""Añade el filtro con extencion que especifica que solo se busque archivos de este tipo"""
		if self.lineEdit_2.text()!="" and self.lineEdit_2.text()!=None:
			if len(metaData.levantar(self.lineEdit_2.text()))==1:
				for type in metaData.levantar(self.lineEdit_2.text(),True):
					self.conExten.append(type)			
			item =QListWidgetItem()
			self.listWidget_3.addItem(item)
			item = self.listWidget_3.item(self.cantCE)
			self.cantCE=self.cantCE+1
			item.setText(win._fromUtf8(self.lineEdit_2.text()))
			self.lineEdit_2.setText("")	
			
	
	def addSinE(self):
		"""Añade el filtro con sin extencion que especifica que no se busque archivos de este tipo"""
		if self.lineEdit_3.text()!="" and self.lineEdit_3.text()!=None:
			if len(metaData.levantar(self.lineEdit_3.text()))==1:
				for type in metaData.levantar(self.lineEdit_3.text(),True):
					if self.sinExten==['']:
						self.sinExten[0]=type
					else:
						self.sinExten.append(type)
			item = QListWidgetItem()
			self.listWidget_4.addItem(item)
			item = self.listWidget_4.item(self.cantSE)
			self.cantSE=self.cantSE+1
			item.setText(win._fromUtf8(self.lineEdit_3.text()))
			self.lineEdit_3.setText("")
	
	
	def escoger(self):
		self.lineEdit_2.setText(self.listWidget.currentItem().text())
		self.listWidget.setVisible(False)
	
	
	def escoger2(self):
		self.lineEdit_3.setText(self.listWidget_2.currentItem().text())
		self.listWidget_2.setVisible(False)
	
	
	def EvtText(self):	
		"""Rellena el combobox con las coincidencias de tipo segun lo que el usuario escribe"""		
		if(self.lineEdit_2.text()):
			search=self.lineEdit_2.text()
		else:
			search="no existe"
		lista=metaData.levantar(search)		
		if (lista!=[]):
			for i in range(self.listWidget.count()):
				self.listWidget.item(i).setHidden(True)
			self.listWidget.setVisible(True)
			for i in lista:
				self.listWidget.addItem(i)
		else:
			self.listWidget.setVisible(False)
	
	
	def EvtText2(self):
		"""Rellena el combobox con las coincidencias de tipo segun lo que el usuario escribe"""
		if(self.lineEdit_3.text()):
			search=self.lineEdit_3.text()
		else:
			search="no existe"
		lista=metaData.levantar(search)
		if (lista!=[]):
			for i in range(self.listWidget_2.count()):
				self.listWidget_2.item(i).setHidden(True)
			self.listWidget_2.setVisible(True)
			for i in lista:
				self.listWidget_2.addItem(i)
		else:
			self.listWidget_2.setVisible(False)
		
	
	def defaultLocation(self):
		self.fileLocation=QFileDialog.getExistingDirectory (self.form1,QApplication.translate("MainWindow",'Directorio por Defecto'), self.fileLocation)
		if not self.fileLocation:
			self.fileLocation=''
	
		
	def setOpacity(self):
		"""Abre una ventana para cambiar la opacidad de la ventana"""
		dialog=QDialog(self.form1)
		dialog.setGeometry(QRect(0, 0, 170, 70));	
		
		horizontalSlider=QSlider(dialog)
		horizontalSlider.setGeometry(QRect(5,5, 160, 20));
		horizontalSlider.setOrientation(Qt.Horizontal);
		horizontalSlider.setMinimum(80)
		horizontalSlider.setValue(self.opacity*100)
		
		def opacity():
			"""Cambia la opacidad de la ventana"""
			self.opacity=horizontalSlider.value()/100.0
			self.form1.setWindowOpacity(self.opacity)
			dialog.close()
			
		def cancel():
			"""Pone la opacidad como estaba anteriormente a la vista previa"""
			self.form1.setWindowOpacity(self.opacity)
			dialog.close()
			
		def preview():
			"""Vista previa de la opacidad que esta modificando el usuario"""
			o=horizontalSlider.value()/100.0
			self.form1.setWindowOpacity(o)
			
		def hide(event):
			"""Ajusta la opacidad de la ventana"""
			self.form1.setWindowOpacity(self.opacity)
		
		button=QPushButton(QApplication.translate('MainWindow','Aceptar'),dialog)
		button.setGeometry(QRect(108,30, 60, 25));
		button.clicked.connect(opacity)
		
		button2=QPushButton(QApplication.translate('MainWindow','Cancelar'),dialog)
		button2.setGeometry(QRect(40,30, 60, 25));
		button2.clicked.connect(cancel)
		
		horizontalSlider.valueChanged.connect(preview)
		horizontalSlider.hideEvent =hide
		
		dialog.exec_()
	
	
	def changeLang(self,lang):
		"""cambia el idioma por defecto de la aplicacion"""
		self.lang=lang
		QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate('MainWindow','Para guardar los cambios debe reiniciar la aplicación')))
		self.centralwidget.setEnabled(True)
	
	
	def language(self,pos):		
		menu = QMenu()
		action = QAction(self.form1)
		action.setText(QApplication.translate("MainWindow", 'locale', None, QApplication.UnicodeUTF8))
		action.triggered.connect(partial(self.changeLang, 'locale'))
		menu.addAction(action)
		action = QAction(self.form1)
		action.setText('es')
		action.triggered.connect(partial(self.changeLang, 'es'))
		menu.addAction(action)
		for filePath in os.listdir('Locale'):
		    fileName  = os.path.basename(filePath)
		    fileMatch = re.match("onlyone_([a-z]{2,}).qm", fileName)
		    if fileMatch:
				action = QAction(self.form1)
				action.setText(QString.fromUtf8(fileMatch.group(1)))
				action.triggered.connect(partial(self.changeLang, QString.fromUtf8(fileMatch.group(1))))	
				menu.addAction(action)
		action = menu.exec_(QCursor.pos())

	
	def fuenteMenos(self):
		self.form1.setStyleSheet("font-size: 13px;")
		self.treeView.setStyleSheet("font-size: 11px;background:#f8f8f8;")
		self.form1.show()
	
	
	def fuenteMas(self):
		self.form1.setStyleSheet("font-size: 15px;")
		self.treeView.setStyleSheet("font-size: 13px;background:#f8f8f8;")
		self.form1.show()
	
	
	def twitter(self):
		import webbrowser
		webbrowser.open('https://twitter.com/freeOnlyOne')
		
		
	def adicionarTiposArchivo(self):		
		dir=QFileDialog.getExistingDirectory (self.form1,QApplication.translate("MainWindow",'Archivo'), '/')
		if dir:
			self.pushButton_7.setEnabled(False)
			self.progressBar_2.setVisible(True)
			self.progressBar_2.setRange(0,0)
			self.addFileTypes = addFileTypes(dir)
			self.addFileTypes.taskFinished.connect(self.archivosAdicionados)
			self.addFileTypes.start()
			self.addFileTypes.start()
	
	
	def archivosAdicionados(self):
                self.progressBar_2.setRange(0,1)
                self.progressBar_2.setValue(1)
		self.pushButton_7.setEnabled(True)
		cantidad=self.addFileTypes.cantidad
		if cantidad>0:
			QMessageBox.about(self.form1, "OnlyOne", str(QApplication.translate("MainWindow",'Se han encontrado %s tipos de archivos no registrados'))%cantidad) 
		else:
			QMessageBox.about(self.form1, "OnlyOne", str(QApplication.translate("MainWindow",'No se encontraron tipos de archivos no registrados'))) 
	
	
	def onCloseEvent(self,event):
		"""Se ejecuta al cerrar la aplicacion"""
		self.config.save(self.fileLocation,self.opacity,self.lang)
		event.accept()
 
 
	def scanner(self):		
		try:
			if self.con>0:
				self.form1.setCursor(Qt.WaitCursor)
				self.widget_09.setVisible(False)
				self.pushButton_10.setEnabled(False)
				self.pushButton_11.setEnabled(False)
				self.pushButton_12.setEnabled(False)
				self.pushButton_74.setEnabled(False)
				self.pushButton_75.setEnabled(False)
				self.pushButton_66.setEnabled(False)
				self.pushButton_13.setEnabled(False)
				self.pushButton_14.setEnabled(False)
				self.pushButton_15.setEnabled(False)
				self.pushButton_16.setEnabled(False)
				self.pushButton_17.setEnabled(False)
				
				if self.doubleSpinBox.value()>0:
					if self.comboBox.currentIndex ()==0:
						divisor=1
					elif self.comboBox.currentIndex ()==1:
						divisor=1024
					elif self.comboBox.currentIndex ()==2:
						divisor=1024*1024
					elif self.comboBox.currentIndex ()==3:
						divisor=1024*1024*1024
					self.mayork=self.doubleSpinBox.value()*divisor
				if self.doubleSpinBox_2.value()>0:
					if self.comboBox_2.currentIndex ()==0:
						divisor=1
					elif self.comboBox_2.currentIndex ()==1:
						divisor=1024
					elif self.comboBox_2.currentIndex ()==2:
						divisor=1024*1024
					elif self.comboBox_2.currentIndex ()==3:
						divisor=1024*1024*1024
					self.menork=self.doubleSpinBox_2.value()*divisor
				if self.exc > 0:
					self.excDir=[]
					for i in range(self.kurlrequester_2.count()):						
						item=self.kurlrequester_2.item(i)						
						if not item.isHidden():
							if not item.text().toUtf8().data() in self.excDir:
								self.excDir.append(item.text().toUtf8().data())
				
				self.direcciones=[]
				for i in range(self.kurlrequester.count()):
					item=self.kurlrequester.item(i)	
					if not item.isHidden():
						if not item.text().toUtf8().data() in self.direcciones:
							self.direcciones.append(item.text().toUtf8().data())
				
				self.progressBar.setVisible(True)
				self.progressBar.setRange(0,0)
				
				self.label_8.setText("0")
				self.label_9.setText("0")
				self.label_10.setText("")
				self.label_11.setText("")
				self.label_12.setText("")
				self.label_13.setText("")				
				self.label_99.setText("")
				self.label_999.setText("0")
				self.label_9999.setText("(0)")
				self.label_99999.setText("(0)")
				self.label_17.setVisible(False)
				self.label_18.setVisible(False)
				self.label_19.setVisible(False)
				self.label_20.setVisible(False)
				
				self.label_15.setVisible(True)
				self.label_16.setVisible(True)			
				self.label_999.setVisible(True)
				self.label_9999.setVisible(True)
				self.label_99999.setVisible(True)
				self.label_9.setVisible(True)
				self.label_8.setVisible(True)
				self.label_988.setVisible(True)
				self.label_9888.setVisible(True)
				self.label_98888.setVisible(True)
				
				if self.radio1.isChecked():
					from Crypto.Hash import MD2 as hash
				elif self.radio2.isChecked():
					from Crypto.Hash import MD4 as hash
				elif self.radio3.isChecked():
					from Crypto.Hash import MD5 as hash
				elif self.radio4.isChecked():
					from Crypto.Hash import SHA224 as hash
				elif self.radio5.isChecked():
					from Crypto.Hash import SHA256 as hash
				elif self.radio6.isChecked():
					from Crypto.Hash import SHA512 as hash
				
				if self.checkBox_5.isChecked():
					for type in metaData.levantar('image',True):
						if str(type).split("'")[1].split('/')[0]=='image':
							self.conExten.append(type)
				if self.checkBox_6.isChecked():
					for type in metaData.levantar('video',True):
						if str(type).split("'")[1].split('/')[0]=='video':
							self.conExten.append(type)
				if self.checkBox_9.isChecked():
					for type in metaData.levantar('audio',True):
						if str(type).split("'")[1].split('/')[0]=='audio':
							self.conExten.append(type)
				
				if self.checkBox_7.isChecked():
					for type in metaData.levantar('image',True):
						if str(type).split("'")[1].split('/')[0]=='image':
							if self.sinExten==['']:
								self.sinExten[0]=type
							else:
								self.sinExten.append(type)
				if self.checkBox_8.isChecked():
					for type in metaData.levantar('video',True):
						if str(type).split("'")[1].split('/')[0]=='video':
							if self.sinExten==['']:
								self.sinExten[0]=type
							else:
								self.sinExten.append(type)
				if self.checkBox_10.isChecked():
					for type in metaData.levantar('audio',True):
						if str(type).split("'")[1].split('/')[0]=='audio':
							if self.sinExten==['']:
								self.sinExten[0]=type
							else:
								self.sinExten.append(type)
				
				self.search = makeSearch(hash,self.direcciones,self.excDir,self.conExten,self.sinExten,self.menork,self.mayork)
				self.search.taskFinished.connect(self.scannerHasFinished)
				self.search.posibles_repetidos.connect(self.actRepe)
				self.search.s_grupos.connect(self.actGru)
				self.search.total_revisados.connect(self.actTotal)
				self.search.total_temp.connect(self.actTemp)
				self.search.dir_vacions.connect(self.actVacios)
				self.search.rev_sig.connect(self.actPos)				
				self.search.start()
				self.pushButton_666.setVisible(True)		
				self.pushButton_6.setVisible(False)				
				
		except:
			self.form1.setCursor(Qt.ArrowCursor)
			QMessageBox.about(self.form1, "OnlyOne", win._fromUtf8(QApplication.translate("MainWindow", 'La aplicación experimentó un error debido a que existen caracteres extraños en la dirección')))

		
	def actTotal(self):
		cant=int(self.label_999.text())
		self.label_999.setText(str(cant+1))
		
	def actTemp(self):
		cant=int(self.label_99999.text().split('(')[1].split(')')[0])
		self.label_99999.setText('('+str(cant+1)+')')
		if self.panelActivo==2:
			self.label_099.setText(self.label_99999.text())

	def actVacios(self):
		cant=int(self.label_9999.text().split('(')[1].split(')')[0])
		self.label_9999.setText('('+str(cant+1)+')')
		if self.panelActivo==1:
			self.label_099.setText(self.label_9999.text())
		
	def actRepe(self):
		self.label_16.setText(QApplication.translate("MainWindow",'Posibles Repetidos:'))
		cant=int(self.label_9.text())
		self.label_9.setText(str(cant+1))
		
	def actPos(self):
		photo='wait_'+self.lang+'.png'
		self.form1.setCursor(QCursor(QPixmap('pixmaps/onlyone/'+photo)))
		
		
	def actGru(self):
		self.label_15.setText(QApplication.translate("MainWindow", 'Cantidad de Grupos:'))
		cant=int(self.label_8.text())    
		self.label_8.setText(str(cant+1))
	
	def cancelar(self):
		ret = QMessageBox.warning(self.form1,win._fromUtf8(QApplication.translate('MainWindow','Atemción!')),win._fromUtf8(QApplication.translate('MainWindow','¿Está seguro de que desea cancelar la búsqueda?')),QMessageBox.No,QMessageBox.Yes)
		if ret==QMessageBox.Yes:
			if self.search.isRunning ():
				self.search.terminate()
				
	
	def scannerHasFinished(self):
		self.label_16.setText(QApplication.translate("MainWindow",'Cantidad Total:'))
		self.toolBox.setCurrentIndex (2)
		data=self.search.data
		self.direcciones=data[0]
		self.totalArchivos=data[1]
		self.archivosAbiertos=data[2]
		self.dirVacios=data[3]
		self.repetidos=data[4]
		self.tiempoDemora=data[5]
		
		self.progressBar.setRange(0,1)
		self.progressBar.setValue(1)
		self.pushButton_666.setVisible(False)
		self.pushButton_6.setVisible(True)
		
		self.itemList=[]
		g=0
		for grupo in self.repetidos:
			for data in grupo:				
				item=Item(data,g)
				self.itemList.append(item)
			g=g+1
			
		self.createTable()
		
		self.label_8.setText(win._fromUtf8(str(g+1)))
		self.label_9.setText(win._fromUtf8(str(len(self.itemList))))
		
		self.label_17.setVisible(True)
		self.label_18.setVisible(True)
		self.label_19.setVisible(True)
		self.label_20.setVisible(True)
		
		self.data()
		self.reiniciarFiltros()
		self.pushButton_10.setEnabled(True)
		self.pushButton_11.setEnabled(True)
		self.pushButton_12.setEnabled(True)
		self.pushButton_74.setEnabled(True)
		self.pushButton_75.setEnabled(True)
		self.pushButton_66.setEnabled(True)
		self.pushButton_14.setEnabled(True)
		self.pushButton_15.setEnabled(True)
		self.pushButton_16.setEnabled(True)
		self.pushButton_17.setEnabled(True)
		
		self.doubleSpinBox_2.setValue(0.0)
		self.doubleSpinBox.setValue(0.0)
		self.lineEdit_2.setText("")
		self.lineEdit_3.setText("")
		self.listWidget_3.clear()
		self.listWidget_4.clear()
		self.checkBox_5.setChecked(False)
		self.checkBox_6.setChecked(False)
		self.checkBox_7.setChecked(False)
		self.checkBox_8.setChecked(False)
		self.checkBox_9.setChecked(False)
		self.checkBox_10.setChecked(False)
		self.cantSE=0
		self.cantCE=0
		self.form1.setCursor(Qt.ArrowCursor)
		
	
	def marcarDesmarcarItem(self,item):
		if item.checked:
			item.checked=False
		else:
			item.checked=True	
	
	
	def marcarDesmarcar(self,asd):
		self.model.emit(SIGNAL("layoutAboutToBeChanged()"))
		if len(self.treeView.selectedIndexes())==1:
			self.marcarDesmarcarItem(self.model.arraydata[self.treeView.selectedIndexes()[0].row()])
			self.ultimo=self.model.arraydata[self.treeView.selectedIndexes()[0].row()]
		else:
			miLista=self.treeView.selectedIndexes()
			for index in miLista:
				self.marcarDesmarcarItem(self.model.arraydata[index.row()])
			if self.ultimo==self.model.arraydata[self.treeView.selectedIndexes()[0].row()]:
				self.marcarDesmarcarItem(self.model.arraydata[self.treeView.selectedIndexes()[0].row()])
			elif self.ultimo!=None:
				self.marcarDesmarcarItem(self.model.arraydata[self.treeView.selectedIndexes()[-1].row()])
			self.ultimo=None
		self.data()
		self.model.emit(SIGNAL("layoutChanged()"))
		
	
	def createTable(self):
		header = [win._fromUtf8(QApplication.translate("MainWindow",'DIRECTORIO')), win._fromUtf8(QApplication.translate("MainWindow",'TAMAÑO')), win._fromUtf8(QApplication.translate("MainWindow",'TIPO')), win._fromUtf8(QApplication.translate("MainWindow",'MODIFICADO'))]
		self.model = MyTableModel(self.itemList, header, self.form1)
		self.model.sort(2,None)
		self.treeView.setModel(self.model )
		self.treeView.setShowGrid(False)
		vh = self.treeView .verticalHeader()
		vh.setVisible(False)
		hh = self.treeView .horizontalHeader()
		self.treeView.resizeColumnsToContents()
		nrows = len(self.itemList)
		self.treeView.setColumnWidth(0,self.treeView.width()-(322))
		self.treeView.setColumnWidth(1,90)
		self.treeView.setColumnWidth(2,90)
		self.treeView.setColumnWidth(3,120)
		self.treeView.setSortingEnabled(True)
	 
	 
	def data(self):
		"""Actualiza la informacion atendiendo a las acciones del usuario"""
		self.label_8.setText(win._fromUtf8(str(self.model.cantGrupos())))
		self.label_9.setText(win._fromUtf8(str(len(self.model.arraydata))))
		self.label_10.setText(win._fromUtf8(str(self.model.cantMarcados())))		
		self.label_11.setText(win._fromUtf8(str(self.PesoArchivosNoMarcados())))
		self.label_12.setText(win._fromUtf8(str(self.PesoArchivosMarcados())))		
		self.label_13.setText(win._fromUtf8(str(self.PesoTotal())))		
		self.label_98.setVisible(True)
		self.label_99.setText(win._fromUtf8(str(self.tiempoDemora)))
		self.label_999.setText(win._fromUtf8(str(self.totalArchivos)))
		self.label_9999.setText('('+win._fromUtf8(str(len(self.dirVacios)))+')')
		self.label_99999.setText('('+win._fromUtf8(str(len(self.archivosAbiertos)))+')')
		self.label_099.setText(self.label_9999.text())
		
	 
	def PesoArchivosNoMarcados(self):
		peso=0
		for item in self.model.arraydata:
			if not item.checked:
				peso+=pesoEnByte(item.column(1))
		return metaData.peso(peso)
	 
	
	def PesoArchivosMarcados(self):
		peso=0
		for item in self.model.arraydata:
			if item.checked:
				peso+=pesoEnByte(item.column(1))
		return metaData.peso(peso)
	 
	
	def PesoTotal(self):
		peso=0
		for item in self.model.arraydata:
			peso+=pesoEnByte(item.column(1))
		return metaData.peso(peso) 	 

		
	def Error(self,error):
		"""Crea una ventana mostrando la informacion del error"""
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
		
		lista=s.split(error,":")
		self.label_777.setText(win._fromUtf8(lista[0]))
		self.plainTextEdit_777.appendPlainText(win._fromUtf8(lista[1])+"\n")
		errores=s.split(lista[2],"***")
		for e in errores:
			self.plainTextEdit_777.appendPlainText(win._fromUtf8(e+"\n"))
			
		self.groupBox_777.setWindowTitle(QApplication.translate("MainWindow",'Error'))
		self.groupBox_777.show()
	  
 
	def reiniciarFiltros(self):
		self.conExten=[]
		self.sinExten=['']
		self.mayork=0
		self.menork=0
		self.excDir=[]
		
		
	def format(self):
		self.totalArchivos=0
		self.archivosAbiertos=[]
		self.dirVacios=[]
		self.repetidos=[]
		self.datos=[]
		self.tiempoDemora=0		
		self.direcciones=[]
		self.excDir=[]
		self.conExten=[]
		self.sinExten=['']
		self.menork=0
		self.mayork=0
 
class Item:
	def __init__(self,data,grupo):
		self.checked=False
		self.data=data
		self.grupo=grupo
		self.color=''
		self.encontrado=False
	
	def column(self,n):
		if n==1:
			return self.data[2]
		elif n==2:
			if self.data[3]=='(None, None)':
				return "None"		
			partes=s.split(self.data[3],"\'")
			tipo=s.split(partes[1],"/")
			if tipo[0]=="image" or tipo[0]=="application":
				tip=s.split(tipo[1],".")
				return tip[len(tip)-1]
			if tipo[0]=="audio":
				return "A/"+tipo[1]
			if tipo[0]=="video":
				return "V/"+tipo[1]
			return partes[1]
		elif n==3:
			return str(self.data[1])
		else:
			return self.data[0]

 
class MyTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
		QAbstractTableModel.__init__(self, parent, *args) 
		self.arraydata = datain
		self.headerdata = headerdata
 
    def removeRow(self,row):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		del self.arraydata[row]
		self.emit(SIGNAL("layoutChanged()"))
    
    def rowCount(self, parent): 
		return len(self.arraydata) 
 
    def columnCount(self, parent):
		return 4
	
    
    def flags(self, index):
	        if index.column() == 0:
			return  Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
	if role == Qt.BackgroundRole :
		if not self.arraydata[index.row()].encontrado:
			if index.row()==0:
				self.arraydata[0].color=QColor('#ffffff')
			else:
				col_ant=self.arraydata[(index.row()-1)].color
				if self.arraydata[index.row()].grupo==self.arraydata[(index.row()-1)].grupo:					
					if col_ant== QColor('#ffffff') or col_ant== QColor('#91C1F4'):
						self.arraydata[index.row()].color=QColor('#ffffff')
					else:
						self.arraydata[index.row()].color=QColor('#bfbfbf')					
				else:
					if col_ant==QColor('#ffffff') or col_ant==QColor('#91C1F4'):
						self.arraydata[index.row()].color=QColor('#bfbfbf')
					else:
						self.arraydata[index.row()].color=QColor('#ffffff')						
		else:
			if index.row()==0:
				self.arraydata[0].color=QColor('#5D9EE3')
			else:
				col_ant=self.arraydata[(index.row()-1)].color
				if self.arraydata[index.row()].grupo==self.arraydata[(index.row()-1)].grupo:					
					if col_ant== QColor('#ffffff') or col_ant== QColor('#91C1F4'):
						self.arraydata[index.row()].color=QColor('#91C1F4')
					else:
						self.arraydata[index.row()].color=QColor('#5D9EE3')					
				else:
					if col_ant==QColor('#ffffff') or col_ant==QColor('#91C1F4'):
						self.arraydata[index.row()].color=QColor('#5D9EE3')
					else:
						self.arraydata[index.row()].color=QColor('#91C1F4')		
		return self.arraydata[index.row()].color	
		
	if role == Qt.CheckStateRole:
		if index.column() == 0:
			if self.arraydata[index.row()].checked:
				return QVariant(Qt.Checked)
			else:
				return QVariant(Qt.Unchecked)
        if role == Qt.DisplayRole:
		if sys.platform=="linux" or sys.platform == "linux2":
			return QVariant(win._fromUtf8(str(self.arraydata[index.row()].column(index.column()))))
		else:
			return self.arraydata[index.row()].column(index.column())
	

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, column, order):
	if column!=0 and column!=3:
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		if column!=1:
			self.arraydata = sorted(self.arraydata, key=lambda x: x.column(column), reverse=True) 
		else:
			self.arraydata = sorted(self.arraydata, key=lambda x: pesoEnByte(x.column(column)), reverse=True) 
		if order == Qt.DescendingOrder:
		    self.arraydata.reverse()
		self.emit(SIGNAL("layoutChanged()"))
	
    def cantGrupos(self):
	if len(self.arraydata)>0:
		cant=0
		item=self.arraydata[0]
		cambio=item.grupo
		cant+=1
		for item in self.arraydata[1:]:
			temp = item.grupo
			if temp!=cambio:
				cambio=temp
				cant+=1
		return cant
		    
    def cantMarcados(self):
		cont=0
		for item in self.arraydata:
			if item.checked==True:
				cont+=1
		return cont
		    
    def marcar(self):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		for item in self.arraydata:
			item.checked=True	
		self.emit(SIGNAL("layoutChanged()"))
		    
    def desmarcar(self):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		for item in self.arraydata:
			item.checked=False
		self.emit(SIGNAL("layoutChanged()"))
		
    def dejarUno(self):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		item =self.arraydata[0]
		item.checked=False
		grupo=item.grupo
		for item in self.arraydata[1:]:
			if grupo==item.grupo:
				item.checked=True
			else:
				grupo=item.grupo
				item.checked=False
		self.emit(SIGNAL("layoutChanged()"))
		
    def dejarNuevo(self):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		item =self.arraydata[0]
		item.checked=True
		grupo=item.grupo
		fecha=item.column(3)
		pos=0
		for item in self.arraydata[1:]:
			temp=item.color
			if grupo==item.grupo:
				if fecha>item.column(3):
					fecha=item.column(3)
					pos=self.arraydata.index(item)
				item.checked=True
			else:
				self.arraydata[pos].checked=False
				grupo=item.grupo
				fecha=item.column(3)
				pos=self.arraydata.index(item)				
				item.checked=True
			if self.arraydata.index(item)+1==len(self.arraydata):
				self.arraydata[pos].checked=False
		self.emit(SIGNAL("layoutChanged()"))
		
    def dejarViejo(self):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		item =self.arraydata[0]
		item.checked=True
		grupo=item.grupo
		fecha=item.column(3)
		pos=0
		for item in self.arraydata[1:]:
			temp=item.color
			if grupo==item.grupo:
				if fecha<item.column(3):
					fecha=item.column(3)
					pos=self.arraydata.index(item)
				item.checked=True
			else:
				self.arraydata[pos].checked=False
				grupo=item.grupo
				fecha=item.column(3)
				pos=self.arraydata.index(item)				
				item.checked=True
			if self.arraydata.index(item)+1==len(self.arraydata):
				self.arraydata[pos].checked=False
		self.emit(SIGNAL("layoutChanged()"))
			
    def marcarEncontrados(self,encontrados):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		for item in self.arraydata:
			if item.data[0] in encontrados:
				item.checked=True
		self.emit(SIGNAL("layoutChanged()"))
		
    def desmarcarEncontrados(self,encontrados):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		for item in self.arraydata:
			if item.data[0] in encontrados:
				item.checked=False
		self.emit(SIGNAL("layoutChanged()"))
		
    def dejarUnEncontrados(self,encontrados):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))		
		
		group=None
		for item in self.arraydata:
			if item.data[0] in encontrados:
				if item.grupo==group:
					item.checked=True
				else:
					item.checked=False
					group=item.grupo
		self.emit(SIGNAL("layoutChanged()"))

		    
    def removeRows2(self,estado):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		self.errores=''
		for i in range(len(self.arraydata))[::-1]:
			if self.arraydata[i].checked==estado:
				try:
					os.remove(self.arraydata[i].data[0])
				except:
					self.errores=self.errores+str(self.arraydata[i].data[0])+"***"
				del self.arraydata[i]
		self.emit(SIGNAL("layoutChanged()"))	

    def removeRows3(self,indexs):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		self.errores=''
		for i in indexs:
			try:
				os.remove(self.arraydata[i].data[0])
			except:
				self.errores=self.errores+str(self.arraydata[i].data[0])+"***"
			del self.arraydata[i]
		self.emit(SIGNAL("layoutChanged()"))			
	   

def main():
	app = QApplication(sys.argv)
	
	conf=config()
	c=conf.load()
	locale=''
	if c:	
		locale=c[2]
	if locale=='' or locale=='locale' or locale=='None':	
		locale =unicode(QLocale.system().name())
	translator=QTranslator()
	translator.load("Locale/onlyone_"+locale)
	app.installTranslator(translator)
	
	qtTranslator=QTranslator()
	qtTranslator.load("qt_"+ locale,QLibraryInfo.location(QLibraryInfo.TranslationsPath))
	app.installTranslator(qtTranslator)
	
	
	
	f = cMainWindow()
	app.exec_()

if __name__=='__main__':
	main()

	