#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from dateutil import parser
import datetime
import threading

class first():
	def __init__(self,direccion,conExten,sinExten,mayork,menork,excDir,metaData,totalArchivos,rep,noMarcados,repetidos,encontrado,archivosAbiertos,dirVacios):
		self.metaData= metaData
		self.totalArchivos=totalArchivos
		self.archivosAbiertos=archivosAbiertos
		self.dirVacios=dirVacios
		
		
		class MiThread(threading.Thread):
                        def __init__(self, base):
                                threading.Thread.__init__(self)
                                self.base = base
                                
                        def run(self):
                            
			        hijos=os.listdir(self.base)
			        for elemento in hijos:
				        if os.path.isfile(self.base+"/"+elemento):
					        meta=os.stat(self.base+"/"+elemento)
					        tipo=metaData.extencion(self.base+"/"+elemento)
                                                if(elemento[len(elemento)-1]=="~"):
						        archivosAbiertos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
                                                        continue	
					        if(conExten!=[]):
                                                        for ext in conExten:
                                                                if(str(tipo)==ext):
                                                                        for ext in sinExten:
                                                                                if(str(tipo)!=ext):
											totalArchivos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif(menork!=0L):
                                                        if((meta.st_size>mayork)and(meta.st_size<menork)):
                                                                for ext in sinExten:
                                                                        if(str(tipo)!=ext):
										totalArchivos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif(menork==0L):
                                                        if(meta.st_size>mayork):
                                                                for ext in sinExten:
                                                                        if(str(tipo)!=ext):
										totalArchivos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif((conExten!=[])and(menork!=0L)):
                                                        if((meta.st_size>mayork)and(meta.st_size<menork)):
                                                                for ext in conExten:
                                                                        if(str(tipo)==ext):
									        for ext in sinExten:
                                                                                        if(str(tipo)!=ext):
												totalArchivos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        elif((conExten!=[])and(menork==0L)):
                                                        if(meta.st_size>mayork):
                                                                for ext in conExten:
                                                                        if(str(tipo)==ext):
                                                                                for ext in sinExten:
                                                                                        if(str(tipo)!=ext):
												totalArchivos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])
					        else:
                                                        for ext in sinExten:
                                                                if(str(tipo)!=ext):
									totalArchivos.append([self.base+"/"+elemento,time.ctime(meta.st_mtime),metaData.peso(meta.st_size),str(tipo)])

		
		class MiThread2(threading.Thread):
                        def __init__(self, grupo,tupla):
                                threading.Thread.__init__(self)
                                self.grupo = grupo
				self.tupla=tupla
                                self.estado="false"
                                
                        def run(self):
				for dir in self.grupo:
					if (dir[0]==self.tupla[0]):
						self.estado="true"
		
		
	
		"""Aqui se rellena un arreglo "totalArchivos[]" con todos los archivos anidados dentro del directorio entrado por el usuario"""
		#hora de inicio
		self.horaInicio=datetime.datetime.fromtimestamp(time.time())
		for base, dirs, files in os.walk(direccion):
			if base==excDir:
				continue
			hijos=os.listdir(base)
			if len(hijos)==0:
				dirVacios.append(base)
				continue
				
			t = MiThread(base)
                        t.start()
                        t.join()
			
		self.rep=rep
			
		def existe(self,tupla):
			"""Busca si ya el fichero se agrego a la lista de archivos revisados"""
			for grupo in rep:
				t2=MiThread2(grupo,tupla)
				t2.start()
				t2.join()
                                return t2.estado	 
		 
		def concuerda(self,tupla):
			"""Busca si el archivo en cuestion es igual a alguno de los ya revisados"""
			pos=0
			for grupo in self.rep:
				if((grupo[0][1]==tupla[1]) and (grupo[0][2]==tupla[2]) and (grupo[0][3]==tupla[3])):
					self.rep[pos].append(tupla)
					return "true"
				pos=pos+1
			return "false"
	
	
		"""Ejecuta las funciones anteriores para definir los archivos k se repiten y los k no"""
		for tupla in self.totalArchivos:
			existencia=existe(self,tupla)
			if(existencia=="false"):
				tieneHermano=concuerda(self,tupla)
				if(tieneHermano=="false"):
					self.rep.append([tupla])
	
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
		
