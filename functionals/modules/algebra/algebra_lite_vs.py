
class Algebra: pass


import factors
from functools import wraps

def equation(func):
    '''Decorator for manipulating equations.
       (rest of the functions are generalised only for polynomials.)'''
    @wraps(func)
    def wrapper(self, term: str):       #change the signature as needed
        if iseqn(self):
            sn = sign(self)
            if iseqn(term):     # equation with another equation
                assert '=' in f'{self},{term}', 'Can only %s equations with ineqalities' % func.__name__.replace("__",'')
                term = Algebra(term)
                s,t = sn, sign(term)
                sn = s if s!='=' else t if t!='=' else '='
                return equate(func(self.lhs,term.lhs), func(self.rhs,term.rhs),sn)
            else:               # equation with a single term
                return equate(func(self.lhs,term), func(self.rhs,term),sn)

        return func(self, term)
    return wrapper


iseqn  = lambda eqn: any([i in str(eqn) for i in ('=','<','>','<=','>=','!=')])
sign   = lambda eqn: [i for i in ('=','<','>','<=','>=','!=','') if i in str(eqn)][0]
equify = lambda expr: str(expr).replace('**','^').replace(' ','').replace('==','=')

equate = lambda l, r, sign = '=': Algebra(f'{l}{sign}{r}')
simpler = lambda num: i if (i:=int(num)) == (f:=float(num)) else f


def var(term: str):
    '''Returns the variable of the supplied term.'''
    def var(term: str):
        '''The main func responsible...'''
        term = equify(term)
        var = []
        for n,i in enumerate(term):
            if i.isalpha():
                var.append(i)
            if i == '^' and '(' not in term:
                var.extend(['^'+term[n+1]])

        return ''.join(var)

    if '/' not in str(term): return var(term)

    num, den = term.split('/')
    if var(num) and var(den):               # if both num & den have variables
        return f'{var(num)}/{var(den)}'

    elif not var(num) and var(den):         # if num does not have variables but den has
        return f'1/{var(den)}'

    elif var(num) and not var(den):         # If nam have variable but den does not have
        return var(term)
    else: return ''                         # If None of'em has variables


def const(term: str):
    '''Returns the constant integer of the supplied term.'''
    if '/'  in (term:= str(term)):
        n,d = term.split('/')
        n,d = n.replace(var(n),''), d.replace(var(d),'')
        return simpler(const(n)/const(d))

    num = str(term).replace(var(term),'')

    if '.' in num: return simpler(eval(num))
    if num == '-': return -1
    elif num =='': return 1

    return int(num)


alpha = lambda term: ''.join(a for a in str(term) if a.isalpha())

like = lambda term1, term2: var(term1) == var(term2)


def terms(expr: str):
    '''Returns a list of terms in the supplied expression'''
    eqn = equify(expr).replace('+','|').replace('-','|-').replace('=','|=|')
    terms = eqn.split('|')

    for n,i in enumerate(terms):
        if i == '': terms.remove(i)
        try:    terms[n] = simpler(eval(i))
        except: continue

    return terms


def unterm(termz: list):
    '''Returns the algebraic expression from the supplied list of terms.'''
    expr = list(termz)
    for n,i in enumerate(expr):
        if i == '=': continue
        if type(i) == int: expr[n] = str(i)

        if var(i) != '':
            if const(i) == 1:
                expr[n] = var(i)
            elif const(i) == (-1):
                expr[n] = '-'+var(i)

        if const(i) == 0: del expr[n]

    return Algebra('+'.join(expr).replace('+-','-').replace('+=+','='))


constz = lambda expr: tuple(const(i) for i in terms(expr) if i != '=')

varz   = lambda expr: sorted({var(i) for i in terms(expr) if var(i)})

alphaz = lambda expr: sorted(set(map(alpha,terms(expr))))


pow_dict = termd = lambda expr: {p : [term for term in terms(expr) if power(term) == p] for p in range(deg(expr),-1,-1)}

var_dict = liked = lambda expr: {v : [term for term in terms(expr) if var(term) == v] for v in varz(expr)+['']}

