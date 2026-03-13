
'''
item = list()
print(item)

item.append('egg')
print(item)

stuff=[]
stuff.append(185)
print(stuff)

alphabets = 'AFSDFSIOHNWD'
print(alphabets)
newform = list(alphabets)
print(newform)

text ='good day     hello'
print(text.split())
words = text.split()
print()


s = '-'.join(alphabets)
print(s)
s1 = ''.join(alphabets)
print(s1)
s2 = 'scasd'.join(alphabets)
print(s2)

if 'A' in alphabets: print('yay')
if 'a' in alphabets: print('nar')
'''


'''
#for strings, list, tuple
#will show error bc not in the string 
print('index G?', newform.index('G'))

#will print out indexW?and10(position)
print('index W?', newform.index('W'))


#for strings ONLY
#wil print out findA?and10(position)
print('find A?', alphabets.find('A'))

#will print out findZ?and-1(bc not found,so show-1)
print('find Z?', alphabets.find('Z'))
'''

line = input('gibberish hehe')
print('that line was', len(line), 'characters long')















