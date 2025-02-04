def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly)
    from a_class, otherwise returns False.

    :param obj: The object to check
    :param a_class: The class to compare against
    :return: Boolean
    """

    obj_type = type(obj)

    if obj_type is a_class:
        return False

    return a_class in obj_type.__mro__
