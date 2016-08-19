import os

nb = raw_input('Enter number of pages: ')

try:
	nrp = int(nb)
except ValueError:
	print("Invalid number")

curpag = 1

while curpag <=nrp:
	#pixma:04A9173A_1A840C is printer model shown at scanimage -L 
	string='scanimage -d "pixma:04A9173A_1A840C" --format jpg > page'+ str(curpag) +".jpg"
	os.system("echo Scanning...")
	os.system(string)
	string2 = "convert page" + str(curpag) + ".jpg -resize 5000" + " spage" + str(curpag) +".tif"
	os.system("echo Converting...")
	os.system(string2)
	string3 = "tesseract spage" + str(curpag) +".tif text" +str(curpag) + " -l ron"
	os.system(string3)
	string4 = "rm -f page" + str(curpag) +".jpg spage" +str(curpag)+ ".tif"
	os.system("echo Removing jpg and tif files...")
	os.system(string4)
	curpag=curpag+1
	raw_input("Press Enter to continue...")