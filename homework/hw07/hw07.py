
passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '97e452c59a442b883101399ae62ce6cb4bac08f3d1c84cbbb365504d'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()