#OnlyOne is an application to remove duplicated files within a specified directory
#Copyright (C) 2014 Carlos Manuel Ferr�s Hern�ndez
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


def Language():
	import pickle

	fichero=open("language.sp","r")
	language=pickle.load(fichero)
	fichero.close()
	return language

