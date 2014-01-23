#!/usr/bin/env python
# -*- coding: utf-8 -*-

#OnlyOne is an application to remove duplicated files within a specified directory
#Copyright (C) 2014 Carlos Manuel Ferrás Hernández
#
#This file is part of OnlyOne.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

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
		
		
		
		
		
		