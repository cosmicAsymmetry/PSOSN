from pkgutil import iter_modules

modules = [name for _, name, __ in iter_modules()]

def check_import(packagename):
	if packagename in modules:
		print('{} .... check!'.format(packagename))
		return True
	else:
		return False

packages = ['pymongo', 'twitter', 'facebook', 'numpy', 'scipy', 'matplotlib',
            'sklearn', 'igraph', 'nltk', 'networkx', '_mysql']

all_passed = True

for p in packages:
    assert check_import(p), '{0} not present'.format(p)

if all_passed:
    print('All checks passed')