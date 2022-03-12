import tkinter as tk
from tkinter import ttk


ascii_chars = dict()
for i in range(300):
    ascii_chars.update({chr(i):i})
ascii_chars.update({'return':10})

chars = dict()


def convert(word, index = 0):
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
    result = divide(ascii_chars['return'])
    for i in {n for n in word}:
        result += divide(ascii_chars[i])
        chars.update({f'{i}' : letter_index})
        letter_index +=1
    result += f'{letter_index*"<"}'
    return result


def process():
    result_box['state'] = 'normal'
    result_box.delete('1.0','end')
    initialisation = list(init(text_entry.get('1.0','end')))
    converter = list(convert(text_entry.get('1.0','end')))
    
    while converter[0] == '>':
        converter.pop(0)
        initialisation.pop(-1)
        
    result = str()
    for char in initialisation:
        result += f'{char}'
    for char in converter:
        result += f'{char}'
    print(result)
    
    result_box.insert('1.0',result)
    result_box['state'] = 'disabled'


def clipboard():
    window.clipboard_clear()
    window.clipboard_append(result_box.get('1.0','end'))


window = tk.Tk()
window.attributes('-topmost',1)
window.attributes('-topmost',0)
window.focus()
window.resizable(False,False)
window.title('Brain F*ck Converter')
window.geometry('500x400+100+100')

text_label = ttk.Label(window, text = 'Enter a text to convert')
text_label.place(x = 20, y = 20)

text_entry = tk.Text(window, width = 56)
text_entry.place(x = 23, y = 50, height = 100)

convert_button = ttk.Button(window, text = 'Convert', command = process)
convert_button.place(x = 400, y = 170 )

result_box = tk.Text(window, width = 56, height = 7)
result_box.insert('1.0','>+++++[-<++>]>++++++++++++[-<+++++++++>]>+++++++++++[-<++++++++++>]<+>>++++++++++++++[-<++++++++>]<++>>++++++++[-<++++>]>++++++++++[-<++++++++++>]<+>>+++++[-<++>]>++++++++++[-<++++++++++>]>+++++++++++++++++[-<+++++>]<++>>+++++++++[-<++++++++>]<.<<<<.<<<<..>.>>.>>>>.<<<<<<.>.<<.>>>>>>.<.')
result_box['state'] = 'disabled'
result_box.place (x = 23, y = 216)

copy_button = ttk.Button(window, text = 'Copy to clipboard', command = clipboard)
copy_button.place(x = 371, y = 346)


window.mainloop()
