def divide(a,b):
    if not isinstance(a,(int)):
        raise TypeError('第一个输入非整数')
    if not isinstance(b,(int)):
        raise TypeError('第二个输入非整数')
    if b==0:
      print('除数不能为0')
      return
    return float(a)/b

if __name__ == "__main__":
    a = int(input("a="))
    b = int(input('b='))
    print('a/b = %f'%divide(a,b))
    


