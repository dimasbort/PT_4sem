def log(func):
    def wrapper(*args, **kwargs):
        func_str = func.__name__
        args_str = ', '.join(args)
        kwargs_str = ', '.join([':'.join([str(j) for j in i]) for i in kwargs.items()])
        with open('log.txt', 'w') as f:
            f.write('Func: ' + func_str + '\n')
            f.write('Arguments: ' + args_str + '\n')
            f.write('Kwargs: ' + kwargs_str)
        return func(*args, **kwargs)
    return wrapper


@log
def example(a, b, c = 3):
    print('example')
    return a + b

if __name__ == '__main__':
    d = example('a', 'b', c='abc')
    print(d)
