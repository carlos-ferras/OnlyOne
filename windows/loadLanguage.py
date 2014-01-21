def Language():
	import pickle

	fichero=open("language.sp","r")
	language=pickle.load(fichero)
	fichero.close()
	return language

