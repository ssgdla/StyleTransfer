import os

def main():
    path = "./videos"
    stylePic = "./images/japanMoutain2.jpg"
	

    filelist = os.listdir(path)
    os.system("mkdir results")

    for afile in filelist:
	inputPic = path+"/"+afile
	outputPic= "./results/"+ afile	

	command = "python run_main.py --content %s --style %s --output %s" %(inputPic,stylePic,outputPic)	
	
	os.system(command)

if __name__ == '__main__':
    main()
