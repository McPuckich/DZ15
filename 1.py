st = 'I am learning Python. hello, WORLD!'
print(st)
st = st[:st.find('h')] + st[st.rfind('h') + 1:]
print(st)