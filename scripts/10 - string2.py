molde = "{} eh uma linguagem {}"
print(molde.format('Python', 'facil'))

molde = "{0} eh uma linguagem {1}mente {1}"
print(molde.format('Python', 'facil'))

molde = "{a[0]} eh uma linguagem {a[1]}mente {a[1]}"
print(molde.format(a = ('Python', 'facil')))