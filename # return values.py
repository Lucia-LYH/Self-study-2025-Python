# return values
lang = input ('type the language you use:')
def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'bonjour'
    else:
        return 'hello'

print (greet (lang), 'Julia')
#print (greet ('fr'), 'Hely')
#print (greet ('en'), 'Lina')

# so the difference between return & print?
# 'return' ends the function immediately, and sends a value back to wherever the function was called
    # def xxx(xx):
     #if...:
     #return
     #...
     #print (xxx(xx))
# 'print' prints out the result
    #def xxx(xx):
    #if...:
    #print('')
    #...
    #xxx(xx)
