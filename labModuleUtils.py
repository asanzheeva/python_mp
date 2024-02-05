
def show_numbers(n: int):
    print(*range(n))

def show_words(word: str, n: int):
    print(*[f"{word} {i}" for i in range(n)], sep='\n')

    show_numbers(5)
    show_words("Привет, 5")