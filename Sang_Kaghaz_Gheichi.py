import random

Choices = ['sang','kaghaz', 'gheichi']
personPoints = 0
pcPoints = 0

while True:
	pcChoice = random.choice(Choices)
	personChoice = input(f'''\nWelcome To Sang Kaghaz Gheichi Game!
Please Choose One:
Your Points: {personPoints}
PC Points: {pcPoints}
	
[Sang]
[Kaghaz]
[Gheichi]

Your Choice: ''')
	if personChoice.lower() in Choices:
		if personChoice.lower() == pcChoice:
			print('\n[Har Doye Shoma Yek Chiz ra Entekhab Kardid!]\n')
		elif personChoice.lower() == 'sang' and pcChoice == 'kaghaz':
			print(f'\n[PC Kaghaz Ra Entekhab kard Va Shoma Sang Ra Pas Shoma Bakhtid!]\n')
			print('\nPC Points +1\n')
			pcPoints += 1
		
		elif personChoice.lower() == 'sang' and pcChoice == 'gheichi':
			print(f'\n[PC Gheichi Ra Entekhab kard Va Shoma Sang Ra Pas Shoma Bordid!]\n')
			print('\nPerson Points +1\n')
			personPoints += 1
	
		elif personChoice.lower() == 'kaghaz' and pcChoice == 'sang':
			print(f'\n[PC Sang Ra Entekhab kard Va Shoma Kaghaz Ra Pas Shoma Bordid!]\n')
			print('\nPerson Points +1\n')
			personPoints += 1
	
		elif personChoice.lower() == 'kaghaz' and pcChoice == 'gheichi':
			print(f'\n[PC Gheichi Ra Entekhab kard Va Shoma Kaghaz Ra Pas Shoma Bakhtid!]\n')
			print('\nPC Points +1\n')
			pcPoints += 1
		
		elif personChoice.lower() == 'gheichi' and pcChoice == 'sang':
			print(f'\n[PC Sang Ra Entekhab kard Va Shoma Gheichi Ra Pas Shoma Bakhtid!]\n')
			print('\nPC Points +1\n')
			pcPoints += 1
		
		elif personChoice.lower() == 'gheichi' and pcChoice == 'kaghaz':
			print(f'\n[PC Kaghaz Ra Entekhab kard Va Shoma Gheichi Ra Pas Shoma Bordid!]\n')
			print('\nPerson Points +1\n')
			personPoints += 1
	elif personChoice.lower() == 'end':
		print(f'\n\nGame Ended!\nResults:\nPerson Points: {personPoints}\nPC Points: {pcPoints}')
		break
	elif not personChoice.lower() in Choices:
		print('\n[Error!]\nLotfan Entekhab ra Be Dorosti Vared Konid!\n')
		