alpha_dict=alphad= lambda expr: {a : [term for term in terms(expr) if alpha(term) == a] for a in alphaz(expr)}


def simplified(expr: str):
    '''docstring'''
    var_num = {var : sum(const(i) for i in val) for var,val in liked(expr).items()}
    return unterm(str(num)+var for var,num in var_num.items())


def power(term: str):
    '''docstring'''
    if '^' in (Var := var(term)):
        return int(Var.replace(alpha(term),'').replace('^',''))
    elif Var == '':
        return 0
    else:
        return 1


deg = lambda expr: max( power(i) for i in terms(expr))

pow_sorted = lambda expr: unterm(factors.sum(termd(expr).values()))


def sort(expr: str):
    '''Returns a sorted format of the supplied expression.'''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    sorted_alg = []
    ind = lambda trm: alp.index(alpha(trm))

    for val in termd(expr).values():
        indlist = [ind(i) for i in val]

        while indlist:
            for i in val:
                if ind(i) == min(indlist):
                    sorted_alg.append(i)
                    val.remove(i)
                    indlist.remove(ind(i))

    return unterm(sorted_alg)


def std(eqn: str):
    '''Returns the supplied equation in standard form:
        "ax+by-c=0"'''
    if not iseqn(eqn): return sort(simplified(eqn))
    eq = Algebra(eqn)
    return Algebra(f'{sort(simplified(eq.lhs-eq.rhs))}{sign(eq)}0')


# Remove them if they're already in roots
coeff = lambda v, expr: [const(i) for i in terms(expr) if var(i) == v][0]
val   = lambda v, eqn: -[i for i in terms(std(eqn)) if type(i) == int][0]/coeff(v,eqn)


def common(expr: str):
    '''Returns the common term in supplied polynomial.'''
    com_num = factors.hcf(*constz(expr))
    com_pow = min(power(trm) for trm in terms(expr))
    com_trm = com_num*(Algebra(a[0])**com_pow) if len(a:= alphaz(expr)) == 1 else (com_num)
    return str(com_trm)


def quad_eq(a: int, b: int, c: int):
    '''Returns the roots of the supplied terms of a quadratic equation.
       Equation must be of the form: "ax^2 + bx + c" (for variable x)'''
    a, b, c = int(a),int(b),int(c)

    D = b**2 - 4*a*c

    if D > 0:
        num1, num2 = (-b + D**0.5)/(2*a), (-b - D**0.5)/(2*a)
        return [simpler(num1), simpler(num2)]
    elif D == 0:
        return [(quadr:= simpler(-b/(2*a))), quadr]
    elif D < 0:
        return []


def sigma(i: int, n: int, expr: str):
    '''Returns the solution of the Sigma expr from the supplied:
        n
        Σ (expr)
       i=1'''
    expr = expr.replace(alpha(expr)[0],'i')
    return sum(Algebra(expr).solve_for(i = num) for num in range(i,n+1))


def series(expr: str, extent: range):
    '''Returns a series of numerals in the supplied 'expr' within the supplied 'extent'.
       series('2i', range(6)) -> <generator object>'''
    v = varz(expr)[0]
    return (Algebra(expr).solve_for(**{v:i}) for i in extent)



#_________________________<class '__name__.Algebra'>_________________________________________________

class Algebra:
    '''Purpose'''

    def __init__(self,expr: str):
        '''Initializes the equation for the Algebra object.'''
        self.eq = equify(expr)

        if iseqn(self.eq):
            eq = self.eq.split(sign(self.eq))
            self.lhs = Algebra(eq[0])
            self.rhs = Algebra(eq[-1])

    poly = classmethod(lambda cls, eqn: cls(str(std(eqn)).replace(f'{sign(eqn)}0','')))


    copy = lambda self: unterm(terms(self))

    __iter__ = lambda self: iter(terms(self))


