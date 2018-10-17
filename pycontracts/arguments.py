from copy import deepcopy

class Arguments(object):
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

        self.__unify_args()
        self.__unify_kwargs()

        self.all_args = deepcopy(self.__dict__)
        print(self.all_args)

    def __unify_args(self):
        for idx, value in enumerate(self.__args):
            setattr(self, "arg__{}".format(idx), value)
        
        del self.__args

    def __unify_kwargs(self):
        for name, value in self.__kwargs.items():
            setattr(self, name, value)

        del self.__kwargs
