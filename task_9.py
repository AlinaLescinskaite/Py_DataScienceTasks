
def greeting(function):
    def wrapper(*args, **kwargs):
        # print(args)
        return f'Merry Christmas, {function(*args, **kwargs)}'
    return wrapper


@greeting
def kiss():
    return ":*"


@greeting
def personalization(name):
    return f'dear {name}'


if __name__ == '__main__':

    # decorated_kiss_function = greeting(kiss)
    # print(kiss())
    # print(decorated_kiss_function())
    #
    # decorated_personalization_function = greeting(personalization)
    # print(personalization("John"))
    # print(decorated_personalization_function("John"))

    print(kiss())
    print(personalization(name="John"))