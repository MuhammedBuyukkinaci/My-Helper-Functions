def hello(name = None):
    if name is None:
        return "Hello Stranger"
    else:
        return f"Hello {name}"
