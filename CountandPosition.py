text = input('Enter whatever phrase you want: ')

print('The amount of As on this phrase is: {}'.format(text.lower().count('a')))
print('The position of the first A on the text is: {}'.format(text.lower().find('a') + 1))
print('The position of the last A on the text is: {}'.format(text.lower().rfind('a') + 1))