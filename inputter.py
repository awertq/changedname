import json

def write_file(string_to_write):
	with open(filename,"a") as f_n:
		container = f_n.write(string_to_write+"\n")           #function to append line to the file


filename = "name.txt"
entered = input("enter you'r name : ")

with open(filename,"w") as f_n:
	container = f_n.write(entered+"\n")


another = input("sex : ")
write_file(another)

while True:
	choice = input("do you want to write anything else  [enter/n]")
	if choice == "n":
		break

	else :
		to_enter = input(">>>  ")
		write_file(to_enter)

