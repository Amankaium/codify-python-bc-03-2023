def example(n):
    print(n, "This is sample function")
    if n < 500:
        example(n+1)
    else:
        return "END"


example(1)
