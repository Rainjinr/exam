# https://github.com/Rainjinr/exam.git

def get_card_number(number=input()):
    return (number.replace(number[:-4], "*" * len(number[:-4])))


print(get_card_number())
