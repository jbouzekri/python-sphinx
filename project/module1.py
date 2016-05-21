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
        """
        nothing different than function description

        You can make a link to official python doc :

        * for a module :mod:`unittest.mock`
        * for a class :class:`unittest.mock.MagicMock`
        * for a function :func:`unittest.mock.patch`

        All cross reference `here <http://www.sphinx-doc.org/en/stable/domains.html#cross-referencing-python-objects>`_

        Reference external documentation :class:`flask_restful.Api`

        Reference local method :

        * in same file :func:`MyClass.my_method`
        * in other file :func:`project.package1.pmodule1.AnotherClass.another_method`
        * rename :func:`my text <project.package1.pmodule1.AnotherClass.another_method>`

        Sphinx code :

        * `:mod:`<full mod name>``
        * `:class:`<full class name>``
        * `:func:`<full func name>``
        """
        return param1

    @staticmethod
    def my_static_method():
        """
        ``.. note:: text``

        .. note:: can be useful to emphasize important feature

        ``.. seealso:: text``

        .. seealso:: :class:`MyClass.my_method` you can reference another method

        ``.. warning:: text``

        .. warning:: You can emphasize a constraint on an argument

        ``.. todo:: text``

        .. todo:: check that arg2 is non zero.
        """
        return True

    def other_method(self):
        """
        You can put code inside docstring::

            class MyEmbeddedCode(object):
                pass

        >>> import template
        >>> a = template.MainClass1()
        >>> a.function1(1,1,1)
        2
        """
        pass