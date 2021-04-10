from . import v
from .translate import Translate

print('\nchlorine v' + v + ' running, see web pages for more information.\n   GitHub:   https://github.com/rice0208/chlorine\n   Webpage:  https://fluorine.pythonanywhere.com/')
try:
    while True:
        print(Translate(input('\nchlorine> ')).translate())
except KeyboardInterrupt:
    print('\nUser quitted chlorine program.\n')
    exit(0)