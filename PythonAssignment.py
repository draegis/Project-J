# Allting som står efter "#" symbolen är kommentarer
# Ta bort det innan det lämnas in, eller alternativt skriv om kommentarerna så dom representerar er bättre
# Och om ni tycker programmet är för förenklat så går det att göra på bättre sätt jag gjorde det på det sätt jag ansåg enklast att förstå
# I pythons print funktion så separerar man test från variablar med ett komma tecken till exempel "print("Här är",minvariabel,"som exempel")"
# Lycka till! / Rasmus
manadsnummerfraga = input('Skriv in ett manadsnummer: ') #Här skapar jag en variabel och ber användaren att skriva in ett månadsnummer och tilldelar det till variabeln
manadsnummerfraga = int(manadsnummerfraga) #Här omvandlar jag det inmatade värdet från string till int för att kunna jämföra det senare i programmet med logiska operatorer
if manadsnummerfraga >= 1 and manadsnummerfraga <= 12: #Här kollar jag om värdet som vi fick är emellan 1-12
	dagsnummerfraga = input('Skriv in ett dagnummer inom manaden: ') #Här skapar jag en variabel och ber användaren att skriva in ett dagnummer och tilldelar det till variabeln
	dagsnummerfraga = int(dagsnummerfraga) #Här omvandlas den som vi gjorde tidigare för månads variabeln så vi kan jämföra med logiska operatorer
	if manadsnummerfraga == 1: #Här kollar vi om månadsnumret är 1
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 2: #Här kollar vi om månadsnumret är 2
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 28: #Här kollar vi om dagsnumret är emellan 1-28
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-28 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 3: #Här kollar vi om månadsnumret är 3
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 4: #Här kollar vi om månadsnumret är 4
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #Här kollar vi om dagsnumret är emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 5: #Här kollar vi om månadsnumret är 5
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 6: #Här kollar vi om månadsnumret är 6
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #Här kollar vi om dagsnumret är emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 7: #Här kollar vi om månadsnumret är 7
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 8: #Här kollar vi om månadsnumret är 8
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 9: #Här kollar vi om månadsnumret är 9
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #Här kollar vi om dagsnumret är emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 10: #Här kollar vi om månadsnumret är 10
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 11: #Här kollar vi om månadsnumret är 11
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 30: #Här kollar vi om dagsnumret är emellan 1-30
			print("Korrekt datum!")
		else: #Om dagsnumret ej ligger mellan 1-30 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
	elif manadsnummerfraga == 12: #Här kollar vi om månadsnumret är 12
		if dagsnummerfraga >= 1 and dagsnummerfraga <= 31: #Här kollar vi om dagsnumret är emellan 1-31
			print("Korrekt datum!")
		else: ##Om dagsnumret ej ligger mellan 1-31 skrivs detta ut.
			print("Manad", manadsnummerfraga ,"har ingen dag", dagsnummerfraga)
else: #Detta skrivs ut om värdet inte är emellan 1-12
	print("Manad", manadsnummerfraga ,"finns ej.")