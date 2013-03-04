#!/usr/bin/python
"""
Author: Krzysztof Voss <shobbo@gmail.com>
"""

from string import Template
import subprocess
import readline
import sys

with open('templates/program_test.tpl', 'r') as f:
    tpl = Template(f.read())
ofile_fn = 'output.f'
stmts = []

def process():
    stmts_txt = '\n'.join(stmts)
    tpl_txt = tpl.substitute({
        'statements' : stmts_txt,
    })
    return tpl_txt

def print_stm():
    for idx, s in zip(range(len(stmts)), stmts):
        print idx,':',s

def help_me():
    print 'available: Fortran/!e (also !!)/!c/!d/!l/!h/!q'

if __name__ == '__main__':

    while True:
        while True:
            line = raw_input('>>> ')
            if line == '!e' or line == '!!':
                break
            elif line == '!c':
                stmts = []
            elif line == '!l':
                print_stm()
            elif line == '!d':
                idx = int(raw_input('!l idx to delete: '))
                stmts.pop(idx)
                print_stm()
            elif line == '!h':
                help_me()
            elif line == '!q':
                sys.exit(0)
            else:
                stmts.append(' '*6 + line)

        code = process()
        with open(ofile_fn, 'w') as f:
            f.write(code)

        cmd = ['gfortran', '-g', '-Wall', ofile_fn ]
        ret = subprocess.call(cmd)
        if ret == 0:
            cmd = ['./a.out']
            try:
                ret = subprocess.call(cmd)
            except:
                pass
