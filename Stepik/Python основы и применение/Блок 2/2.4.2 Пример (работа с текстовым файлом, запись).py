#  r (read) - открыть для чтения (по умолчанию)
#  w (write) - открыть для записи, содержимое файла стирается
#  a (append) - открыть для записи, запись ведется в конец файла

f = open('test1.txt', 'w')
f.write('Hello\n')
f.write('world')
f.close()
print('_____________________________________________________________________________')

f = open('test1.txt', 'w')
lines = ['Line 1', 'Line 2', 'Line 3']
contents = '\n'.join(lines)
f.write(contents)
f.close()
print('_____________________________________________________________________________')

'Режим append - запись в конец файла'
f = open('test_append.txt', 'a')
f.write('Hello\n')
f.close()