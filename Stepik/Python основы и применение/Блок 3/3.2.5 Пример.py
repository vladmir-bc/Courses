capital = 'London is the capital of Great Britain'
template = '{0} is the capital of {1}'
print(template.format('London', 'Great Britain'))
print(template.format('Vaduz', 'liechtenstein'))

template = '{capital} is the capital of {country}'
print(template.format(capital='London', country='Great Britain'))
