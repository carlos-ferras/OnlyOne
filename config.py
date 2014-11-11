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

import commands
import os
#os.chdir('/usr/share/onlyone')

class config:
	
	def __init__(self):
		try:
			a=str(commands.getoutput('$HOME'))
			b=a.split('/')
			del b[0]
			c=b[-1].split()
			del b[-1]
			if len(c)>1:
				d=c[0].split(':')
				e=d[0]
			else:
				e=c[0]
			self.userRoot=''
			for i in b:
				self.userRoot+='/'+i
			self.userRoot+='/'+e
			self.dir=self.userRoot+'/.onlyone.conf'
		except:
			self.dir='onlyone.conf'
		
	def load(self):		
		if os.path.exists(self.dir):
			file=open(self.dir,'r')
			try:
				config=['',1,'es']
				while True:
					line =file.readline()
					if not line:
						break
					if not line.find('File Location '):
						config[0] =str(line.split("[")[1].split("]")[0])
					elif not line.find('Opacity '):
						try:
							config[1]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Lang '):
						config[2] =str(line.split("[")[1].split("]")[0])
				return config
			except:
				return False
			file.close()
		return False
			
	def save(self,fileLocation,opacity,lang):
		file=open(self.dir,'w+').close()
		file=open(self.dir,'w+')
		try:
			location=fileLocation.toUtf8().data()
		except:
			location=fileLocation
		file.write("File Location ["+str(location)+"]\n"+"Opacity ["+str(opacity)+"]\n"+"Lang ["+str(lang)+"]\n")
		file.close()
		return True
		
		
		
		
		
		