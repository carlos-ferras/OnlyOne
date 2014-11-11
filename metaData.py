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
#os.chdir('/usr/share/onlyone')
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
		dirFichero='ficheros'
		fichero=open(dirFichero,'r+')
		tengo=fichero.readlines()
		if len(tengo)>0:
			fichero.seek(-1,1)
		fichero.write("\n")
		for tipo in tipos:
			fichero.write(tipo)
			fichero.write("\n")
		fichero.close()
		
	def levantar(self,busqueda,familia=False):
		"""devuelve los mimetypes k en su nombre tienen coincidancias con la busqueda"""
		import string
		coinciden=[]
		dirFichero='ficheros'
		fichero=open(dirFichero,'r')
		tipos=fichero.readlines()
		fichero.close()
		
		def aux(n):
			if n.find(busqueda)!=-1:
				return n			
		coinciden=filter(aux,tipos)		
		if not familia:
			temp=[]
			for n in coinciden:
				try:
					temp.append(n.split("'")[1])
				except:
					pass
			coinciden=[]
			coinciden=temp
			for  i in range(len(coinciden))[::-1]:
				temp = coinciden[i]
				if temp in coinciden[:i]:
					del coinciden[i]	
		return coinciden
		
	def adicionarTipos(self,dir):
		"""Adiciona al fichero tipos, los tipos encontrados de los k no contenia"""
		import mimetypes
		
		tipos2=self.levantar("",True)
		tipos=['']
		add=[]

		for base, dirs, files in os.walk(str(dir)):
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
		for t in tipos:
			if not str(t)+'\n' in tipos2:
				add.append(t)
		self.guardar(add)
		
		return len(add)
			
