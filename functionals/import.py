
import os

def Import(src: str) -> type(os):
    '''docstring'''
    mod = (loc:= src.split('/'))[-1].replace('.py','')
    os.chdir('/'.join(loc[:-1]))
    print(os.getcwd())
    print(os.listdir())
    exec(f'import {mod}', globals(), locals())
    exec(f'return {mod}')
