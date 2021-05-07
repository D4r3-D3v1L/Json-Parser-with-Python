def array_check(token_list):
	res_arr = []
	if token_list[0] == ']':
		return res_arr,token_list[1:]
	while len(token_list):
		token , token_list = parsing(token_list)
		res_arr.append(token)

		if token_list[0] == ']':
			return res_arr,token_list[1:]
		elif token_list[0] != ',':
			raise Exception("Comma Expected")
		else:
			token_list =token_list[1:]
	raise Exception("End bracket not found")

def object_check(token_list):
	res_obj = {}
	if token_list[0] == '}':
		return res_obj,token_list[1:]
	while len(token_list):
		key = token_list[0]
		if type(token_list[0]) == str :
			token_list = token_list[1:]
		else:
			raise Exception("String Needed")
		if token_list[0] != ':':
			raise Exception("Semicolon Missing")
		token , token_list = parsing(token_list[1:])
		res_obj[key] = token
		# print(res_obj,token_list)
		# print(token_list[0])
		if token_list[0] == '}':
			return res_obj,token_list[1:]
		elif token_list[0] != ',':
			raise Exception("Comma Expected")
		else:
			token_list = token_list[1:]

	raise Exception("End Flower Bracket not found")

def parsing(token_list):
	if token_list[0] == '[':
		return array_check(token_list[1:])
	elif token_list[0] == '{':
		return object_check(token_list[1:])
	else:
		return token_list[0],token_list[1:]

# t = ['{', 'value', ':', 'New', ',', 'onclick', ':', 'CreateDoc()', '}']
# a = parsing(t)[0]
# print(a.keys())
