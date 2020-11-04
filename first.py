print('Study python Basic')
print("프린트")
print('''프린트''')
print("""프린트""")
print()


#separator 옵션
print('p','y','t','H','o',sep='')
print('p','y','t','H','o',sep='ㅡㅡ')
print('010','7777','1234',sep='-') 

#end옵션
print('welcome to', end=' ')
print('IT NEWS', end=' ')
print('Web Site')

#file 옵션
import sys


print('Learn Python', file=sys.stdout)

# format 사용 (d, s, f)
print('%s %s' %('one','ywo'))
print('{} {}'.format('one', 'two'))
print('{1} {0}' .format('one','two'))

# %s
print('%10s' % ('nice1111'))
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:.>10}'.format('nice'))
print('{:^10}'.format('nice'))   
print('%.5s' %('nice'))
print('%.5s' %('nicepython'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))

print('%4d' % (423132132))
print('{:4d}'.format(42))

# %f
print('%f' % (3.12321312111111113123))
print('%1.5f' % (3.12321312111111113123))
print('%1.18f' % (3.12321312111111113123))
print('{:f}'.format(3.12321312111111113123))

print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))