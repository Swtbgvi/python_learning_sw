class SelfLearning:
    # constructor, means putting all default values in it
    # executes at the first while calling the class
    def __init__(self):
        self.name = "swetha"
        self.name1 = "swetha test"

    def weekday(self):

        return self.name

if __name__ == '__main__':
    # SelfLearning() is a class
    # sf is an object created from the class
    sf = SelfLearning()
    print(sf.name1)
    print(sf.weekday())


