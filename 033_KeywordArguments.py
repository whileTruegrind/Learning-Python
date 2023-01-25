# Keyword Arguments
    ## An argument preceded by an identifier
    ## Helps with readability
    ## Order of arguments doesn't matter

def hello(greeting, title, name):
    print(f"{greeting} {title}{name}")

hello(greeting = "Hello", title = "Mr.", name = "Rishi")