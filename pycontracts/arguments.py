
class Arguments(object):
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

        self.__unify_args()
        self.__unify_kwargs()

    def __unify_args(self):
        for idx, value in enumerate(self.__args):
            setattr(self, "arg_{}".format(idx), value)

    def __unify_kwargs(self):
        for name, value in self.__kwargs.items():
            print(type(name))
            setattr(self, name, value)
