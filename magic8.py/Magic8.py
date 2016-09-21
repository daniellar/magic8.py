# def return to landing
# def yes / no 

import random
replies = ('It is certain', "It is decidedly so",
"Without a doubt",
"Yes, definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful")


def main():
	query = request_input()

def request_input():
	while True:
		query = raw_input("Ask me your query... ").lower()
		choice = raw_input("Are you sure you seek this truth? 'Yes' or 'No'.").lower()
		if choice.lower() == 'yes':
			answer = export_query()
			print answer
		else:
			print "May your journey reveal the answers you seek." 
			return query

def export_query():
	export = random.choice(replies)
	return export

 

if __name__ == '__main__':
	main()