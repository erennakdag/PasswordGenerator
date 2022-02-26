from sys import argv
from password import Password


psw = Password()


def main():
    
    
    if len(argv) == 1:
        print(f"Your new password: {generate_with_defaults()}")
        
    elif len(argv) >= 2:
        
        # lowering all letters for good measure
        curr = argv[1].lower()
        
        # checking for the right command line argument
        if curr == "config" or curr == "-c" or curr == "c":
            print(f"Your new password: {generate_with_config()}")
        else:
            raise Exception(f"Unknown command-line argument ‘{argv[1]}‘")
        
        # checking if the user wants to save the current configuration
        try:
            save = argv[2].lower()
            if save == "-s" or save == "save":
                psw.save_config()
            else:
                raise Exception(f"Unknown command-line argument ‘{argv[2]}‘")
        except IndexError:
            pass
        
    else:
        raise Exception(f"Not enough or too many arguments. Your argument count was {len(argv)}")


def generate_with_defaults() -> str:
    """
    Generates the password without configuring the params

    Returns:
        str: The Password
    """
    
    return psw.generate()


def generate_with_config() -> str:
    """
    Configures the class params and generates the password
    
    Returns:
        str: The Password
    """

    psw.config()
    return psw.generate()


if __name__ == "__main__":
    main()
    