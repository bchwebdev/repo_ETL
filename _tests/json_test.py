import json
from io import StringIO


print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))


io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())


def clean_json(path, target):
	"""Delete key in the JSON file"""
	import json
	changed = False
	targets = target.split('/')

	# read file to parser
	js = json.load(open(path, 'r'))

	# change file
	pos = js
	while True:
		new_target = targets.pop(0)
		if not isinstance(pos, dict):
			break
		if new_target in pos and len(targets) > 0:
			# descend
			pos = pos[new_target]
		elif new_target in pos:
			# delete terminal target
			changed = True
			del(pos[new_target])
		else:
			# target not found
			break
		if 0 == len(targets):
			# target not found
			break

	if changed:
		from bleachbit.Options import options
		if options.get('shred'):
			delete(path, True)
		# write file
		json.dump(js, open(path, 'w')) 





"""

# some JSON:
x =  '{ "control":{"unite":"1","dateCreation":"2022-05-01_00-46-49"},"name":"John", "age":30, "city":"New York"}'
z = "../Collecteur/json_files/Unity1_2022-05-01_00-46-29.json"

w="test.json"


clean_json(z,w)

print(w)

ww = open(w,'r')

yy = json.load(w)
print(w)



y = json.loads(x)
print(x)


yy = json.loads(open(z,'r').read())
yy = json.dumps(yy, indent = 0)
# the result is a Python dictionary:
print(yy)
"""


