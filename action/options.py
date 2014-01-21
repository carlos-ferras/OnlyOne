#!/usr/bin/env python
# -*- coding: utf-8 -*-

class options():
	
	#noMarcados,repetidos,encontrado se reciven luego de ser procesados por la clase first
	def __init__(self):
		pass
		
	def marcar(self,tupla,marcados,noMarcados):
		"""marca un archivo"""
		pos=0
		for archivo in noMarcados:
			if(archivo==tupla):
				marcados.append(tupla)
				del noMarcados[pos]
				break
			pos=pos+1
                return marcados,noMarcados
			
	def desmarcar(self,tupla,marcados,noMarcados):
		"""desmarca un archivo"""
		pos=0
		for archivo in marcados:
			if(archivo==tupla):
				noMarcados.append(tupla)
				del marcados[pos]
				break
			pos=pos+1
                return marcados,noMarcados
			
	def todosMenosUno(self,repetidos):
		"""marca todos los archivos de todos los grupos menos el primero de cada grupo"""
		noMarcados=[]
		marcados=[]
		for grupo in repetidos:
			cantidad=len(grupo)
			noMarcados.append(grupo[0])        
			for i in range(1,cantidad):
				marcados.append(grupo[i])
                return marcados,noMarcados
				
	def marcarTodos(self,repetidos):
		"""marca todos los archivos de todos los grupos"""
		noMarcados=[]
		marcados=[]
		for grupo in repetidos:
			for tupla in grupo:
				marcados.append(tupla)
                return marcados,noMarcados
				
	def desmarcarTodos(self,repetidos):
		"""desmarca todos los archivos de todos los grupos"""
		marcados=[]
		noMarcados=[]
		for grupo in repetidos:
			for tupla in grupo:
				noMarcados.append(tupla)
		return marcados,noMarcados
				
	def marcarEncontrados(self,encontrado,marcados,noMarcados,repetidos):
		"""Marca todos los archivos encontrados luego de realizar una busqueda con el metodo encontrar()"""
		for tupla in encontrado:
			self.marcar(tupla,marcados,noMarcados)
                return marcados,noMarcados
				

				
				
				
				
				
				
				
				
				
				
				