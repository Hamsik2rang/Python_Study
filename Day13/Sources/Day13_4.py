files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda s: True if '.jpg' in s or '.png' in s else None, files)))

# In Lambda function, If condition must be used with else, but cannot use elif.
# if you want to use multiple if condition un lambda, u can use like this:
#   lambda [x] : if condition_1 else expression if condition_2 else expression if condition3 else ....


print(list(filter(lambda s: s.find('.jpg') != -1 or s.find('.png') != -1, files)))

