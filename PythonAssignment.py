# Allting som st�r efter "#" symbolen �r kommentarer
# Ta bort det innan det l�mnas in, eller alternativt skriv om kommentarerna s� dom representerar er b�ttre
# Och om ni tycker programmet �r f�r f�renklat s� g�r det att g�ra p� b�ttre s�tt jag gjorde det p� det s�tt jag ans�g enklast att f�rst�
# I pythons print funktion s� separerar man test fr�n variablar med ett komma tecken till exempel "print("H�r �r",minvariabel,"som exempel")"
# Lycka till! / Rasmus
manadsnummerfraga = input('Skriv in ett manadsnummer: ') #H�r skapar jag en variabel och ber anv�ndaren att skriva in ett m�nadsnummer och tilldelar det till variabeln
manadsnummerfraga = int(manadsnummerfraga) #H�r omvandlar jag det inmatade v�rdet fr�n string till int f�r att kunna j�mf�ra det senare i programmet med logiska operatorer
if manadsnummerfraga >= 1 and manadsnummerfraga <= 12: #H�r kollar jag om v�rdet som vi fick �r emellan 1-12
	dagsnummerfraga = input('Skriv in ett dagnummer inom manaden: ') #H�r skapar jag en variabel och ber anv�ndaren att skriva in ett dagnummer och tilldelar det till variabeln
	dagsnummerfraga = int(dagsnummerfraga) #H�r omvandlas den som vi gjorde tidigare f�r m�nads variabeln s� vi kan j�mf�ra med logiska operatorer
	if manadsnummerfraga == 1: #H�r kollar vi om m�nadsnumret �r 1
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 2: #H�r kollar vi om m�nadsnumret �r 2
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 28: #H�r kollar vi om dagsnumret �r emellan 1-28
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-28 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 3: #H�r kollar vi om m�nadsnumret �r 3
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 4: #H�r kollar vi om m�nadsnumret �r 4
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #H�r kollar vi om dagsnumret �r emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 5: #H�r kollar vi om m�nadsnumret �r 5
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 6: #H�r kollar vi om m�nadsnumret �r 6
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #H�r kollar vi om dagsnumret �r emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 7: #H�r kollar vi om m�nadsnumret �r 7
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 8: #H�r kollar vi om m�nadsnumret �r 8
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 9: #H�r kollar vi om m�nadsnumret �r 9
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #H�r kollar vi om dagsnumret �r emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 10: #H�r kollar vi om m�nadsnumret �r 10
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 11: #H�r kollar vi om m�nadsnumret �r 11
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #H�r kollar vi om dagsnumret �r emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 12: #H�r kollar vi om m�nadsnumret �r 12
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #H�r kollar vi om dagsnumret �r emellan 1-31
			print("Korrekt datum!")
		else: ##Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
else: #Detta skrivs ut om v�rdet inte �r emellan 1-12
	print("Manad", manadsnummerfraga ,"finns ej.")