# booleans:

    def __contains__(self, item):
        '''Returns item in self'''
        elems = [i for i in self]
        nums = [const(i) for i in self]
        alps = [var(i) for i in self]
        return item in (elems + nums + alps + [str(n) for n in nums])


    def __lt__(self, expr: str):
        '''Returns self < expr ( for variables == 1).'''
        expr = Algebra(expr)
        one = {a : 1 for a in alphaz(self)}
        self_int = self.solve_for(**one)
        expr_int = expr.solve_for(**one)
        return self_int < expr_int

    __eq__ = lambda self, expr: set(terms(simplified(self))) == set(terms(simplified(expr)))

    __ne__ = lambda self, expr: not self == expr

    __gt__ = lambda self, expr: False if self == expr else not self < expr

    __le__ = lambda self, expr: self < expr or self == expr

    __ge__ = lambda self, expr: self > expr or self == expr


# calculators:

    __add__  = equation(lambda self, expr: simplified(f'{self}+{expr}'.replace('+-','-')) if expr != -Algebra(self) else 0)
    #__add__ = equation(lambda self, expr: simplified(unterm(terms(self)+terms(expr))) if expr != -Algebra(self) else 0)

    __sub__  = equation(lambda self, expr: self + (-(Algebra(expr))) if expr != self else 0)

    __radd__ = lambda self, expr: self + expr

    __rsub__ = lambda self, expr: -(self) + expr

    __rmul__ = lambda self, expr: self * expr

    __mod__  = lambda self, expr: simplified(rem) if (rem := self - (self/expr * expr))!= 0 else 0

    __divmod__=lambda self, expr: (self/expr, self%expr)

    __floordiv__ = lambda self, term: self/term


    @equation
    def __mul__(self, expr: str):
        '''Returns self * term'''
        def mul(Self, val: str):
            num_mul = const(Self) * const(val)

            if not var(val):
                var_mul = var(Self)

            elif alpha(Self) == alpha(val):
                var_mul = f'{alpha(Self)}^{power(Self) + power(val)}'

            else: var_mul = var(Self) + var(val)    # elif alpha(Self) != alpha(val):

            return str(num_mul) + var_mul
        prod = []
        for s in self:
            for v in terms(expr):
                prod.append(mul(s,v))

        return simplified(unterm(prod))


    @equation
    def __pow__(self, expt: int):
        '''Returns self**expt'''
        prod = 1
        for i in range(int(expt)): prod *= self
        if prod != 1: prod.sort()

        return prod


    def __truediv__(self, expr: str):
        '''Returns self / expr'''
        expr = Algebra(expr)
        if len(expr) == 1:
            if const(expr) == 1:  return self
            elif not const(expr): raise ZeroDivisionError('devision by zero')

        elif self == expr: return 1

        def div(Self, val, /):
            num_div = simpler(const(Self)/const(val))
            if like(Self,val):
                var_div = ''
            elif alpha(Self) == alpha(val):
                exp = power(Self) - power(val)
                suffix = f'^{exp}' if exp > 1 else ''
                var_div = alpha(Self) + suffix
            else:
                var_div = var(Self)+'/'+var(val)

            return str(num_div) + var_div

        first = lambda eqn: terms(pow_sorted(eqn))[0]

        quot = []
        rem = self.copy()
        trm = first(expr)
        while deg(rem) >= deg(expr):
            quo = div(first(rem),trm)
            quot.append(quo)
            rem -= expr*quo
            rem = std(rem)

        return unterm(quot)


# uninumericals:

    __invert__ = lambda self: -(self +1)

    __pos__ = lambda self: self

    __neg__ = lambda self: unterm(str(-const(i)) + var(i) for i in self)

    __abs__ = lambda self: unterm(str(abs(const(i))) + var(i) for i in self)

    __len__ = lambda self: len(terms(self))

    __int__ = lambda self: int(sum(constz(self)))

    __reversed__ = lambda self: reversed(terms(self))


