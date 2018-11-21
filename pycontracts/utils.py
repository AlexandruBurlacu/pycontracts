def check_any(args_dict, predicate_func):
    """
    Used to check if the predicate function returns true for at least one of the arguments.
    """
    for arg in args_dict.values():
        if predicate_func(arg):
            return True
    
    return False

def check_all(args_dict, predicate_func):
    """
    Used to check if the predicate function returns true for all of the arguments.
    """
    for arg in args_dict.values():
        if not predicate_func(arg):
            return False
    
    return True

def drop_fst_arg(args_dict):
    """
    Convinient function to drop the first argument, for example when applying
    a contract to class methods and you don't need the ``self`` argument.
    """
    if "arg__0" in args_dict:
        del args_dict["arg__0"]
    return args_dict

def drop_args(args_dict, args_list):
    """
    Convinient function to drop the unnecessary arguments.
    """
    for arg in args_list:
        if arg in args_dict:
            del args_dict[arg]

    return args_dict
