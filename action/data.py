#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string as s

class data():
	
	#marcados, lo libera options
	def __init__(self,metaData):
		self.metaData= metaData
	
	def pesoEnByte(self,peso):
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
		
	def pesoArchivos(self,lista):
		"""devuelve cuanto pesan todos los archivos pasados por parametro"""
		p=0  
		for tupla in lista:
			tamano=self.pesoEnByte(tupla[2])
			p+=tamano
		return self.metaData.peso(p)
	
	#revisar este metodo
	def pesoTotal(self,marcados,noMarcados):
		"""devuelbe cuanto pesan todos los archivos encontrados, en total"""

		tamano1=self.pesoEnByte(self.pesoArchivos(marcados))
		tamano2=self.pesoEnByte(self.pesoArchivos(noMarcados))
		return self.metaData.peso(tamano1+tamano2)
		
		
	def pesoGrupo(self,grupo):
		"""devuelve cuanto pesa un archivo del grupo pasado por parametro"""
		return grupo[0][2]
		
	def cantMarcados(self,marcados):
		"""devuelbe cuantos archivos hay marcados"""
		return len(marcados)	
		
	def fechaGrupo(self,grupo):
		"""devuelve la fecha de modificacion de los archivos de un grupo"""
		return grupo[0][1]
		
	def tipoGrupo(self,grupo):
		"""devuelve el tipo de archivo de los archivos un grupo"""
		return grupo[0][3]
		
		
		
		
		
		