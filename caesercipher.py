print('Welcome to the Caesar Cipher program')

def caesar_cipher():
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while True:
        print("\nType 'encode' to encrypt, type 'decode' to decrypt:")
        decision = input().lower()
        
        if decision not in ['encode', 'decode']:
            print("Invalid choice! Please enter 'encode' or 'decode'")
            continue
            
        message = input('Enter your message: ').lower()
        if not message:
            print("Message cannot be empty!")
            continue
            
        try:
            shift = int(input('Enter your shift value (1-25): '))
            if shift < 1 or shift > 25:
                print("Shift value must be between 1 and 25")
                continue
        except ValueError:
            print("Invalid shift value! Please enter a number")
            continue

        result = ''
        for char in message:
            if char in alphabets:
                if decision == 'encode':
                    index_value = (alphabets.index(char) + shift) % 26
                else:  # decode
                    index_value = (alphabets.index(char) - shift) % 26
                result += alphabets[index_value]
            else:
                result += char  # Keep non-alphabetic characters unchanged
                
        print(f'Your {decision}d message is: {result}')
        
        loop = input('\nDo you want to continue? (yes/no): ').lower()
        if loop != 'yes':
            print("Thank you for using Caesar Cipher!")
            break

caesar_cipher()


