# jabber = open('Jabberwocky.txt', 'r')
#
# for i in jabber:
#     print(i, end=' ')
#
# jabber.close()

with open('Jabberwocky.txt', encoding = 'utf-8') as jabber:
    for lines in jabber:
        print(lines.rstrip())
    

