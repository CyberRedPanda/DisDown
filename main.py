# create simple txt file with Discord invites first called discord_links.txt

import requests 

headers = {
	'Accept': 'application/json',
}

def checker():
	with open("discord_links.txt") as f:
		for line in f:
			line = "https://discordapp.com/api/invite" + str(line.strip())
			response = requests.get(line, headers = headers)
			if response.status_code == 200:
				print("https://discord.gg" + str(line) + " is a valid invite link")
			elif response.status_code == 429:
				print(response.headers)
				break
			else:
				print(str(line) + " returned a " + str(response.status_code))


if __name__=="__main__":
	checker()
