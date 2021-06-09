import re


if __name__ == '__main__':
    print('Enter email address')
    email = input()
    pattern = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if len(re.findall(pattern, email)) > 0:
        print('valid')
    else:
        print('not valid')

    print('Enter float number')
    float = input()
    pattern = r'^\d*.\d*$'
    if len(re.findall(pattern, float)) > 0:
        print('valid')
    else:
        print('not valid')

    print('Enter url')
    email = 'https://www.google.com/dir/1/2/search.html?arg=0-a&arg1=1-b&arg3-c#hash'
    pattern = r''
    host = re.findall(pattern, email)
    print(host)
