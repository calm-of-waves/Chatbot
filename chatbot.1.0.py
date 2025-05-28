databaza = {
    'Hello' : 'Hello',
    'Nahili yagdaylarynyz?': 'Elhamdulillah gowy, siz nahili?'
    'Name etyan?' : 'Siz bilen yazyshyp otyn:)'
}
while (True):
    word = input(f'''You: ''')
    if (word.lower().strip() =='exit'):
        print(f''' 
        ________________Closing_________
    ''')
        break

    if(word in databaza.keys()):
        print(f''' Komputer: {databaza[word]} ''')
    elif(word not in databaza.keys()):
        answer = input(f'''I dont know {word}, How can I answer this question?
                        If you teach me, I'll not forget \n New answer: ''')

        databaza[word] = answer








