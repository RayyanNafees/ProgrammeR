
from flask import Flask, escape, render_template, request
from subprocess import call
from sys import exc_info

app = Flask(__name__)

@app.route('/')         # Keep it for webpage frames...
def code() -> 'html':
    return render_template('io.html')

@app.route('/in')
@app.route('/idle')
def input():
    return render_template('input.html')


@app.route('/out', methods = ['POST'])
def output():
    print((x:=request.form['code']))
    codes = x.split('\n')
 
    for n,i in enumerate(codes):
        if 'print(' in i:
            ilist = list(i)
            ilist.insert(i.rindex(')'),',file = out')
            I = ''.join(ilist)
            codes[n] = '    ' + I.replace('\r','\n')
        else:        
            codes[n] = '    ' + i.replace('\r','\n')
        
    codes.insert(0,"with open('out.py','w') as out:\n")

    with open('input.py','w+') as inp:
        inp.writelines(codes)

    try:
        exec(request.form['code'])  # to raise the error if any...
        call("python input.py")       # exec can also be used here...

        with open('out.py') as out:
            outp = out.readlines()

    except Exception as err:
        outp = exc_info()

    return render_template('output.html',
                           output = outp)


'''import subprocess
filepath = "Documents/game"
subprocess.call("python "+filepath)''' # Use it to run an external file.

# Just figure out how to get the output  from a file...

if __name__ == '__main__':
    app.run(debug=True)
