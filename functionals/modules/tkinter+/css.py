def cssify(csstr):
    if csstr.startswith('{')and csstr.endswith('}'):
        csstr =  csstr.replace('{','').replace('}','').strip()
    if csstr.endswith(';'):
        csstr = csstr[:-1]
    return csstr.rstrip()

def dictify(cssdict):
    for k,v in cssdict.items():
        if v=='none':
            cssdict[k] = None
    #remains more to do such as rgb & rgba
    return cssdict

css2dict    = lambda csstr: {prop.strip() : val.strip() for prop, val in ( q.split(':') for q in cssify(csstr).split(';') )}
val_replace = lambda old, new, _dict: {k: (v if v is not old else new) for k,v in _dict.items()}
key_replace = lambda old, new, _dict: {(k if k is not old else new): v for k,v in _dict.items()}
