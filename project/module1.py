# -*- coding: utf-8 -*-

"""
This is the top comment of the module.  
"""

#: Comment for a module constant
MY_GLOBAL_VARIABLE='has a value'


def my_function():
    """ this function does nothing """
    pass


def div(a, b):
    """    
    description of a function with params
    
    sphinx code::
    
            :param int a: first param description (type defined in same comment line)
            :param b: second param description (type defined in next comment line)
            :type b: int
            :return: the description of the return value
            :rtype: int
            :raises ValueError: if b is 0 Describe what triggers the exception 
       
    :param int a: first param description (type defined in same comment line)
    :param b: second param description (type defined in next comment line)
    :type b: int
    :return: the description of the return value
    :rtype: int
    :raises ValueError: if b is 0 Describe what triggers the exception
    """
    if b == 0:
        raise ValueError('zero division error')
    return a / b


class MyClass(object):
    """
    You can describe what the class does.
    
    :param int a: constructor param description
    """
    
    #: Class constant description
    CLASS_CONSTANT = "my class constant"
    
    def __init__(self, a):
        self.a = a
        
    def my_method(self, param1):
        return param1
    
    @staticmethod    
    def my_static_method():
        """
        ``.. note:: text``
        
        .. note:: can be useful to emphasize important feature
            
        ``.. seealso:: text``
        
        .. seealso:: :class:`MyClass2.my_static_method` you can reference another method in the same file 
            or in a different file :class:`project.package1.pmodule1.AnotherClass.another_method`
            if text too long overwrite : :class:`my text <project.package1.pmodule1.AnotherClass.another_method>`
        
        ``.. warning:: text``
        
        .. warning:: You can emphasize a constraint on an argument
        
        ``.. todo:: text``
        
        .. todo:: check that arg2 is non zero.
        """
        return True


class MyClass2(object):  
    @staticmethod    
    def my_static_method():
        return True