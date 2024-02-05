# Модуль - это любой программный код на питоне, т.е любой файл с расширением *.py


print(f"Start -> {__name__}")

# # (1)
# import labModuleUtils

# if __name__ == "__main__":
#     labModuleUtils.show_numbers(10)
#     labModuleUtils.show_words("Hi", 4)

# print(f"End -> {__name__}")

# (2)
from labModuleUtils import show_numbers
if __name__ == "__main__":
    show_numbers(8)

print(f"End -> {__name__}")