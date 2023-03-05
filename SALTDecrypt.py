#!/usr/bin/python3.9

import os #"clear"
import crypt #Pour crypter (SALT)
from termcolor import colored

prompt="_-SALTDecrypt-_/~ "

#Déchiffre
def crackMDP(mdpsalt, fichier_mdp):
	sel = mdpsalt[0:2] #Le sel est la première et deuxième lettre avec la lib crypt

	try:
		fichier = open(fichier_mdp, "r")
	except:
		print(colored("[ERREUR] Le fichier "+fichier_mdp+" n'existe pas!!\n", "red"))
		quit()


	for mdp in fichier.readlines():
		mdp = mdp.strip(" ").strip("\n")
		print(colored(prompt+"Essai du mot de passe "+mdp+" (SEL:"+sel+")...", "yellow"))
		crypte = crypt.crypt(mdp, sel)

		if crypte == mdpsalt:
			print(colored(prompt+"MOT DE PASSE TROUVE: "+mdp+" !!\n", "green"))
			quit()

	return

def main():
	os.system("clear")
	print(colored(banner, "blue"))
	print(colored(title, "yellow"))
	nom_fichier_mdp = input(prompt+"Entrez le fichier contenant des mots de passes en clair: ")

	nom_fichier_mdpsalt = input(prompt+"Entrez le fichier contenant des mots de passes chiffré avec du SEL: ")

	try:
		fichier_mdpsalt = open(nom_fichier_mdpsalt, "r")
	except:
		print(colored("[ERREUR] Le fichier "+nom_fichier_mdpsalt+" n'existe pas!!\n", "red"))
		quit()


	for mdpsalt in fichier_mdpsalt.readlines():
		mdpsalt = mdpsalt.strip(" ").strip("\n")
		crackMDP(mdpsalt, nom_fichier_mdp)

	print(colored(prompt+"Mot de passe non trouvé...", "red"))


banner = ("   _____ ___    __  __________                             __\n"+
"  / ___//   |  / / /_  __/ __ \___  ____________  ______  / /_\n"+
"  \__ \/ /| | / /   / / / / / / _ \/ ___/ ___/ / / / __ \/ __/\n"+
" ___/ / ___ |/ /___/ / / /_/ /  __/ /__/ /  / /_/ / /_/ / /_\n"+
"/____/_/  |_/_____/_/ /_____/\___/\___/_/   \__, / .___/\__/\n"+
"                                          /____/_/\n")
title = "Decrypt passwords crypted with CRYPT (SALT) by b64-Sm9yZGFuIExBSVJFUw\n"

main()
