def builder(r):
    for i in range(r):   #r can be replaced with any number. 
        print(str(i+1)*(i+1)) # if user input is 2 then: 1st iter - '1' (0 digit (but text) + 1 by 0+1 = 1), 2nd iter - ((1+1) digit times (1+1) equals 22)

def userinput():
    return int(input("Type a number: ")) #returns a number to a iterable, what calls this function

def main():
    number = userinput()  #makes a local iter. named "number" and gets a userinput() (that is... well... equal to user input.)
    builder(number)  #calls function "builder" and inserts "number" there to... well look at line 3

main()  #executes main (the whole code lol) then an iterable (inside 'main')"number" calls 'userinput()' func. that RETURNS an integer that you type on a keyboard TO "number" inside "main"