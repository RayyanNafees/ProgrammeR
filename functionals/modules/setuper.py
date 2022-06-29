
"""Creates a 'distribution discription' setup for you easily!"""

with open("README.txt","w+") as file:
    file.write(input("Guide lines for users of your module: "))

sdict = {}

args = ['name','version','description','author','author_email','url','py_modules']

for i in args:
    sdict[i] = input(i.capitalize()+': ')

sdict['py_modules'] = [sdict['py_modules']]

code = ['from setuptools import setup \n \n',
        f'sdict = {sdict}\n',
        'setup(**sdict)']

with open("setup.py","w+") as setup:
    setup.writelines(code)

from subprocess import call
from time import sleep

try:
    call('py -3 setup.py sdist')
    sleep(3)
    call('cd dist')
    sleep(3)
    call(f"py -3 -m pip install {sdict['name']}-{sdict['version']}.tar.gz")

    print('!! MISSION ACCOMPLISHED !!')
    
except Exception as err:
    print(str(err))

x = input()
