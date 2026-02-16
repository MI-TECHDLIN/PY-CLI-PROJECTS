import re
# datemodifier
txt='11-2-2008'

kir=re.match('\d{2}+',txt,)
print(kir.group())

txt='today is 23/02/2019.'\
'yesterday was 22/02/2019.'\
'januaru was 24/02/2019.'

p=re.compile('(\d{2})\/(\d{2})\/(\d{4})')
pE=p.sub(r'\3.\2.\1\n',txt)
print(pE)

# capturing groups
txt='Ezechukwu Miracle'

pattern=re.compile('(?P<First>\w+) (?P<Last>\w+)')
m=pattern.match(txt)
print(m.groupdict())

# non capturring groups
txt='i love cats ' \
'i love dogs' 

me=re.findall('i love (?:cats|dogs)',txt)
print(me)

# look ahead

article= "Discipline is one of the most powerful qualities a person can develop in life. Discipline is the foundation of success in academics, career, and personal growth. Without discipline, talent often remains unused. With discipline, even average ability can produce extraordinary results. Discipline teaches us how to control our thoughts and actions. Discipline helps students wake up early to study. Discipline keeps athletes training even when they feel tired. Discipline pushes entrepreneurs to work on their goals consistently. Discipline builds habits that shape our future. When you practice discipline, you learn to delay gratification. Discipline allows you to choose long-term success over short-term pleasure. Through discipline, distractions lose their power over you. Discipline strengthens your focus in a world full of noise. Every great achievement begins with discipline. Discipline is not about punishment; it is about self-control. True discipline comes from within, not from external pressure. Parents teach discipline to prepare children for responsibility. Schools promote discipline to create order and respect. Society depends on discipline to function smoothly. Financial stability requires discipline in spending and saving. Physical fitness demands discipline in exercise and diet. Emotional maturity grows through discipline in managing reactions. Spiritual growth also involves discipline in reflection and practice. Time management becomes effective with discipline. Discipline transforms dreams into achievable goals. Without discipline, motivation fades quickly. With discipline, progress continues even when motivation disappears. Discipline builds resilience during tough times. People who practice discipline rarely give up easily. Leadership requires strong discipline. A leader without discipline struggles to inspire others. Team success often reflects collective discipline. Nations develop faster when citizens value discipline. History shows that discipline has shaped civilizations. Personal growth depends on daily discipline. Small acts of discipline compound into major achievements. Reading regularly requires discipline. Learning new skills demands consistent discipline. Mastery is impossible without discipline. Social media can test your discipline. Technology becomes productive only when guided by discipline. Academic excellence thrives on steady discipline. Career advancement rewards professional discipline. Healthy relationships benefit from emotional discipline. Developing discipline takes patience. Every time you resist temptation, you strengthen your discipline. Failures can teach valuable lessons about discipline. Setting clear goals improves your discipline. Daily routines encourage structured discipline. Self-respect grows with discipline. Confidence increases when discipline produces results. Freedom actually expands through discipline. The more discipline you practice, the more control you gain. Success stories often highlight the role of discipline. Ultimately, discipline is the bridge between goals and accomplishment. Discipline is the quiet force behind every meaningful success. If you commit to building discipline, you build the power to shape your destiny."


f=re.finditer(r'\bdiscipline\b',article)
print(f)

# lookahead
txt='i love pyton , i love regex'
p=re.search('love(?=\sregex)',txt)
print(p)

# lnegative ookahead
txt='i love pyton , i love regex'
p=re.search('love(?!\sregex)',txt)
print(p)

# lookbehind
txt='love regex or hate regex, cant ignore regex'

f=re.search('(?<!(love|hate)\s)regex',txt)
print(f)