import csv

class Password:
    
    """
    A Password Generator Class
    """
    
    def __init__(self) -> None:
        
        with open("config.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.params = {
                    "capitals": bool(row["capitals"]),
                    "digits": bool(row["digits"]),
                    "chars": bool(row["chars"]),
                    "length": int(row["length"]),
                }
    
        self.text = ""
    
    
    def config(self) -> None:
        
        """
        Configures the generation process
        """
        
        # Config the password generation
        print("""
              Let's configure your password generation!
              Should your password contain...
              """)
        
        # Whether it has capital letters
        self.params["capitals"] = self.__handle_input("Capital letters? ")
        # Whether it has digits
        self.params["digits"] = self.__handle_input("Digits? ")
        # Whether it has characters
        self.params["chars"] = self.__handle_input("Characters? ")
        # Its Length
        try:
            self.params["length"] = int(input("What about its length?: "))
        except ValueError:
            print(f"I'll just take the default ({self.params['length']}) then -__-")
        
        
    def generate(self) -> str:
        """
        Generates a password consisting of randomly selected letters
        with the given config settings

        Returns:
            str: Returns the generated password
        """
        
        # imports
        from random import randrange
        
        # letter/char pool using the config settings
        pool = ""
        
        if self.params["capitals"]:
            from string import ascii_letters as letters
        else:
            from string import ascii_lowercase as letters
            
        pool += letters
        
        if self.params["digits"]:
            from string import digits
            pool += digits
        
        if self.params["chars"]:
            pool += "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        
        # generate the password
        self.text = ''.join(pool[randrange(0, len(pool))] for _ in range(self.params["length"]))
        
        return self.text
    
    
    def save_config(self) -> None:
        with open("config.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.params.keys())
            writer.writeheader()
            writer.writerow(self.params)
      
        
    @staticmethod
    def __handle_input(text: str) -> bool:
        """
        Handles the user input to behave accordingly
        """
        
        # Get user input
        inp = input(text).lower()
        
        # the answer must be a Yes or No, 
        # any other invalid answer results in No
        return inp == "y" or inp == "yes"
    