import re

p = re.compile(r"abc")
m = p.match('abcdef')
print m.group()

#.除换行符以外
p = re.compile(".")
m1 = p.match("aga")
print m.group()
#m2= p.match("\n")
#print m2.group()

m3 = p.findall("agb.dfre.fdfe")
print m3

#字符集合
p = re.compile('[abc]')
m = p.findall('abcdef')
print type(m)
print m
m1 = p.match('abcdef')
print m1.group()


#数量词
p = re.compile('[abc]*')
print p.findall('abcdasga')

p = re.compile('[abc]+')
print p.findall('abcdef') #贪婪模式

p = re.compile('[abc]*?') #非贪婪模式
print p.findall('abcdef')

p = re.compile('[abc]+?') #非贪婪模式
print p.findall('abdasf')

p = re.compile('[abc]{2}')
print p.findall('abcabc')

p = re.compile('[abc]{2,3}')
print p.findall('abcabcabc')

p = re.compile('[abc]{2.3}?')
print p.findall('abcabcabc')


#边界
p = re.compile('^[abc]*')
print p.findall('abcdef')
print p.findall('bcdef')
print p.findall('def')
print p.findall('defavc')

p = re.compile('[abc]*')
print p.findall('aggbecabcdef')
m = p.match('abdegae')
print m.group()

p = re.compile('[^abc]*')
print p.findall('abddfeg')

p = re.compile('^[abc]*e$')
print p.findall('abcd')
print p.findall('abcde')
print p.findall('abce')

p = re.compile('(a)(b)(c)') #元组匹配
m = p.match('abcdef')
print m.group()
print type(m.group())
print m.groups()
print type(m.groups())

m = p.match('abdeg')
#print m.groups()

p = re.compile('(a)b(c)') #匹配分组，匹配子串
m = p.match('abcdef')
print m.groups()
m = p.match('adcfa')
#print m.groups()

p = re.compile('(?P<name>a)b(c)')
m= p.match('abcdef')
print m.groups()
print m.groupdict()

p = re.compile('(?P<name>a)b(c)(?P=name)')
print p.findall('abcd')
print p.findall('abca')

p = re.compile(r'(?P<name>a)b(c)(?P=name)\1')
print p.findall('abcaa')
print p.findall('abcac')

p = re.compile(r'(?P<name>a)b(c)(?P=name)\2')
print p.findall('abcac')
m = p.match('abcac')
print m.group()
print m.groups()
print m.groupdict()
print m.group(1)
print m.group(2)


#特殊构造
p = re.compile(r'(?:abc){2}')
print p.findall('abc')
print p.findall('abcabc')
print p.findall('abcabcabcabc')
m= p.match('abcabcabcabc')
print m.groups()

p = re.compile(r'a(?=\d)')
print p.findall('a1a2a3')
p  = re.compile(r'\w(?=\d)')
print p.findall('word1 wor2 wo3')
p = re.compile(r'\w+(?=\d)')
print p.findall('word1 wor2 wo3')

p =re.compile(r'a(?!\d)')
print p.findall('word1 wora2')
print p.findall('worad fjka2')

p = re.compile(r'(?<=\d)a')
print p.findall('word1 wora2 aw3a')

p = re.compile(r'(?<!\d)a')
print p.findall('word1 wora2 aw3a')

p = re.compile(r'(\d)?abc(?(1)\d|abc)')
print p.findall('1abc4')
m = p.match('1abc3')
print m.group()
m = p.match('1abcabc')
#print m.group()
m = p.match('abcabc')
print m.group()

p = re.compile(r'(?i)abc')
print p.findall('Abc')

p = re.compile(r'abc',re.I)
print p.findall('aBc')

p = re.compile(r'-')
s = p.split("a-bd-ddd-asga-fewg-ge")
print s

p = re.compile('a')
m = p.finditer('abcaadfaaa') #迭代器
print m
print m.next()

p = re.compile(r'(\w+) (\w+)')
s = "hi you,good boy"
print p.sub(r' \2 \1',s) #位置替换