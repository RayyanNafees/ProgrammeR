
def val(cmd: str) -> object:
    '''Returns the object value from the stringified object.
       Example: val(func.__name__) -> func'''
    obj = []
    cmds = cmd.split('\n')
    for i in range(1):
        if '\n' in cmd:
            exec('{}\n obj.append(cmds[-1])'.format('\n'.join(cmds[:-1])))
        else: exec(f'obj.append({cmd})')
    return obj[0]
