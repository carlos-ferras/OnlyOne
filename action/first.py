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
import time
from dateutil import parser
import datetime
import threading
import string as s

class first():
	def __init__(self,direccion,conExten,sinExten,mayork,menork,excDir,metaData,totalArchivos,rep,noMarcados,repetidos,encontrado,archivosAbiertos,dirVacios):
		self.metaData= metaData
		self.totalArchivos=totalArchivos
		self.archivosAbiertos=archivosAbiertos
		self.dirVacios=dirVacios
	
		"""Aqui se rellena un arreglo "totalArchivos[]" con todos los archivos anidados dentro del directorio entrado por el usuario"""
		#hora de inicio
		self.horaInicio=datetime.datetime.fromtimestamp(time.time())
		carpetas=s.split(excDir,"/")
		del carpetas[0]
		for base, dirs, files in os.walk(direccion):			
			if len(carpetas)>1:
				carpetasBase=s.split(base,"/")
				del carpetasBase[0]
				if len(carpetasBase)>=len(carpetas):					
					coincide=True
					for i in range(len(carpetas)):
						if carpetasBase[i]!=carpetas[i]:
							coincide=False
							break
					if coincide==True:
						continue
				
			hijos=os.listdir(base)
			if len(hijos)==0:
				dirVacios.append(base)
				continue
				
			hijos=os.listdir(base)
			for elemento in hijos:
				        if os.path.isfile(base+"/"+elemento):
					        meta=os.stat(base+"/"+elemento)
					        tipo=metaData.extencion(base+"/"+elemento)
                                                if(elemento[len(elemento)-1]=="~"):
						        archivosAbiertos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
                                                        continue	
					        if(conExten!=[]):
                                                        for ext in conExten:
                                                                if(str(tipo)==ext):
                                                                        for ext in sinExten:
                                                                                if(str(tipo)!=ext):
											totalArchivos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif(menork!=0L):
                                                        if((meta.st_size>mayork)and(meta.st_size<menork)):
                                                                for ext in sinExten:
                                                                        if(str(tipo)!=ext):
										totalArchivos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif(menork==0L):
                                                        if(meta.st_size>mayork):
                                                                for ext in sinExten:
                                                                        if(str(tipo)!=ext):
										totalArchivos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif((conExten!=[])and(menork!=0L)):
                                                        if((meta.st_size>mayork)and(meta.st_size<menork)):
                                                                for ext in conExten:
                                                                        if(str(tipo)==ext):
									        for ext in sinExten:
                                                                                        if(str(tipo)!=ext):
												totalArchivos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif((conExten!=[])and(menork==0L)):
                                                        if(meta.st_size>mayork):
                                                                for ext in conExten:
                                                                        if(str(tipo)==ext):
                                                                                for ext in sinExten:
                                                                                        if(str(tipo)!=ext):
												totalArchivos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        else:
                                                        for ext in sinExten:
                                                                if(str(tipo)!=ext):
									totalArchivos.append([base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])

		"""Aqui se crean las listas de ficheros repetidos"""	
		self.rep=[]
		self.grupo=[[["","","",""]]]
		self.tamGrupo=1
		for i in range(len(totalArchivos)):
			accion=True
			for j in range(len(self.grupo)):
				if((totalArchivos[i][1]==self.grupo[j][0][1]) and (totalArchivos[i][2]==self.grupo[j][0][2]) and (totalArchivos[i][3]==self.grupo[j][0][3])):
					self.grupo[j].append(totalArchivos[i])
					accion=False
					break
			if accion==True:
				self.grupo.append([totalArchivos[i]])
			if len(self.grupo)==self.tamGrupo:
				self.rep.append(self.grupo)
				self.grupo=[[["","","",""]]]
				
		self.rep.append(self.grupo)
		
		def unir(self,grupoDeGrupos1,grupoDeGrupos2):
			"""Para unir 2 listas en una"""
			grupoDeGrupos=grupoDeGrupos1
			tope=len(grupoDeGrupos)
			for i in range(len(grupoDeGrupos2)):
				accion=True
				for j in range(tope):
					if( (grupoDeGrupos2[i][0][1]==grupoDeGrupos[j][0][1]) and (grupoDeGrupos2[i][0][2]==grupoDeGrupos[j][0][2]) and (grupoDeGrupos2[i][0][3]==grupoDeGrupos[j][0][3])):
						grupoDeGrupos[j]=grupoDeGrupos[j]+grupoDeGrupos2[i]
						accion=False
						break
				if accion==True:
					grupoDeGrupos.append(grupoDeGrupos2[i])
			return grupoDeGrupos
		
		
		
		def reducir(self,x):
			"""Es quien se encarga de comvertir todas las listas en una sola"""
			aux=0
			repe=[]
			while aux+1<len(x):
				repe.append(unir(self,x[aux],x[aux+1]))
				aux=aux+2
			if aux==len(x)-1:
				repe.append(x[aux])
			if len(repe)==1:
				return repe[0]
			else:
				return reducir(self,repe)
					
		self.rep=reducir(self,self.rep)
		del self.rep[0]


	
		self.noMarcados=noMarcados
		self.repetidos=repetidos		
				
		def rellenarNoMarcados(self,grupo):
			"""rellena la lista de archivos sin marcar con todos los archivos encontrados"""
			for tupla in grupo:
				self.noMarcados.append(tupla)
			
	
		"""Elimina las tuplas k contienen un soo elemento, es decir, k no tienen repetidos"""
		for grupo in self.rep:
			if (len(grupo)!=1):
				self.repetidos.append(grupo)
				rellenarNoMarcados(self,grupo)
				
		self.encontrado=[]
		
		#hora de Fin
		self.horaFin=datetime.datetime.fromtimestamp(time.time())	
				
	def cantidades(self):
		"""devuelve cuantos grupos hay, y cuantos archivos en total[grupos,archivos]"""
		groups=0
		files=0
		for grupo in self.repetidos:
			groups=groups+1
			for tupla in grupo:
				files=files+1
		return groups,files
		
	def encontrar(self,cadena):
		"""busca dentro de los archivos repetidos, los que en su direccion o en su nombre coinciden con la cadena entrada"""
		import string as s
		self.encontrado=[]
		for grupo in self.repetidos:
			for tupla in grupo:
				esta=s.find(tupla[0],cadena)
				if (esta!=-1):
					self.encontrado.append(tupla)
		return self.encontrado
		
	def getTotalArchivos(self):
		return self.totalArchivos
		
	def getArchivosAbiertos(self):
		return self.archivosAbiertos
		
	def getNoMarcados(self):
		return self.noMarcados
	
	def getRepetidos(self):
		return self.repetidos
		
	def getEncontrado(self):
		return self.encontrado
		
	def getDirVacios(self):
		return self.dirVacios
		
	def getTiempoDemora(self):
		return self.horaFin-self.horaInicio
		
