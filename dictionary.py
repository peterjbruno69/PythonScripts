acronyms = {'LOL': 'laugh out loud',
            'IDK': "I don't know",
            'TBH': 'to be honest',
            'BTW': 'By the way'}
#definition = acronyms.get('BTW')

#if definition:
#    print(definition)
#else:
#    print("Key doesn't exist")

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') +' what happened '+ acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)

