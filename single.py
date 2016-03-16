class Foo:
    _instance_ = None

    @staticmethod
    def GetInstance():
        """
        method_1
        This is the manual implementation of the singleton pattern
        It's a java like implementation
        :return:
        """
        if Foo._instance_ is None:
            Foo._instance_ = Foo()
        return Foo._instance_


def make_it_singelton(c):
    """
    method2 - function decorator
    :param c: The class to warp, this decorator receives wrap it with the function
     "get_instance" (which adds to it the singleton feature) and then returns the function.
    :return: get_instance wrapar
    """
    instance = {}

    def get_instance(*args, **kwargs):
        if len(instance) == 0:
            instance[c] = c(*args, **kwargs)
        return instance[c]

    return get_instance


class MakeItSingelton:
    """
        method3 - Class decorator
        This class warps a given class and give it singleton features
    """

    def __init__(self, c):
        self.c = c
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.c(*args, **kwargs)
        return self.c

