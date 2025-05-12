
def move_2(input):
    l = 0
    input = list(input)
    for r in range(len(input)):
        if input[r] != '2':
            input[l], input[r] = input[r], input[l]
            l += 1
        
    return "".join(input)
if __name__ == '__main__':
    input = "12245622"
    print(move_2(input))
                