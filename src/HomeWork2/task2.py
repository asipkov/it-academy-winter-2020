# 2. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
predl = 'Найти самое... длинное слово, в введенном: предложении.'
result = ''
e = [",", ".", ";", ":", "...", "!", "?", "-", '"', "(", ")"]
for i in range(len(e)):
    predl = predl.replace(e[i], "")
print(predl)
for word in predl.split():
    if len(word) > len(result):
        result = word
print('Самое длинное слово в предложении: ' + result)
