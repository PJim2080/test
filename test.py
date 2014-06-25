import sys
print sys.__name__
#print sys.argv[1]
s=raw_input('Enter something -->')
print s

try:
    s=raw_input('Enter something --> ')
except EOFError:
    print 'Input Error!'
print s
