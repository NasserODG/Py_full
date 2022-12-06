caractere = input("\t\tEntrer your longest sentence (We prefer sentence without A) : \n")

while True:
	if "A" in caractere :
		caractere = input("\t\tEntrer your longest sentence (We prefer sentence without A) : \n")
	else:
		break
print("Successful !! Your longest sentence does not contain an A") 