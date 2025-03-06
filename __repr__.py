class Color:
    def __init__(self, color_name):
        self.color_name = color_name

    def __repr__(self):
        return f'Color({self.color_name})'

if __name__ == '__main__':
    c1 = Color('Yellow')
    c2 = repr('Yellow')   
    print("C1:",c1)
    print("C2:",c2)    