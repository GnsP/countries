import json

poptab = [ x.split(', ') for x in open('country-list.csv').read().split('\n')]
captab = [ x.split(', ') for x in open('country-capitals.csv').read().split('\n')]
flgtab = [ x.split(', ') for x in open('country-flags.csv').read().split('\n')]
curtab = [ x.split(', ') for x in open('country-currency.csv').read().split('\n')]

popmap = dict([[x[1], { 'population': x[2], 'area': x[3], 'density': x[4]}] for x in poptab if len(x) > 1])
capmap = dict([[x[0], x[1:]] for x in captab if len(x) > 1])
curmap = dict([[x[0], { 'currency': x[1], 'code': x[2]}] for x in curtab if len(x) > 1])
flgmap = dict([[x[1], x[0]] for x in flgtab if len(x) > 1])
countries = [x[1] for x in poptab if len(x) > 1]

res = [{
    'serial': i+1,
    'name': countries[i],
    'capitals': capmap[countries[i]],
    'currency': curmap[countries[i]]['currency'],
    'currency_code': curmap[countries[i]]['code'],
    'population': popmap[countries[i]]['population'],
    'area': popmap[countries[i]]['area'],
    'population_density': popmap[countries[i]]['density'],
    'flag': flgmap[countries[i]]
} for i in range(len(countries))]

print(json.dumps(res, indent=4))
