##====================================================================##
##                                                                    ##
## SOFTWARE: Whois python.                                            ##
## AUTHOR: Charles Dantas (chameleon)                                 ##
## VERSION: 1.0                                                       ##
## CREATION DATE: 29/06/2022                                          ##
##                                                                    ##
##====================================================================##

#Important! Download pip install python-whois

import sys
import whois

def __init__():

	try:

		domain = input("Domain: ")
		consult = whois.whois(domain)
		print(consult.email)
		print(consult.text)

	except Exception as error:

		print(f'Error:{error}') 

__init__()

