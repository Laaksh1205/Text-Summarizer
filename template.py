    #to open vs code on terminal: code .
#will be writing the entire project structure in this file
import os
from pathlib import Path
import logging
#to log all the info during runtime as well

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
#to create login stream

project_name = "text-summarizer"
#will be creating SRC like source, it will have the porject name, inside which all the compoents will be there

list_of_files = [
    ".github/workflows/.gitkeep",
    #will be using it at time of CICD deployment, we just write our CI CD Related EML automatic file 
    #whenwver we commit it will automatically take the code from GITHUB & do the deployment
    #on commiting this code in github, the empty folder won't be uploaded so using some file gitkeep file, its like hidden file

    f"src/{project_name}/__init__.py",
    #consturctor file is needed because this thing is installed as my local package
    #like to do operations like import for components from the project 
    #&when to install this local package this consructor file is needed

    f"src/{project_name}/components/__init__.py",
    #components is my another local package

    f"src/{project_name}/utils/__init__.py",
    #will be keeping all the utility functions

    f"src/{project_name}/utils/commom.py",
    #will be creating common utility functions 

    f"src/{project_name}/logging//__init__.py",

    f"src/{project_name}/config/__init__.py",

    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/pipeline/__init__.py",
    #it will contain about training & prediction pipline

    f"src/{project_name}/entity/__init__.py",

    f"src/{project_name}/constants/__init__.py",

    "conifg/config.yaml",

    "params.yaml",

    "app.py",

    "main.py",

    "Dockerfile",
    #will be using this docker file to build the image of source code & do the deployment of the image in our PC2 machine in AWS

    "requirements.txt",

    "setup.py",
    #help to install all the packages & dependencies of this project

    "research/trials.ipynb",
    #it will contain all the notebook experiments

]
#list of files I need to create 

for filepath in list_of_files:
#first of we need to covert the path to the specifed os format, we are using using windows but we are using /,
#so when weare not handling these kinds of paths it will give an error
#In Linux we use / and in windows we use \
#to handle this, we are using Path class from pathlib module in python is used.
    filepath = Path(filepath)
    #it will detect the OS I am using & based on that it will provide the path
    filedir, filename = os.path.split(filepath)
    #we need to seperate out the folder and filename, because first we need to create the folders & then the file

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    #we need to check if this file directory is not empty, beacuse if this variable is empty that means there is no folder 
    #& if not empty we run it.
    #now floder creation is done

    #to create the file
    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
                pass    
                logging.info(f"Creating empty file: {filepath}")
    else:
         logging.info(f"File already exists: {filepath}")
         #if file size is not empty, that means there is some code
         # so we not going to replace the file so it will ignore the file & will create other file
         #but if it is empty then it will replace the file