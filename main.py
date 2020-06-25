# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
  return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico_K8(nomFichier, sep):
  print("Creation d'un dictionnaire a partir du fichier {} avec '80' entrees".format(nomFichier))
  f = open(nomFichier, "r")
  dictionnaire = {}
  for i in range(0,80):
    lines = f.readline().split(sep)
    dictionnaire[lines[0]] = lines[1].replace("\n","")
  f.close()
  return dictionnaire
###### exercice 02
def verifUrl_A4(url):
  index = 0
  test = 0
  while index < len(url):
    if url[index] == ".":
      test = test + 1
    index = index + 1
  if test > 1:
    print("url mal formee")
    verif = False
    return verif
  x = url.split(".")

  if len(x[1]) != 3:
    print("url mal formee") 
    verif = False
  else:
    verif = True
  return verif

###### exercice 03


###### exercice 04


###### exercice 05
    

###### exercice 06


# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))

	###### exercice 01
  print("exercice 01 #######################")
  resolDns = makeDico_K8("dns.txt",",")
  print(resolDns)
	###### exercice 02
  print("exercice 02 #######################")
  result = verifUrl_A4("toto.com")
  print(result)

	###### exercice 03
  print("exercice 03 #######################")


	###### exercice 04
  print("exercice 04 #######################")


	###### exercice 05
  print("exercice 05 #######################")


	###### exercice 06
  print("exercice 06 #######################")

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")


	###### exercice 08
  print("exercice 08 #######################")


	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()