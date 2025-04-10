print('Welcome to the  caesercipher program')
def ceasercipher():
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    value = True
    while value:
        print("Type 'encode' to encrypt, type 'decode' to decrypt:")
        decision = input()
        message = input('enter your message : ')
        shift = int(input('enter your shift value :'))
        if decision.lower() == 'encode':
            encodedvalue = ''
            for i in message:
                if i == ' ':
                    encodedvalue += i
                else:
                    index_value = alphabets.index(i)
                    index_value += shift
                    if index_value > 25:
                        index_value = 26 - index_value
                    encodedvalue += alphabets[index_value]
            print(f'your encoded message {encodedvalue}')
        elif decision.lower() == 'decode':
            decodedvalue = ''
            for m in message:
                if m == ' ':
                    decodedvalue += m
                else:
                    index_value2 = alphabets.index(m)
                    index_value2 -= shift
                    decodedvalue += alphabets[index_value2]
            print(f'your decode message is {decodedvalue}')
        loop = input('If you want to continue Type Yes or No')
        if loop.lower() == 'yes':
            value = True
        elif loop.lower() == 'no':
            value = False

ceasercipher()


