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
		self.direccion=""
		
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
		
		self.posR=[]
		self.temR=[]
		
		
		
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
		self.menork=num
		
	def AnadirExcDir(self,dir):
		self.excDir=dir
		
	def reiniciarFiltros(self):
		self.conExten=[]
		self.sinExten=['']
		self.mayork=0L
		self.menork=0L
		self.excDir=''
		
	def AnadirDir(self,direccion):
		self.direccion=direccion


	#OPCIONES-1
	def RealizarBusqueda(self):
		self.totalArchivos=[]
		self.archivosAbiertos=[]
		self.rep=[[['','','','']]]
                self.marcados=[]
		self.noMarcados=[]
		self.repetidos=[]
		self.encontrado=[]
		self.dirVacios=[]
		
		if self.conExten!=[]:
			self.sinExten=['']

                self.first= first.first(self.direccion,self.conExten,self.sinExten,self.mayork,self.menork,self.excDir,self.metaData,self.totalArchivos,self.rep,self.noMarcados,self.repetidos,self.encontrado,self.archivosAbiertos,self.dirVacios)
		
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
		spanish=["Filtros","Por Carpeta..","Por Tipo..","Por Peso..","Realizar búsqueda en el directorio:","No incluir el directorio:","Solo buscar:","No incluir:","Solo incluir archivos con peso:","Mayor que:","Menor que:","Búsqueda","Realizar búsqueda              ","Adicionar tipos de archivos","Herramientas","Borrar Archivos Marcados      ","Borrar Archivos No Marcados ","Borrar Archivos Temporales    ","Borrar Directorios Vacíos         ","Cantidad de Grupos:","Cantidad Total:","Cantidad de Marcados:","Peso de los no Marcados:","Peso de los Marcados:","Peso Total:","Idioma","Tipografía","Ayuda","Contáctenos en Facebook","Acerca de...","Marcar todos","Marcar todos menos uno de cada grupo","Desmarcar todos","Marcar encontrados","DIRECTORIO","PESO","TIPO","MODIFICADO","Ordenar","Buscar","Tiempo de Búsqueda:","Añadir otro tipo de archivo","Excluir otro tipo de archivo","Archivos Revisados:","Directorios Vacíos:","Temporales:","Información de licencia","Descripción detallada","Contácte con los desarrolladores","gana espacio en menos tiempo","es una herramienta que todos necesitamos, diseñada para las manos del usuario más inexperto, encuentre los ficheros repetidos dentro de sus directorios con más información, elimínelos, no son necesarios....solo ocupan nuestro espacio","Desarrollado por","Universidad de las Ciencias Informáticas","Error","Limpiar Selección","Se han encontrado %s coincidencias","Operación terminada","No debe haber tildes en la dirección","Cancelar"]
		english=["Filters","By Folder","By Type..","By Size..","Start search in directory:","Exclude the directory:","Search only:","Exclude:","Only include files with size:","Greater than:","Lesser than:","Search","Start search","Add file types","Tools"," Delete Marked Files        "," Delete Unmarked Files    ","Delete Temporary Files   ","Delete Empty Directories","Number of Groups:","Total Amount:","Number of Marked:","Unmarked size:","Marked size:","Total size:","Language","Typography","Help","Contact us on Facebook","About ...","Mark all","Mark all but one in each group","Unmark all","Mark found","DIRECTORY","SIZE","FILE TYPE","MODIFIED","Order","Search","Search Time","Add another file type","Exclude another file type","Revised files:","Empty Directories:","Temporary:","License Information","Detailed description","Contact the developers","gaining ground in less time","is a tool we all need, designed for the hands of the most inexperienced user will find the duplicated files within their directories with more information, delete them, they are not necessary .... only occupy our space","Developed by","University of Informatics Sciences","Error","Clear Selection","Found %s matches","Operation Completed","There should be no accent marks at the address","Cancel"]
		french=["Filtres","Par Dossier..","Par Type..","Par poids..","Effectuez une recherche de répertoire:","Exclure le répertoire:","Rechercher uniquement:","Exclure:","Inclure uniquement les fichiers dont le poids:","supérieur à:","Inférieur à:","Recherche","Sommaire Recherche           ","Ajouter des types de fichiers","Outils","Marqué Supprimer les fichiers","Supprimer les fichiers pas marqué","Supprimer les fichiers temporaires","supprimer les répertoires vides","Numéro du groupe:","Montant Total:","Quantité de étiquetée:","Poids non marqué:","Poids des Noté:","Poids total:","Langue","typographie","Aider","Contact sur Facebook","Sur...","Marquer tous les","Marquer tous sauf un dans chaque groupe","Décochez tous","Marquer trouvé","ANNUAIRE","POIDS","TYPE DE FICHIER","MODIFIÉ","Ordre","Recherche","Temps de recherche","Ajouter un autre type de fichier","Exclure autre type de fichier","Fichiers révisée:","Empty Directories:","Temporaire:","Informations sur la licence","Description Détaillée","Contactez les développeurs","gagne du terrain en moins de temps","est un outil que nous devons tous, conçu pour les mains de l'utilisateur le plus inexpérimenté trouver les fichiers dupliqués au sein de leurs répertoires avec plus d'informations, les supprimer, ils ne sont pas nécessaires .... seulement occuper notre espace","Propulsé par","Université des sciences informatiques","Erreur","Effacer la sélection","Matchs de% Trouvé","Opération terminée","Il ne doit pas avoir  tildes dans la direction","Annuler"]
		portuguese=["Filtros","Por Pasta..","Por Tipo..","Por Peso..","Realizar pesquisa de diretório:","Excluir o diretório:","Apenas busca:","Excluir:","Só incluir arquivos com peso:","Maior do que:","Menor que:","Pesquisa","Realizar pesquisa              ","Adicionar tipos de arquivo","Ferramentas","Apagar Arquivos Marcados       ","Apagar Arquivos Não Marcados","Excluir arquivos temporários   ","Remover diretórios vazios         ","Número do grupo:","Montante Total:","Quantidade de rotulados:","Peso sem rótulo:","Peso da rotulados:","Peso Total:","Língua","Tipografia","Ajudar","Contate-nos no Facebook","Sobre...","Marcar tudo","Marcar todos, mas um em cada grupo","Desmarque tudo","Marcar encontrado","DIRETÓRIO","PESO","TIPO DE ARQUIVO","MODIFICADO","Ordem","Pesquisa","Tempo de Pesquisa","Adicionar outro tipo de arquivo","Excluir outro tipo de arquivo","Arquivos Revisado:","Diretórios vazios:","Temporário:","Informações sobre a licença","Descrição detalhada","Contato com os desenvolvedores","ganhando terreno em menos tempo","é uma ferramenta que todos nós precisamos, projetado para as mãos do usuário mais inexperiente vai encontrar os arquivos duplicados dentro de seus diretórios com maiores informações, excluí-los, eles não são necessários .... só ocupar o nosso espaço","Desenvolvido por","Universidade das Ciências Informáticas","Erro","Limpar Seleção","Encontrados %s jogos","Operação concluída","Não deve haver tils na direção","Cancelar"]
		german=["Filters","Nach Ordner..","Nach Typ..","Gewichts..","Führen Verzeichnissuche:","Ausschließen das Verzeichnis:","Nur suchen:","Ausschließen:","Nur Dateien mit Gewichts:","Größer als:","Weniger als:","Suche","Inhalt Suchen               ","Dateitypen hinzufügen","Werkzeuge","Partitur Dateien löschen            ","Dateien nicht löschen Partitur ","Temporäre Dateien löschen     ","Entfernen Sie leere Verzeichnisse","Anzahl der Gruppen:","Gesamtbetrag:","Anzahl der Tore:","Unbeschriftet Gewicht:","Gewicht der Partitur:","Gesamtgewicht:","Sprache","Typografie","Hilfe","Kontaktieren Sie uns auf Facebook","über...","Markieren Sie alle","Markieren Sie alle, aber einer in jeder Gruppe","Deaktivieren Sie alle","Lesezeichen gefunden","VERZEICHNIS","GEWICHT","DATEITYP","GEANDERT","Bestellen","Suche","Suche Zeit","In anderen Dateityp","Ausschließen andere Datei","Überarbeitete Dateien:","Leere Verzeichnisse:","Vorübergehend:","Lizenzinformationen","Detaillierte Beschreibung","Kontakt zum Entwickler","vormarsch in weniger Zeit","ist ein Werkzeug, das wir alle brauchen, für die Hände der unerfahrene Benutzer konzipiert werden die duplizierten Dateien in ihren Verzeichnissen mit mehr Informationen finden, löschen Sie sie, sie sind nicht notwendig .... nur unseren Platz einnehmen","Präsentiert von","Universität für Informationswissenschaften","Fehler","Auswahl löschen","Gefunden %s Treffer","Vorgang abgeschlossen","Es sollte keine Tilden in der Richtung ","Stornieren"]
		russian=["фильтры","по папкам..","по типу..","по весу..","Выполните поиск в каталоге:","Исключить каталог:","Поиск только:","исключать:","Только файлы только с весом:","Больше:","Менее:","поиск","Содержание Поиск     ","Добавить типы файлов","инструментарий","Состав удалять файлы       ","Удалить файлы не забил    ","Удаление временных файлов","Удалить пустых каталогов","Количество групп:","Общая сумма:","Количество Состав:","Немеченому вес:","Масса Состав:","общий вес:","язык","книгопечатание","Помогите","Контакты на Facebook","о...","Отметить все","Отметить все, но один в каждой группе","Снимите все","Марк нашел","СПРАВОЧНИК","ВЕС","ТИП ФАЙЛА","поправками","порядок","поиск","Поиск Время","Добавить файл другого типа","Исключить другой файл","Пересмотренный Файлы:","пустые каталоги:","временный:","Информация о лицензии","подробное описание","Связаться с разработчиками","набирает силу за меньшее время","является инструментом, мы все должны, предназначен для руки самого неопытного пользователя найдете дублирующиеся файлы в своих каталогах с большим количеством информации, удалять их, они не нужны .... только занимают наше пространство","Создано","Университет информационных наук","Ошибка","Очистить выбор","Найденных %s","Операция выполнена","Там не должно быть никаких тильды в направлении","отменить"]
		chinese=["过滤器","按文件夹..","按类型..","按重量..","执行目录搜索:","排除目录:","仅搜索:","排除:","仅包括具有重量文件:","大于:","小于:","搜索","内容搜索","添加文件类型","工具","进球删除文件","删除文件不进球","删除临时文件","删除空目录","组数:","总金额:","的进球数:","未标注的重量:","进球的重量:","整机重量:","语","活版印刷","帮助","联系我们在Facebook","关于...","标记全部","马克各组，但在所有","取消所有","马克发现","目录","重量","文件类型","改性","顺序","搜索","搜索时间","添加其他文件类型","排除其他文件","经修订的文件:","空目录:","临时:","许可信息","详细说明","联系开发者","在较短的时间抬头","是我们都需要一个工具，专为最没有经验的用户手中会发现他们的目录中重复的文件更多的信息，删除它们，它们是没有必要的....只占据我们的空间","技术支持","信息科学大学","错误","清除选择","发现 ％s 的比赛","操作完成","應該有在方向上沒有波浪號","取消"]
		japanese=["フィルター","フォルダごと..","タイプ別..","重さによる..","ディレクトリ検索を実行する:","ディレクトリを除外:","検索のみ:","除外する:","唯一の重みを持つファイルが含まれ:","越える:","以下:","検索","コンテンツ検索","ファイルタイプを追加","ツール","得点ファイルの削除","得点されていないファイルを削除します。","一時ファイルを削除します","空のディレクトリを削除","グループの数:","合計金額:","得点数:","ラベルのない重量:","得点の重み:","総重量:","言語","タイポグラフィ","助け","Facebook上でお問い合わせ","約...","マークのすべて","マークのすべてが、各グループの1","選択をすべて解除","マークが見つかりました","ディレクトリ","重量","ファイルタイプ","改正","オーダー","検索","検索時間","別のファイルタイプを追加","他のファイルを除外","改訂されたファイル:","空のディレクトリ:","一時的な:","ライセンス情報","詳細な説明","開発者に連絡してください","短い時間で地面を獲得","我々が最も不慣れなユーザの手のために設計されたすべての必要性は、より多くの情報と、そのディレクトリ内で重複ファイルを見つけるツールですが、それらを削除し、それは必要ありません....だけ私達のスペースを占有する","アトス","情報科学大学","エラー","選択をクリア","見つかっ％sの試合","操作完了","方向にはチルダがあってはならない","キャンセル"]
		arabic=["مرشحات","بواسطة المجلد..","حسب نوع..","بواسطة الوزن..","إجراء البحث الدليل:","استبعاد الدليل:","بحث فقط:","منع:","وتشمل الملفات مع الوزن فقط:","أكبر من:","أقل من:","بحث","محتويات البحث","إضافة أنواع الملفات","أدوات","سجل حذف الملفات","حذف الملفات لم يسجل","حذف الملفات المؤقتة","إزالة الدلائل فارغة","عدد المجموعات:","إجمالي المبلغ:","وسجل عدد من:","غير المسماة الوزن:","وزن وسجل:","مجموع الوزن:","لغة","أسلوب الطباعة","مساعدة","الاتصال بنا في الفيسبوك","حول...","إختر الكل","العلامة لكن كل واحد في كل مجموعة","ازل جميع","وجدت علامة","الدليل","الوزن","الملف النوع","المحورة","النظام","بحث","البحث التوقيت","إضافة نوع ملف آخر","استبعاد الملفات الأخرى","ملفات المنقحة:","الدلائل فارغة:","مؤقت:","معلومات الترخيص","وصف تفصيلي","الاتصال المطورين","تكتسب الأرض في وقت أقل","هو أداة سوف نحتاج جميعا، والمصممة ليد المستخدم الأكثر خبرة العثور على الملفات المكررة في الدلائل الخاصة بهم مع مزيد من المعلومات، حذفها، فهي ليست ضرورية فقط .... تحتل فضائنا","مدعوم من","جامعة العلوم معلومات","خطأ","اختيار واضحة","مباريات٪ جدت ق","اكتمال عملية","There should be no accent marks at the address","إلغاء"]
		italian=["Filtri","Per Cartella..","Per Tipo..","Per Peso..","Esegui directory ricerca:","Escludere la directory:","Cerca solo:","Escludere:","Includere solo i file con peso:","Maggiore di:","Inferiore:","Ricerca","Indice Ricerca       ","Aggiungi tipi di file","Strumenti","Eliminare i file contrassegnati","Eliminare file non segnati       ","Eliminare i file temporanei     ","Rimuovere directory vuote     ","Numero di gruppi:","Importo Totale:","Numero di Votata:","Peso senza etichetta:","Peso del Votata:","Peso Totale:","Lingua","Tipografia","Aiuto","Contattaci su Facebook","Circa...","Seleziona tutto","Segna tutti ma uno in ogni gruppo","Deseleziona tutto","Seleziona trovato","DIRECTORY","PESO","TIPO DI FILE","MODIFICATO","Ordine","Ricerca","Tempo di ricerca","Aggiungi un altro tipo di file","Escludi un altro tipo di file","Files rivistos:","Elenchi vuote:","Temporaneo:","Informazioni sulla licenza","Descrizione dettagliata","Contattare gli sviluppatori","guadagnando terreno in meno tempo","è uno strumento di cui abbiamo tutti bisogno, studiato per le mani l'utente più inesperto sarà trovare i file duplicati all'interno delle loro cartelle con più informazioni, cancellarli, non sono necessari .... solo occupano il nostro spazio","sviluppato da","Università degli Studi di Scienze Informatiche","Errore","Annulla selezione","Partite %s Trovato","Operazione completata","Non ci dovrebbero essere tilde nella direzione","Cancellare"]
		
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
				try:
					os.remove(direccion[0])
				except:errores=errores+str(direccion[0])+"***"
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
			return 'ErrorDirectoriosNoBorrados: No se pudo borrar los siguientes directorios: '+errores
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
					
	

	def tipoI(self):
		self.temR.append(self.repetidos[0])
		tipo=self.TipoGrupo(self.repetidos[0])
		del self.repetidos[0]
		for i in range(len(self.repetidos)):
			if self.TipoGrupo(self.repetidos[i])==tipo:
				self.temR.append(self.repetidos[i])
				self.posR.insert(0,i)
		for i in self.posR:
			del self.repetidos[i]
		self.posR=[]
		
	def OrganizarTipo(self):
		self.posR=[]
		self.temR=[]
		while len(self.repetidos)>0:
			self.tipoI()
		self.repetidos=self.temR


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
		