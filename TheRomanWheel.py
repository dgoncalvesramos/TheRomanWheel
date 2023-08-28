import socket
import base64
import sys 
import re
import codecs

#Extrait la chaine de caractère encodée en ROT 13 à l'aide d'une regex puis retourne sa valeur décodée
def extract_string_and_decode_it(text):
	pattern = re.compile(r"my string is '([^']+)'")
	match = pattern.search(text)
	if match:
		encoded_string = match.group(1)
	else:
		sys.exit("Encoded string was not found")
	return codecs.decode(encoded_string, 'rot_13')

	
	
# Paramètres
HOST = 'challenge01.root-me.org'  # Hostname
PORT = 52021        			  # Port du serveur

# Créer le socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Reception de la réponse
response = s.recv(1000).decode()
print(response)

#Envoie du message
message = extract_string_and_decode_it(response) + '\n'
s.send(message.encode())

#Réception du flag
response = s.recv(1000).decode()
print(response)
