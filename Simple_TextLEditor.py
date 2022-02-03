# Enter your code here. Read input from STDIN. Print output to STDOUT


def read_command(command):
    return command.split(' ')

def append(text, string):
    return text + string

def delete(text, last_char_index):
    return text[:-int(last_char_index)]

def print_index(text, index):
    print(text[int(index) -1])

def undo(old_text):
    return old
    


n = int(input())

text = ''
ops = []
for index in range(n):
    ops.append(input())    
    
stack = []

for raw_command in ops:
    parsed_command =  read_command(raw_command)
    
    command = int(parsed_command[0])
    
    if command == 1:
        stack.append(text)
        text = append(text, parsed_command[1])
    elif command == 2:
        stack.append(text)
        text = delete(text,parsed_command[1])
    elif command == 3:
        
        print_index(text, parsed_command[1])
    elif command == 4:
        text = stack.pop()
    
