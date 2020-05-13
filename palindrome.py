def convert(w):
    tmp = ''
    for l in w.lower():
        if l in 'йцукенгшщзхъфывапролджэячсмитьбюё':
            tmp += l
        else:
            tmp += ''
    return tmp

def palindrome(w):
    if len(w) <= 1:
        return True
    else:
        return w[0] == w[-1] and palindrome(w[1:-1])
 


# w = '"Ура!" - вопите, дети, повару!'
w = 'simon lemon'
w_converted = convert(w)
w_palindromed = palindrome(w_converted)
print(w_palindromed)