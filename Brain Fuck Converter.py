ascii_chars = {
    ' ' : 32,
    'a' : 97,
    'b' : 98,
    'c' : 99,
    'd' : 100,
    'e' : 101,
    'f' : 102,
    'g' : 103,
    'h' : 104,
    'i' : 105,
    'j' : 106,
    'k' : 107,
    'l' : 108,
    'm' : 109,
    'n' : 110,
    'o' : 111,
    'p' : 112,
    'q' : 113,
    'r' : 114,
    's' : 115,
    't' : 116,
    'u' : 117,
    'v' : 118,
    'w' : 119,
    'x' : 120,
    'y' : 121,
    'z' : 122,
    '0' : 48,
    '1' : 49,
    '2' : 50,
    '3' : 51,
    '4' : 52,
    '5' : 53,
    '6' : 54,
    '7' : 55,
    '8' : 56,
    '9' : 57,
    'é' : 130,
    'è' : 138,
    'ç' : 135,
    'à' : 133,
    'ê' : 136,
    'î' : 140,
    'ô' : 149,
    'ï' : 139,
    'A' : 65,
    'B' : 66,
    'C' : 67,
    'D' : 68,
    'E' : 69,
    'F' : 70,
    'G' : 71,
    'H' : 72,
    'I' : 73,
    'J' : 74,
    'K' : 75,
    'L' : 76,
    'M' : 77,
    'N' : 78,
    'O' : 79,
    'P' : 80,
    'Q' : 81,
    'R' : 82,
    'S' : 83,
    'T' : 84,
    'U' : 85,
    'V' : 86,
    'W' : 87,
    'X' : 88,
    'Y' : 89,
    'Z' : 90,
    '.' : 46,
    ':' : 58,
    ';' : 59,
    "'" : 39,
    ',' : 44,
    ')' : 41,
    '(' : 40,
    'return' : 10
    
    }

chars = dict()

def convert(word,index = 0):
    output = list()
    result = ''
    index = index
    
    for letter in word:
        
        while index != chars[str(letter)]:
            
            if index < chars[str(letter)]:
                output.append('>')
                index += 1
            elif index > chars[str(letter)]:
                output.append('<')
                index -= 1
        output.append('.')

    for i in range(len(output)):
        result += output[i]
        
    pos_check = 0 
    for i in result:
        if i == '<':
            pos_check -= 1
        elif i == '>':
            pos_check += 1
    result += f'{pos_check*"<"}.'
    
    print(result)
    return result

def divide(n,s = 0):
    

    i = n
    best_sum = list()
    store_list = list()
    
    # Dividing of the number
    while i >1:
        i -= 1
        if n%i == 0:
            
            # Creation of a list of the products
            best_sum.append([i,n//i])
            store_list = [n for n in best_sum]


    # Summing the products to compare them
    for i in range(len(best_sum)):
        best_sum[i] = sum(best_sum[i])


    # Take the lowest product
    f = 0
    t = max(best_sum)
    r = 0
    while f < len(best_sum)-1:
        if best_sum[f] < t:
            t = best_sum[f]
            r = f
        f += 1

    # print the best result
    
    output = f'>{int(store_list[r][0])*"+"}[-<{int(store_list[r][1])*"+"}>]'
    
    if len(output) > 30:
        s += 1
        output = f'{divide(n-1,s)}'
        
        if len(output) <= 30 and output[-1] == ']':
            output += f'<{s*"+"}>'
            
    return output


def init(word):
    letter_index = 1
    print(divide(ascii_chars['return']))
    for i in {n for n in word}:
        print(divide(ascii_chars[i]))
        chars.update({f'{i}' : letter_index})
        letter_index +=1
    print(f'{letter_index*"<"}')


linesnum = int(input('How many lines : '))
sentences = list()
initword = ''
for i in range(linesnum):
    sentences.append(input(f'Sentence {i+1} : '))
    
for n in range(len(sentences)):
    initword += sentences[n]

init(initword)
for n in sentences:
    convert(n)