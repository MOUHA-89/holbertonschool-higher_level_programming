def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly or indirectly)
    from a_class, otherwise returns False.
    
    :param obj: The object to check
    :param a_class: The class to compare against
    :return: Boolean
    """
    # Get the type of the object
    obj_type = type(obj)
    
    # Check if the object's type is exactly the same as a_class
    if obj_type is a_class:
        return False
    
    # Check if a_class is in the object type's method resolution order
    return a_class in obj_type.__mro__
