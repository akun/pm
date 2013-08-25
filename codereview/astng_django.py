from logilab.astng import MANAGER
from logilab.astng.builder import ASTNGBuilder

def hashlib_transform(module):
    if module.name == 'django.utils.translation':
        fake = ASTNGBuilder(MANAGER).string_build('''

def ugettext_lazy(value):
    return u''

def ugettext(value):
    return u''

''')
        for hashfunc in ('ugettext_lazy', 'ugettext'):
            module.locals[hashfunc] = fake.locals[hashfunc]

def register(linter):
    """called when loaded by pylint --load-plugins, register our tranformation
    function here
    """
    MANAGER.register_transformer(hashlib_transform)
