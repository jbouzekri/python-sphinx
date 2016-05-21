static page example
*******************

Introduction
============

This page is a static page linked from the home page.
It displays a lot of the syntax of restructuredText.

For the most part, it is a copy/paste from `an example pypi project <https://pythonhosted.org/an_example_pypi_project/sphinx.html>`_

This covers just a few of the many many commands available via sphinx. For more, visit http://sphinx.pocoo.org/.

Also, another great site with just an overview of more common commands is http://docs.geoserver.org/trunk/en/docguide/sphinx.html.

Resources
=========

Sphinx is built of reStructured text and, when using sphinx most of what you type is reStructured text.  Some great resources are below 
(and most examples are ripped out of these pages): 

* http://docutils.sourceforge.net/rst.html
* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt

Bold/Italics
============

Bold and italics are done like this::

    **bold** and *italics*
    
which render like **bold** and *italics*.



Lists 
=====

You can do::
 
   * A thing. 
   * Another thing. 
   
   or
   
   1. Item 1. 
   2. Item 2.
   3. Item 3.
   
   or 
   
   - Some. 
   - Thing.
   - Different. 

which render as:

* A thing. 
* Another thing. 
   
or
   
1. Item 1. 
2. Item 2.
3. Item 3.
   
or 
   
- Some. 
- Thing.
- Different. 





Headers
=======

It's up to you to pick a convention for headers and just stick with it -- 
Sphinx will pick up on your convention: 

You can do whatever header stragetgy you want, but I think a good one is:: 

	H1 -- Top of Page Header
	************************
	There should only be one of these per page and this will also -- when 
	converting to pdf -- be used for the chapters. 
	
	H2 -- Page Sections
	===================
	
	H3 -- Subsection
	----------------
		
	H4 -- Subsubsection
	+++++++++++++++++++

So::
  
     A Subpoint
     ----------
     This is my idea. 
     
     A subsubpoint
     +++++++++++++
     This is a smaller idea. 
    

Is rendered like this:

A Subpoint
----------
This is my idea. 
 
A subsubpoint
+++++++++++++
This is a smaller idea. 





Tables
======

Basic tables are done like this::

	COMPLEX TABLE:
	
	+------------+------------+-----------+
	| Header 1   | Header 2   | Header 3  |
	+============+============+===========+
	| body row 1 | column 2   | column 3  |
	+------------+------------+-----------+
	| body row 2 | Cells may span columns.|
	+------------+------------+-----------+
	| body row 3 | Cells may  | - Cells   |
	+------------+ span rows. | - contain |
	| body row 4 |            | - blocks. |
	+------------+------------+-----------+

	SIMPLE TABLE:
		
	=====  =====  ======
	   Inputs     Output
	------------  ------
	  A      B    A or B
	=====  =====  ======
	False  False  False
	True   False  True
	False  True   True
	True   True   True
	=====  =====  ======

Which render like this:

.. only:: html 

	COMPLEX TABLE:
	
	+------------+------------+-----------+
	| Header 1   | Header 2   | Header 3  |
	+============+============+===========+
	| body row 1 | column 2   | column 3  |
	+------------+------------+-----------+
	| body row 2 | Cells may span columns.|
	+------------+------------+-----------+
	| body row 3 | Cells may  | - Cells   |
	+------------+ span rows. | - contain |
	| body row 4 |            | - blocks. |
	+------------+------------+-----------+
	
	SIMPLE TABLE:
		
	=====  =====  ======
	   Inputs     Output
	------------  ------
	  A      B    A or B
	=====  =====  ======
	False  False  False
	True   False  True
	False  True   True
	True   True   True
	=====  =====  ======





Links
=====

Urls are automatically linked, like http://packages.python.org/an_example_pypi_project/

For other links, you basically use the ``_`` operator. 

To add a text with a hyperlink, I like using this format::

	`Docs for this project <http://packages.python.org/an_example_pypi_project/>`_

which renders as `Docs for this project <http://packages.python.org/an_example_pypi_project/>`_.

To create an anchor link that jumps to another section in the 
same .rst file, use this syntax::

	`Table of Contents`_
	
Which renders like this: `Table of Contents`_






Images
======

Images syntax is like this::

	.. figure::  http://placekitten.com/300/200
	   :align:   center
	   
	   Proof that getting rich is mostly luck. 

Which renders like this:

.. figure::  http://placekitten.com/300/200
   :align:   center
   
   Proof that getting rich is mostly luck. 


You can also add an anchor point for an image like this::

	.. _is_sweaty:
	.. figure::  http://placekitten.com/300/200
	   :align:   center
	   
	   Proof that getting rich is mostly luck. 

Which renders like this:

.. _is_sweaty:
.. figure::  http://placekitten.com/300/200
   :align:   center
   
   Proof that getting rich is mostly luck. 
   
Now you can reference this anchor like this::

    This picture is_sweaty_.
    
which renders like this:
   
This picture is_sweaty_.






Documents
=========

To download documents you use the syntax::

	 :download:`An Example Pypi Project<docs/examplepypi.pdf>`
	 
which renders like :download:`An Example Pypi Project<docs/examplepypi.pdf>`.
	 






Substitutions
=============

