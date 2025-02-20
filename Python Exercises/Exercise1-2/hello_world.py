class Program:
    """Example class"""

    def run(self) -> str:
        return 'Hello Master!!'


# We are using python's "__name__" property to our advantage:
# When executing this file directly, its "python name" is "__main__" because it is the main entry point.
# When importing this file from another, its name will be "hello_world" or the name of the .py file
# and the main function will not be executed while the functions and vars are imported in the interpreter.

if __name__ == "__main__":
    program: Program = Program()
    print (program.run())
