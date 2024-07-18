import string
import random
from datetime import datetime, timedelta

def DateTime(min_year=1980, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return str(start + (end - start) * random.random())

def String(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def StringWithWhitespace(length=200):
    return ''.join(random.choices(string.ascii_letters + string.whitespace, k=length))

def Number(length=10):
    return ''.join(random.choices(string.digits, k=length))

def StringNumber(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def Version(dotzero=False):
    if dotzero: 
        return str(random.randint(1,10)) + ".0"
    else:
        return str(random.randint(1,10))
    
def EntryOfArray(data=[]):
    return random.choice(data)