Substitutions syntax is ::
	
	.. |biohazard| image:: http://placekitten.com/300/200 

	The |biohazard| symbol must be used on containers used to dispose of medical waste.
	
	
Or if you want to do a literal text replacement use::
	
	.. |doctest| replace:: :mod:`doctest`
	
	I really like |doctest|.

Which renders like this: 
	
.. |biohazard| image:: http://placekitten.com/300/200 

The |biohazard| symbol must be used on containers used to dispose of medical waste.

.. |doctest| replace:: :mod:`doctest`

I really like |doctest|.

.. note::

   Substitutions are really useful, especially when put into a ``global.rst``
   and included at the top of every file.  See Includes_ below for more. 








Includes
========

The syntax::

   .. include myfile.rst
   
Will 'inline' the given file.  A common convention I use is create a global
.rst file called ``global.rst`` and include that at the top of every page.  
Very useful for links to common images or common files links, etc.










Table of Contents
=================

Using the syntax::

	.. toctree::
	   :maxdepth: 2
	   
	   setuptools
	   buildanduploadsphinx
	   
renders like this:

.. toctree::
   :maxdepth: 2
   
   setuptools
   uploadsphinx

where ``setuptools``, ``sphinx``, etc. correspond to ``setuptools.rst`` and 
``sphinx.rst`` files in the local path. 






Paragraph Markup
================

To bring attention to a section of text, use paragraphs level markups. 

Important constructs include::

	.. note::
	
	.. warning::
	
	.. versionadded:: version

	.. versionchanged:: version
    
	.. seealso::	

The way you would use this is as follows::

   This is a statement. 
   
   .. warning:: 
    
      Never, ever, use this code!
      
   .. versionadded:: 0.0.1
   
   It's okay to use this code. 

Which would render like this:

This is a statement. 

.. warning:: 
    
   Never, ever, use this code!
      
.. versionadded:: 0.0.1

Now it is okay to use this code. 

	
For full Sphinx docs on paragraph markup, check out 
http://sphinx.pocoo.org/markup/para.html.






Code
====

Python code in sphinx is easy.  Because we turned :mod:`pygments` on, all we 
need to do is use the ``::`` operator at the end of a line.  So::

    Here is something I want to talk about::
    	
    	def my_fn(foo, bar=True):
    	    """A really useful function.
    	    
    	    Returns None
    	    """
    	    
Renders like this:
    	    
Here is something I want to talk about::
	
	def my_fn(foo, bar=True):
	    """A really useful function.
	    
	    Returns None
	    """
    
Also, you can add "inline" code by using the fixed-font operator.  

By using two `````` marks like this::

    This is inline ``if __name__ == '__main__':``
    
you get:

This is inline ``if __name__ == '__main__':``







Python Cross Referencing Syntax
===============================

Sphinx makes it easy to quickly link to other code definitions that 
*are in the python path* or can be found by :mod:`intersphinx`. 

The major ones I use all the time are:

* ``:mod:``

* ``:func:``

* ``:class:``

Which is used like this::

   I really like the :mod:`threading` module which has the 
   :class:`threading.Thread` class. 
   
   Here is a link :func:`time.time`.

which renders like this:

I really like the :mod:`threading` module which has the 
:class:`threading.Thread` class. 
   
Here is a link :func:`time.time`.

For more, visit http://sphinx.pocoo.org/markup/inline.html.








'Auto' Directives
=================

From the sphinx docs directly:

:mod:`sphinx.ext.autodoc` -- Include documentation from docstrings

This extension can import the modules you are documenting, and pull in
documentation from docstrings in a semi-automatic way.

.. note::

   For Sphinx (actually, the Python interpreter that executes Sphinx) to find
   your module, it must be importable.  That means that the module or the
   package must be in one of the directories on :data:`sys.path` -- adapt your
   :data:`sys.path` in the configuration file accordingly.

For this to work, the docstrings must of course be written in correct
reStructuredText.  You can then use all of the usual Sphinx markup in the
docstrings, and it will end up correctly in the documentation.  Together with
hand-written documentation, this technique eases the pain of having to maintain
two locations for documentation, while at the same time avoiding
auto-generated-looking pure API documentation.

For more on autodoc see http://sphinx.pocoo.org/ext/autodoc.html.

The main autodoc features I use are:

*  ``.. automodule:: <module_name>``
*  ``.. autoclass:: <class_name>`` and
*  ``.. autofunction:: <function_name>``

The key to using these features is the ``:members:`` attribute.  If: 

*  You don't include it at all, only the docstring for the object is brought in:
*  You just use ``:members:`` with no arguments, then all public functions, 
   classes, and methods are brought it that have docstring. 
*  If you explictly list the members like ``:members: fn0, class0, _fn1`` 
   those explict members are brought.  






Function Definitions
====================

The sphinx syntax (taken from http://sphinx.pocoo.org/markup/desc.html) looks like this::

	.. function:: format_exception(etype, value, tb[, limit=None])
	
	   Format the exception with a traceback.
	
	   :param etype: exception type
	   :param value: exception value
	   :param tb: traceback object
	   :param limit: maximum number of stack frames to show
	   :type limit: integer or None
	   :rtype: list of strings

which renders like this:

.. function:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings

