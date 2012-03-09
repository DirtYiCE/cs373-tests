#! /usr/bin/env python

import sys, os

if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print('Usage: %s homework_id [command [parameters]]' % sys.argv[0])
    print('Where command can be:')
    print('edit:   edit solution with $EDITOR')
    print('zap:    delete your solution')
    print('test:   test your solution with the provided test cases')
    print('format: gets your solution in the format suitable for uploading')
    print('run:    run the output of format')
    exit(-1)

hw = sys.argv.pop(1)
try:
    action = sys.argv.pop(1)
except IndexError:
    action = 'test'

os.chdir(sys.path[0])

def format():
    f = open('%s/template.py' % hw, 'r')
    s = f.read()
    f.close()
    f = open('%s/code.py' % hw, 'r')
    s2 = f.read()
    f.close()

    import re
    def repl(m):
        return m.group(1) + ('\n' + m.group(1)).join(s2.split('\n'))

    return re.sub('(.*)# !code!', repl, s, re.MULTILINE)

if action == 'edit':
    import shlex, subprocess

    if not os.path.isfile('%s/code.py' % hw):
        f = open('%s/code.py' % hw, 'w')
        if os.path.isfile('%s/base_code.py' % hw):
            f2 = open('%s/base_code.py' % hw, 'r')
            f.write(f2.read())
            f2.close()
        f.close()

    cmd = shlex.split(os.environ['EDITOR'])
    cmd.append('%s/code.py' % hw)

    subprocess.call(cmd)
elif action == 'zap':
    os.remove('%s/code.py' % hw)
elif action == 'test':
    import unittest
    sys.path[0:0] = [os.path.abspath(hw)]
    import testcase
    sys.path.pop(0)

    unittest.main(testcase)
elif action == 'format':
    print(format())
elif action == 'run':
    exec compile(format(), '<string>', 'exec')
else:
    print('Unknown action %s!' % action)
    exit(-1)
