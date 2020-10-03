from pprint import pprint


class Stu(object):
    pass


class Stu():
    a=1
    def xxx(self):
        pass
    print(dir(Stu))
    X=Stu()
    print(dir(X))