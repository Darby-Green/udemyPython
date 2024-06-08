from typing import Set

requiredSkills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'}
}

interviewees = set()

for candidate, skills in candidates.items():
    # if skills.issuperset(requiredSkills):
    if skills > set(requiredSkills):  #performance issues with this
        interviewees.add(candidate)

print(interviewees)