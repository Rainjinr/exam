def get_pal():
    pal = input()
    return pal.lower() == pal.lower()[::-1]
print(get_pal())
