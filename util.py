import numbers, os.path

# on my computer (gentoo amd64 linux, python 2.7.2) it works up to epsilon 1e-15
# (at least with homework 1.4). With 1e-16, errors start to appear. 1e-12 should
# be safe in most cases.
def arrayCmp(case, a, b, epsilon = 1e-12):
    lines = []

    def sub(a, b, eps, ma, mb, at):
        succ = len(a) == len(b)
        l = min(len(a), len(b))

        for i in range(l):
            if isinstance(a[i], numbers.Real) and \
                    isinstance(b[i], numbers.Real):
                if abs(a[i] - b[i]) > eps:
                    lines.append("Numbers %.20f and %.20f differ by %f at %s" %
                                 (a[i], b[i], abs(a[i]-b[i]), at + '[%d]' % i))
                    succ = False
            elif getattr(a[i], '__iter__', False) and \
                    getattr(a[i], '__len__', False) and \
                    getattr(b[i], '__iter__', False) and \
                    getattr(b[i], '__len__', False):
                if not sub(a[i], b[i], eps, ma, mb, at + '[%d]' % i):
                    succ = False
            else:
                if a[i] != b[i]:
                    lines.append("'%s' and '%s' are not equal at %s" %
                                 (a[i], b[i], at + '[%d]' % i))
                    succ = False

        def chkExtra(displ, a, b):
            if len(a) != l:
                lines.append('Array %s at %s has more items (%d vs %d)' %
                             (displ, at == '' and 'root' or at, len(a), len(b)))
                lines.append('Extra values: %s' % a[l:])
        chkExtra('a', a, b)
        chkExtra('b', b, a)

        return succ

    if not sub(a, b, epsilon, a, b, ''):
        lines.append("'%s' and '%s' does not equal" % (a, b))
        case.fail("\n".join(lines))

def compileFile(file_dir, funwrap = False):
    fn = os.path.join(os.path.dirname(file_dir), 'code.py')
    f = open(fn, 'r')
    s = f.read()
    if funwrap:
        s = 'def _funwrap():\n  ' + '\n  '.join(s.split('\n'))+'\n_funret = _funwrap()'

    c = compile(s, fn, 'exec')
    f.close()
    return c
