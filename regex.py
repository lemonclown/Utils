import re

c_comment_regex = r'(\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/)|(\/\/.*)'

def remove_comment(line):
	removed_line = re.sub(c_comment_regex, " ", line)
	return removed_line