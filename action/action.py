#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import first
import metaData
import options
import data

class action():
	def __init__(self):
		
		self.conExten=[]
		self.sinExten=['']
		self.mayork=0L
		self.menork=0L
		self.excDir=''
		
		self.totalArchivos=[]
		self.archivosAbiertos=[]
		self.rep=[[['','','','']]]
                self.marcados=[]
		self.noMarcados=[]
		self.repetidos=[]
		self.encontrado=[]
		self.dirVacios=[]
		
		self.metaData= metaData.metaData()
		self.options= options.options()
		self.data= data.data(self.metaData)	
		
		
		
	#FILTROS		
	def AnadirConExten(self,exten):
		if len(self.metaData.levantar(exten))==1:
			self.conExten.append(self.metaData.levantar(exten)[0])
		
	def AnadirSinExten(self,exten):
		if len(self.metaData.levantar(exten))==1:
			if self.sinExten==['']:
				self.sinExten[0]=self.metaData.levantar(exten)[0]
			else:
				self.sinExten.append(self.metaData.levantar(exten)[0])
			
	def AnadirMayork(self,num):
		self.mayork=num
		
	def AnadirMenork(self,num):
		self.manork=num
		
	def AnadirExcDir(self,dir):
		self.excDir=dir
		
	def reiniciarFiltros(self):
		self.conExten=[]
		self.sinExten=['']
		self.mayork=0L
		self.menork=0L
		self.excDir=''



	#OPCIONES-1
	def RealizarBusqueda(self,direccion):
		self.totalArchivos=[]
		self.archivosAbiertos=[]
		self.rep=[[['','','','']]]
                self.marcados=[]
		self.noMarcados=[]
		self.repetidos=[]
		self.encontrado=[]
		self.dirVacios=[]

                self.first= first.first(direccion,self.conExten,self.sinExten,self.mayork,self.menork,self.excDir,self.metaData,self.totalArchivos,self.rep,self.noMarcados,self.repetidos,self.encontrado,self.archivosAbiertos,self.dirVacios)
		
		self.totalArchivos=self.first.getTotalArchivos()
		self.archivosAbiertos=self.first.getArchivosAbiertos()
		self.noMarcados=self.first.getNoMarcados()
		self.repetidos=self.first.getRepetidos()
		self.dirVacios=self.first.getDirVacios()
		
	def AdicionarTipos(self):
		self.metaData.adicionarTipos()
		
	def Traducir(self,idioma):
		import pickle

		traductor={}
		spanish=["Filtros","Por Carpeta..","Por Tipo..","Por Peso..","Realizar búsqueda en el directorio:","No incluir el directorio:","Solo buscar:","No incluir:","Solo incluir archivos con peso:","Mayor que:","Menor que:","Búsqueda","Realizar búsqueda              ","Adicionar tipos de archivos","Herramientas","Borrar Archivos Marcados      ","Borrar Archivos No Marcados ","Borrar Archivos Temporales    ","Borrar Directorios Vacíos         ","Cantidad de Grupos:","Cantidad Total:","Cantidad de Marcados:","Peso de los no Marcados:","Peso de los Marcados:","Peso Total:","Idioma","Tipografía","Ayuda","Contáctenos en Facebook","Acerca de...","Marcar todos","Marcar todos menos uno de cada grupo","Desmarcar todos","Marcar encontrados","DIRECTORIO","PESO","TIPO","MODIFICADO","Ordenar","Buscar","Tiempo de Búsqueda:","Añadir otro tipo de archivo","Excluir otro tipo de archivo"]
		english=["Filters","By Folder","By Type..","By Size..","Start search in directory:","Exclude the directory:","Search only:","Exclude:","Only include files with size:","Greater than:","Lesser than:","Search","Start search","Add file types","Tools"," Delete Marked Files        "," Delete Unmarked Files    ","Delete Temporary Files   ","Delete Empty Directories","Number of Groups:","Total Amount:","Number of Marked:","Unmarked size:","Marked size:","Total size:","Language","Typography","Help","Contact us on Facebook","About ...","Mark all","Mark all but one in each group","Unmark all","Mark found","DIRECTORY","SIZE","FILE TYPE","MODIFIED","Order","Search","Search Time","Add another file type","Exclude another file type"]		
		french=["Filtres","Par Dossier..","Par Type..","Par poids..","Effectuez une recherche de répertoire:","Exclure le répertoire:","Rechercher uniquement:","Exclure:","Inclure uniquement les fichiers dont le poids:","supérieur à:","Inférieur à:","Recherche","Sommaire Recherche           ","Ajouter des types de fichiers","Outils","Marqué Supprimer les fichiers","Supprimer les fichiers pas marqué","Supprimer les fichiers temporaires","supprimer les répertoires vides","Numéro du groupe:","Montant Total:","Quantité de étiquetée:","Poids non marqué:","Poids des Noté:","Poids total:","Langue","typographie","Aider","Contact sur Facebook","Sur...","Marquer tous les","Marquer tous sauf un dans chaque groupe","Décochez tous","Marquer trouvé","ANNUAIRE","POIDS","TYPE DE FICHIER","MODIFIÉ","Ordre","Recherche","Temps de recherche","Ajouter un autre type de fichier","Exclure autre type de fichier"]
		portuguese=["Filtros","Por Pasta..","Por Tipo..","Por Peso..","Realizar pesquisa de diretório:","Excluir o diretório:","Apenas busca:","Excluir:","Só incluir arquivos com peso:","Maior do que:","Menor que:","Pesquisa","Realizar pesquisa              ","Adicionar tipos de arquivo","Ferramentas","Apagar Arquivos Marcados       ","Apagar Arquivos Não Marcados","Excluir arquivos temporários   ","Remover diretórios vazios         ","Número do grupo:","Montante Total:","Quantidade de rotulados:","Peso sem rótulo:","Peso da rotulados:","Peso Total:","Língua","Tipografia","Ajudar","Contate-nos no Facebook","Sobre...","Marcar tudo","Marcar todos, mas um em cada grupo","Desmarque tudo","Marcar encontrado","DIRETÓRIO","PESO","TIPO DE ARQUIVO","MODIFICADO","Ordem","Pesquisa","Tempo de Pesquisa","Adicionar outro tipo de arquivo","Excluir outro tipo de arquivo"]
		german=["Filters","Nach Ordner..","Nach Typ..","Gewichts..","Führen Verzeichnissuche:","Ausschließen das Verzeichnis:","Nur suchen:","Ausschließen:","Nur Dateien mit Gewichts:","Größer als:","Weniger als:","Suche","Inhalt Suchen               ","Dateitypen hinzufügen","Werkzeuge","Partitur Dateien löschen            ","Dateien nicht löschen Partitur ","Temporäre Dateien löschen     ","Entfernen Sie leere Verzeichnisse","Anzahl der Gruppen:","Gesamtbetrag:","Anzahl der Tore:","Unbeschriftet Gewicht:","Gewicht der Partitur:","Gesamtgewicht:","Sprache","Typografie","Hilfe","Kontaktieren Sie uns auf Facebook","über...","Markieren Sie alle","Markieren Sie alle, aber einer in jeder Gruppe","Deaktivieren Sie alle","Lesezeichen gefunden","VERZEICHNIS","GEWICHT","DATEITYP","GEANDERT","Bestellen","Suche","Suche Zeit","In anderen Dateityp","Ausschließen andere Datei"]
		russian=["фильтры","по папкам..","по типу..","по весу..","Выполните поиск в каталоге:","Исключить каталог:","Поиск только:","исключать:","Только файлы только с весом:","Больше:","Менее:","поиск","Содержание Поиск     ","Добавить типы файлов","инструментарий","Состав удалять файлы       ","Удалить файлы не забил    ","Удаление временных файлов","Удалить пустых каталогов","Количество групп:","Общая сумма:","Количество Состав:","Немеченому вес:","Масса Состав:","общий вес:","язык","книгопечатание","Помогите","Контакты на Facebook","о...","Отметить все","Отметить все, но один в каждой группе","Снимите все","Марк нашел","СПРАВОЧНИК","ВЕС","ТИП ФАЙЛА","поправками","порядок","поиск","Поиск Время","Добавить файл другого типа","Исключить другой файл"]
		chinese=["过滤器","按文件夹..","按类型..","按重量..","执行目录搜索:","排除目录:","仅搜索:","排除:","仅包括具有重量文件:","大于:","小于:","搜索","内容搜索","添加文件类型","工具","进球删除文件","删除文件不进球","删除临时文件","删除空目录","组数:","总金额:","的进球数:","未标注的重量:","进球的重量:","整机重量:","语","活版印刷","帮助","联系我们在Facebook","关于...","标记全部","马克各组，但在所有","取消所有","马克发现","目录","重量","文件类型","改性","顺序","搜索","搜索时间","添加其他文件类型","排除其他文件"]
		japanese=["フィルター","フォルダごと..","タイプ別..","重さによる..","ディレクトリ検索を実行する:","ディレクトリを除外:","検索のみ:","除外する:","唯一の重みを持つファイルが含まれ:","越える:","以下:","検索","コンテンツ検索","ファイルタイプを追加","ツール","得点ファイルの削除","得点されていないファイルを削除します。","一時ファイルを削除します","空のディレクトリを削除","グループの数:","合計金額:","得点数:","ラベルのない重量:","得点の重み:","総重量:","言語","タイポグラフィ","助け","Facebook上でお問い合わせ","約...","マークのすべて","マークのすべてが、各グループの1","選択をすべて解除","マークが見つかりました","ディレクトリ","重量","ファイルタイプ","改正","オーダー","検索","検索時間","別のファイルタイプを追加","他のファイルを除外"]
		arabic=["مرشحات","بواسطة المجلد..","حسب نوع..","بواسطة الوزن..","إجراء البحث الدليل:","استبعاد الدليل:","بحث فقط:","منع:","وتشمل الملفات مع الوزن فقط:","أكبر من:","أقل من:","بحث","محتويات البحث","إضافة أنواع الملفات","أدوات","سجل حذف الملفات","حذف الملفات لم يسجل","حذف الملفات المؤقتة","إزالة الدلائل فارغة","عدد المجموعات:","إجمالي المبلغ:","وسجل عدد من:","غير المسماة الوزن:","وزن وسجل:","مجموع الوزن:","لغة","أسلوب الطباعة","مساعدة","الاتصال بنا في الفيسبوك","حول...","إختر الكل","العلامة لكن كل واحد في كل مجموعة","ازل جميع","وجدت علامة","الدليل","الوزن","الملف النوع","المحورة","النظام","بحث","البحث التوقيت","إضافة نوع ملف آخر","استبعاد الملفات الأخرى"]
		italian=["Filtri","Per Cartella..","Per Tipo..","Per Peso..","Esegui directory ricerca:","Escludere la directory:","Cerca solo:","Escludere:","Includere solo i file con peso:","Maggiore di:","Inferiore:","Ricerca","Indice Ricerca       ","Aggiungi tipi di file","Strumenti","Eliminare i file contrassegnati","Eliminare file non segnati       ","Eliminare i file temporanei     ","Rimuovere directory vuote     ","Numero di gruppi:","Importo Totale:","Numero di Votata:","Peso senza etichetta:","Peso del Votata:","Peso Totale:","Lingua","Tipografia","Aiuto","Contattaci su Facebook","Circa...","Seleziona tutto","Segna tutti ma uno in ogni gruppo","Deseleziona tutto","Seleziona trovato","DIRECTORY","PESO","TIPO DI FILE","MODIFICATO","Ordine","Ricerca","Tempo di ricerca","Aggiungi un altro tipo di file","Escludi un altro tipo di file"]
		
		if idioma=="spanish":
			for i in range(len(spanish)):
				traductor[i]=spanish[i]
		elif idioma=="english":
			for i in range(len(english)):
				traductor[i]=english[i]
		elif idioma=="french":
			for i in range(len(french)):
				traductor[i]=french[i]
		elif idioma=="portuguese":
			for i in range(len(portuguese)):
				traductor[i]=portuguese[i]
		elif idioma=="german":
			for i in range(len(german)):
				traductor[i]=german[i]
		elif idioma=="russian":
			for i in range(len(russian)):
				traductor[i]=russian[i]
		elif idioma=="chinese":
			for i in range(len(chinese)):
				traductor[i]=chinese[i]
		elif idioma=="japanese":
			for i in range(len(japanese)):
				traductor[i]=japanese[i]
		elif idioma=="arabic":
			for i in range(len(arabic)):
				traductor[i]=arabic[i]
		elif idioma=="italian":
			for i in range(len(italian)):
				traductor[i]=italian[i]
				
		language=open("language.sp","w")
		pickle.dump(traductor,language)
		language.close()
	
	
	
	#OPCIONES-2
	def Marcar(self,tupla):
		self.marcados,self.noMarcados=self.options.marcar(tupla,self.marcados,self.noMarcados)
	
	def Desmarcar(self,tupla):
		self.marcados,self.noMarcados=self.options.desmarcar(tupla,self.marcados,self.noMarcados)
		
	def MarcarTodosMenosUno(self):
		self.marcados,self.noMarcados=self.options.todosMenosUno(self.repetidos)
		
	def MarcarTodos(self):
		self.marcados,self.noMarcados=self.options.marcarTodos(self.repetidos)
		
	def DesmarcarTodos(self):
		self.marcados,self.noMarcados=self.options.desmarcarTodos(self.repetidos)
		
	def Encontrar(self,cadena):
		self.encontrado=self.first.encontrar(cadena)
	
	def MarcarEncontrados(self):
		self.marcados,self.noMarcados=self.options.marcarEncontrados(self.encontrado,self.marcados,self.noMarcados,self.repetidos)

	def Borrar(self,direcciones):
		errores=''

		for direccion in direcciones:    
			if os.path.isfile(direccion[0]):
				os.remove(direccion[0])
			else:
				errores=errores+direccion+"***"
		return errores
		
	def BorrarTemporales(self):
		exc=self.Borrar(self.archivosAbiertos)
		self.archivosAbiertos=[]
		if exc != '' :
			return 'ErrorArchivosNoBorrados: No se pudo borrar los siguientes archivos: '+exc
		return exc
	
	def BorrarDirectoriosVacios(self):
		import shutil
		errores=''
		for dir in self.dirVacios:
			try:
				shutil.rmtree(dir)
			except:
				errores=errores+dir+"***"
		self.dirVacios=[]
		if errores != '' :
			return 'ErrorArchivosNoBorrados: No se pudo borrar los siguientes archivos: '+errores
		return errores
		
	def BorrarMarcados(self):
		exc=self.Borrar(self.marcados)
		self.marcados=[]
		if exc != '' :
			return 'ErrorArchivosNoBorrados: No se pudo borrar los siguientes archivos: '+exc
		return exc
	
	def BorrarNoMarcados(self):
		exc=self.Borrar(self.noMarcados)
		self.noMarcados=[]
		if exc != '' :
			return 'ErrorArchivosNoBorrados: No se pudo borrar los siguientes archivos: '+exc
		return exc
	
	
		
	#DATOS
	def CantidadGrupos_Archivos(self):
		return self.first.cantidades()
		
	def PesoArchivosMarcados(self):
		return self.data.pesoArchivos(self.marcados)
		
	def PesoArchivosNoMarcados(self):
		return self.data.pesoArchivos(self.noMarcados)
		
	def PesoTotal(self):
		return self.data.pesoTotal(self.marcados,self.noMarcados)
		
	def PesoGrupo(self,grupo):
		return self.data.pesoGrupo(grupo)
		
	def FechaGrupo(self,grupo):
		return self.data.fechaGrupo(grupo)
		
	def TipoGrupo(self,grupo):
		return self.data.tipoGrupo(grupo)
		
	def CantidadArchivosMarcados(self):
		return self.data.cantMarcados(self.marcados)	
		
	def CantidadArchivosRevisados(self):
		return len(self.totalArchivos)
		
	def TiempoDemora(self):
		return self.first.getTiempoDemora()
		
		
	
	#OPCIONES-3
	def OrganizarPeso(self,orientacion):
		for i in range(len(self.repetidos)):
			pesoI=self.data.pesoEnByte(self.PesoGrupo(self.repetidos[i]))
			for j in range(len(self.repetidos)):
				pesoJ=self.data.pesoEnByte(self.PesoGrupo(self.repetidos[j]))
				if orientacion=="mayor":
					if pesoI>pesoJ:
						tem=self.repetidos[i]
						self.repetidos[i]=self.repetidos[j]
						self.repetidos[j]=tem
				elif orientacion=="menor":
					if pesoI<pesoJ:
						tem=self.repetidos[i]
						self.repetidos[i]=self.repetidos[j]
						self.repetidos[j]=tem
					
	def OrganizarFecha(self,orientacion):
		from dateutil import parser
		for i in range(len(self.repetidos)):
			fechaI=parser.parse(self.FechaGrupo(self.repetidos[i]))
			for j in range(len(self.repetidos)):
				fechaJ=parser.parse(self.FechaGrupo(self.repetidos[j]))
				if orientacion=="mayor":
					if fechaI>fechaJ:
						tem=self.repetidos[i]
						self.repetidos[i]=self.repetidos[j]
						self.repetidos[j]=tem
				elif orientacion=="menor":
					if fechaI<fechaJ:
						tem=self.repetidos[i]
						self.repetidos[i]=self.repetidos[j]
						self.repetidos[j]=tem
					
	def OrganizarTipo(self):
		for i in range(len(self.repetidos)):
			tipoI=self.TipoGrupo(self.repetidos[i])
			if (i==0):
				if (tipoI==self.TipoGrupo(self.repetidos[i+1])):
					continue
			elif (i==(len(self.repetidos)-1)):
				if (tipoI==self.TipoGrupo(self.repetidos[i-1])):
					continue
			else:
				if ((tipoI==self.TipoGrupo(self.repetidos[i-1])) or (tipoI==self.TipoGrupo(self.repetidos[i+1]))):
					continue
			for j in range(len(self.repetidos)):			
				tipoJ=self.TipoGrupo(self.repetidos[j])
				if( tipoI==tipoJ and i!=j):
					tem=self.repetidos[i]
					del self.repetidos[i]
					self.repetidos.insert(j-1,tem)
					break


	#ATRIBUTOS
	def getMarcados(self):			
		return self.marcados
	
	def getNoMarcados(self):
		return self.noMarcados
		
	def getRepetidos(self):
		return self.repetidos
		
	def getEncontrado(self):
		return self.encontrado

        def getTotalArchivos(self):
		return self.totalArchivos
		
	def getArchivosAbiertos(self):
		return self.archivosAbiertos
		
	def getDirVacios(self):
		return self.dirVacios
		
	def getMimeTypes(self,busqueda):
		return self.metaData.levantar(busqueda)
		