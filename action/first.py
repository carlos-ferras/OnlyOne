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

			
		self.rep=[]
		self.grupo=[[["","","",""]]]
		self.tamGrupo=2
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
		
		"""
		cont=0
		while len(self.rep)>=cont+2:
			self.rep[cont:cont+1]=self.unir(self.rep[cont],self.rep[cont+1])
			cont=cont+1
			if (len(self.rep)==cont) or (len(self.rep)==cont+1):
				cont=0
				
		"""
		
		
		def reducir(self,x):
			aux=0
			repe=[]
			while aux+1<len(x):
				"""
				print x[aux]
				print x[aux+1]
				print "********************************"
				"""
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
		
