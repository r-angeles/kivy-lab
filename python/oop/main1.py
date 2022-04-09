class Dog:

    def __init__(self, name: str, num_tricks=0):
        assert num_tricks >= 0

        self.name = name
        self.num_tricks = num_tricks

    @classmethod
    def get_input(self):
        while True:
            try:
                name = input('Enter a dog\'s name: ')
                num_tricks = int(input('Enter how many tricks it can learn: '))
                return self(name, num_tricks)
            except:
                print('Invalid input')
                continue




def main():
    dog1 = Dog.get_input()
    print(dog1)

main()

# if __name__ == '__main.py__':
#     main()
