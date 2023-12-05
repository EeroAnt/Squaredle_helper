from os import path, remove
from urllib.request import urlopen
from re import sub

def get_raw_list():
	if path.exists("list.txt"):
		remove("list.txt")
	raw_content = urlopen("https://raw.githubusercontent.com/scrabblewords/scrabblewords/main/words/North-American/NWL2020.txt").read()
	allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \n"
	content = "".join([chr(c) for c in raw_content if chr(c) in allowed_chars])
	content_with_no_spaces=sub("\s","\n",content)
	content = list(set(content_with_no_spaces.split("\n")))
	with open("list.txt", "w") as f:
		for i in content:
			if len(i) > 3:
				f.write(i+"\n")

get_raw_list()