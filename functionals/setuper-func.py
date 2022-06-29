def setuper():
    """Creates a 'distribution discription' setup for you easily!"""

    with open("README.txt","w+") as file:
        file.write(input("Guide lines for users of your module: "))
        
    args = ['name','version','description','author','author_email','url','py_modules']
    
    sdict = {input(i.capitalize()+': ') for i in args 

    sdict['py_modules'] = [sdict['py_modules']]

    code = ['from setuptools import setup \n \n',
            f'sdict = {str(sdict)} \n',
            'setup(**sdict)']

    with open("setup.py","w+") as setup:
        setup.writelines(code)
