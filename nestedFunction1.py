def greetPythons(items: list) -> None:
    greeting = 'Hello'

    def makeGreeting(item: str) -> str:
        greeting = 'Hi'
        return f'{greeting} {item}'

    for item in items:
        print(makeGreeting(item))
    print(f"Inside greetPythons, 'greeting' is {greeting}")


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greetPythons(names)