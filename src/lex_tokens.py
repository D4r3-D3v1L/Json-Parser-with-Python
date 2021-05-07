def string(s):
	tmp = ''
	if s[0] == '"':
		s = s[1:] 
	else:
		return None,s
	for i in s:
		if i == '"':
			return tmp,s[len(tmp)+1:]
		else:
			tmp += i
	raise Exception("Needed End Quote")

def number(s):
	num_arr = ['1','2','3','4','5','6','7','8','9','10','0','e','-','.']
	tmp_num = ''
	for i in s:
		if i in num_arr:
			tmp_num += i
		else:
			break
	if '.' in tmp_num:
		return float(tmp_num),s[len(tmp_num):]
	if len(tmp_num) == 0:
		return None,s
	return int(tmp_num),s[len(tmp_num):]

def check_bool(s):
	if s == 'true':
		return True,s[4:]
	elif s == 'false':
		return False,s[5:]
	else:
		return None,s
def null_check(s):
	if s == 'null':
		return True,s[4:]
	return None,s

def space_check(s):
	white_list = [' ','\t','\n','\r']
	if s[0] in white_list:
		return True,s[1:]
	else:
		return None,s

def symbol_check(s):
	symbols = [',','[',']','{','}',':']
	if s[0] in symbols:
		return s[0],s[1:]
	else:
		return None,s

def tokenize(s):
	token_list = []
	while len(s)!=0:
		_string, s = string(s)
		if _string != None:
			token_list.append(_string)
			continue
		_number,s = number(s)
		if _number != None:
			token_list.append(_number)
			continue
		_bool, s = check_bool(s)
		if _bool != None:
			token_list.append(_bool)
			continue
		_null,s = null_check(s)
		if _null:
			token_list.append(None)
			continue
		_space,s = space_check(s)
		if _space:
			continue
		_symbol,s = symbol_check(s)
		if _symbol != None:
			token_list.append(_symbol)
			continue
		
		raise Exception("Invalid Character " + s)	
	return token_list

# a='{"value": "New", "onclick": "CreateDoc()"}'
# print(tokenize(a))



