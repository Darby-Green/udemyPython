morning = ['java', 'C', 'ruby', 'lisp', 'C#']
afternoon = ['python', 'C#', 'java', 'C', 'ruby']

possibleCourses = set(morning).symmetric_difference(afternoon)
print(possibleCourses)

