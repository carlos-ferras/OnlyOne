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

import os
import mimetypes

class metaData():
	
	def __init__(self):
		 pass	
	
	def extencion(self,dir):
		"""Saca la extencion del archivo por el nombre del archivo en caso de no tener alguna, se toma como un archivo de texto plano"""
		try:
			tipo=mimetypes.guess_type(dir)
		except:
			tipo="undefined"

		return tipo
		
	def peso(self,tamano, un_kilobyte_es_1024_bytes=True ) :
		"""Calcula el tamanno del archivo"""
		SUFIJOS = { 1024: [ "KB" , "MB" , "GB" , "TB" , "PB" , "EB" , "ZB" ,"YB" ] }    
		multiplo = 1024.0
		for sufijo in SUFIJOS[multiplo]:
			tamano /= multiplo   
			if tamano < multiplo:
				return "{0:.5f} {1}".format(tamano, sufijo)
				
	def guardar(self,tipos):
		"""Guarda los mimetypes encontrados en el fichero:ficheros"""
		dirFichero='action/ficheros'
		fichero=open(dirFichero,'r+')
		tengo=fichero.readlines()
		fichero.seek(-1,1)
		fichero.write("\n");
		for tipo in tipos:
			fichero.write(tipo);
			fichero.write("\n");
		fichero.close()
		
	def levantar(self,busqueda):
		"""devuelve los mimetypes k en su nombre tienen coincidancias con la busqueda"""
		import string
		coinciden=[]
		dirFichero='action/ficheros'
		fichero=open(dirFichero,'r')
		tipos=fichero.readlines()
		for tipo in tipos:
			if ((string.find(tipo,busqueda))!=-1):
				coinciden.append(string.split(tipo,"\n")[0])
		fichero.close()
		return coinciden
		
	def adicionarTipos(self):
		"""Adiciona al fichero tipos, los tipos encontrados de los k no contenia"""
		import mimetypes
		
		tipos2=self.levantar("")
		tipos=['']
		add=[]

		for base, dirs, files in os.walk("/"):
			hijos=os.listdir(base)
			for elemento in hijos:
				if os.path.isfile(base+"/"+elemento):
					tipo=self.extencion(base+"/"+elemento)
					a=0
					for t in tipos:
						if t==str(tipo): 
							a=1
					if a==0:
						tipos.append(str(tipo))

		del tipos[0]
		a=0
		for t in tipos:
			for t2 in tipos2:
				if t2==t: 
					a=1
			if a==0:
				add.append(t)
		self.guardar(add)
		
		return len(add)
			