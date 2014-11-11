#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#~ Copyright (C) 2014 Carlos Manuel Ferras Hernandez
#~ This file is part of LF02_package.

#~ LF02_package is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ LF02_package is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with LF02_package.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtCore
import os
#os.chdir('/usr/share/onlyone')

class Assistant:
	def __init__(self):
		self.proc= QtCore.QProcess()
	
	def startAssistant(self):
		if not self.proc:
			self.proc=QtCore.QProcess()
		if (self.proc.state() != QtCore.QProcess.Running):
			app ="assistant ";
			args="-collectionFile documentacion/onlyone.qhc -enableRemoteControl"
			self.proc.startDetached(str(app)+str(args))
		return True
		









		
		