calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info (string):
    string1 = string.upper()
    string2 = string.lower()
    info = len(string), string1, string2
    count_calls()
    return info


def is_contains(string, list_to_search):
    count_calls()
    const = False
    for i in list_to_search:
        if string.upper() == i.upper():
            const = True
            continue
    return const

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)