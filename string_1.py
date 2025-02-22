# Convert string pattern "A3B2C1" to "AAABBC"
def convert(val: str) -> str:
    var_str = ""
    for idx in val:
        if idx.isalpha():
            ch = idx
        elif idx.isdigit():
            num = int(idx)
            while num > 0:
                var_str += ch
                num -= 1
    return var_str

if __name__ == '__main__':
    string1 = 'A3B2C1'
    print(f'{convert(string1)=}')                
