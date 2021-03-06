# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 
path = "C:/Users/Yxchi/Downloads/Interaction Record/"
# Function to rename multiple files 
def main(): 
    for folder in os.listdir(path):
        for filename in os.listdir(path + folder + '/'):     	
            dst = folder + " - " + filename
            src = path + folder + '/' + filename 
            dst = path + folder + '/' + dst 
            os.rename(src, dst) 
# Driver Code 
if __name__ == '__main__': 
	# Calling main() function 
	main() 
