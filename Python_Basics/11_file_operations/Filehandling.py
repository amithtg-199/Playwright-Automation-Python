# Example 1: Create/ writing a file

# appraoch 1
file=open("C:\\Automation\\automationFiles\\myfile.txt",'w')
file.write("Welcome to python \n File handling")
file.close()


#Appraoch 2 : using with
# with open("C:\\Automation\\automationFiles\\myfile.txt",'w') as file:
#     file.write("Welcome to python \n File handling")
#     file.close()



# Example 2: Appending data into file
# file=open("C:\\Automation\\automationFiles\\myfile.txt",'a')
# file.write("\n This line is appended...")
# file.close()



# Example 3: Reading data from text file
# read() - reads entire data
#readline() - read single line
#readlines() -- read all the lines in to list format

#
# file=open("C:\\Automation\\automationFiles\\myfile.txt",'r')
# content=file.read()
# #content=file.readline()
# #content=file.readlines()
# print(content)
# file.close()


#4 Renaming the file
# import os
# os.rename("C:\\Automation\\automationFiles\\myfile.txt","C:\\Automation\\automationFiles\\myfile1.txt")
# print("File renamed...")


#5 Deleting the file
# import os
#
# file="C:\\Automation\\automationFiles\\myfile1.txt"
#
# if os.path.exists(file):
#     os.remove(file)
# else:
#     print("File does not exist")


# 6. Creating a directory/folder
# import os
# os.mkdir("C:\\Automation\\automationFiles\\mydir")
# print("Directory created..")


#7. Check the directory exist or not
# import os
# mydir="C:\\Automation\\automationFiles\\mydir"
#
# if os.path.exists(mydir):
#     print("Directory exists")
# else:
#     print("Directory not exists")


#8. Rename teh directory
# import os
#
# os.rename("C:\\Automation\\automationFiles\\mydir","C:\\Automation\\automationFiles\\mydir1")
# print("Directory renamed...")


#9. remove/delete the directory
# import os
# import shutil
# os.rmdir("C:\\Automation\\automationFiles\\mydir123") # if folder/directory is empty.
# #shutil.rmtree("C:\\Automation\\automationFiles\\mydir123")  # if the folder/directory contains files


#10. get the current working directory

import os
print(os.getcwd()) # returns current working directory