# etcetra:

    sort = lambda self: exec('self.eq = sort(self)')

    simplify = lambda self: exec('self.eq = simplified(self)')

    pow_sort = lambda self: exec('self.eq = pow_sorted(self)')

    solve_for = lambda self, **constants: sum((const(i)*(constants[alpha(i)]**power(i))if alpha(i) != '' else i) for i in self)


    def draw_graph(self, extent: range = None, f: type(sort) = None):
        '''Plots the graph of the supplied equation ('self')
           with the slope in the given range (extent)'''
        '''You can specify eqn in the form "y=f(x)", for functional equations
           and specify the 'ƒ' in last argument
           >>>from math import sin, log      # For instance...
           >>>Algebra("y = f(x)").draw_graph(range(-40, 20), sin)
           >>>Algebra("y = f(x)").draw_graph(range(-40, 20), f = lambda x: log(x**2 + 4*x +4))'''
        from matplotlib.pyplot import title, xlabel, ylabel, plot, show

        extent = extent if extent else \
                 range(int(2*min(self.roots())),int(2*max(self.roots())))

        if self.eq == 'y=f(x)':
            x,y = [i for i in extent], [f(i) for i in extent]

        if deg(self) == 2:
            x = [i for i in extent]
            y = [self.solve_for(**{f'{alphaz(self)[1]}':i}) for i in x]

        title(str(self.eq))
        xlabel('x-axis ->')
        ylabel('y-axis ->')

        x_axis = plot(list(extent),[0 for i in extent],color='black',linewidth = 1)
        y_axis = plot([0 for i in range(-100,100)],[i for i in range(-100,100)],color='black',linewidth = 1)

        plot(x,y,linewidth=1)
        show()

        # You can see more in 'graph' method in "algebra" module. (This is algebra_lite)


    def roots(self, *eqns: Algebra):
        '''Returns a list of roots; You must add more equations if self contains more than one var'''
        if eqns:
            assert all(varz(i)==varz(self) for i in eqns)

            if len(eqns)==1 and len(varz(self))==2 and deg(self)==1:     # if linear equation in 2 var
                eq, eq1 = std(eqns[0]), std(self)
                A, B = constz(eq), constz(eq1)
                assert A[0]/B[0] != A[1]/B[1], 'The equations are not consistent !'

                x,y = varz(self)

                root_y = val(y, std(eq1*coeff(x,eq) - eq*coeff(x,eq1)))  # Its wrong !!
                root_x = val(x, std(str(eq1).replace('y',str(root_y))))  # Its wrong too !!

                return [simpler(root_x), simpler(root_y)]

                # You have 3 methods: Substitute, Eliminate, Cross-mul
                # Practise at the shell well before implementing...


        assert len(alphaz(self)) == 2, 'Supports one variable for one eqn.'

        eqn = std(self)

        if deg(eqn) == 2:
            consts = constz(eqn)

            if len(eqn) == 3:
                a,b,c = consts[0], consts[1], consts[2]
            else:
                if any(type(trm) == int for trm in eqn):
                    a,b,c  = consts[0], 0, consts[1]
                else:a,b,c = consts[0], consts[1], 0

            return quad_eq(a,b,c)

        if type(cons := terms(eqn)[-1]) == int:
            pos_facts = [p for p in range(1,cons+1) if not cons%p]
            neg_facts = (-n for n in pos_facts)
            alp = alphaz(self)[0]
            roots = []

            for p,n in zip(pos_facts,neg_facts):
                rem = self.solve_for(**{alp : p})
                if rem == 0:
                    roots.append(p)

                rem = self.solve_for(**{alp : n})
                if rem == 0:
                    roots.append(n)

            return roots
        else: return [0]


    def zeroes(self, *zero: float):
        '''Returns the other zeroes (or roots) of self from the supplied known zeroes.
           If 'zero' is left empty, will return self.roots()'''
        if not zero: return self.roots()
        v = varz(self)[0]
        eqns = [Algebra(f'{v}+{-num}') for num in zero]
        return (self/factors.prod(eqns)).roots()


    __repr__ = lambda self: str(self.eq)


    # def solve(*eqns): ...To be programmed for solving linear equaions in multy vars.
    # solve = lambda *eqns: Algebra(eqns[0]).roots() if len(eqns) == 1 else Algebra(eqns[0]).roots(*eqns)

# MORE CODE ON MATPLOLIB USED TO STAY HERE... NOW, YOU CAN ONLY SEE IT IN 'ALGEBRA' MODULE