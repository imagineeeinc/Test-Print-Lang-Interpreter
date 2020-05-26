print("Plese type your command")

enter = input()

if "print(" in enter:
	if ")" in enter:
		if '"' in enter:
			if '"' in enter:
				
				length = len(enter)
				
				length = length-2
				
				printing = enter[7:length]

				print (printing)

else:
 print("syntax error")
