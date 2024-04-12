


number0f_rows = int(input(''))
numberof_columns= 3*number0f_rows
middle = int(number0f_rows/2)
pattern = '.|.'
lenof_pattern = len(pattern)
numoftimes_patterntobe_printed_lst= []
for row_num in range(middle):
    
    numoftimes_patterntobe_printed=2*row_num+1
    numoftimes_patterntobe_printed_lst.append(numoftimes_patterntobe_printed)
    char_remaining = numberof_columns-numoftimes_patterntobe_printed*lenof_pattern
    first_half = int(char_remaining/2)*'-'
    line_tobeprinted=first_half+pattern*numoftimes_patterntobe_printed+first_half
    print(line_tobeprinted)
welcome = 'WELCOME'
lenof_welcome = len(welcome)
char_remaining = numberof_columns-lenof_welcome
first_half = int(char_remaining/2)*'-'

line_tobeprinted=first_half+welcome+first_half
print(line_tobeprinted)
for numoftimes_patterntobe_printed in reversed(numoftimes_patterntobe_printed_lst):
    char_remaining = numberof_columns-numoftimes_patterntobe_printed*lenof_pattern
    first_half = int(char_remaining/2)*'-'
    line_tobeprinted=first_half+pattern*numoftimes_patterntobe_printed+first_half
    print(line_tobeprinted)

