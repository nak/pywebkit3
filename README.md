pywebkit3
=========

bindings for gtk, gdk and pywebkit3 classes in pure python

pywebkit3 is a project borne out of frustration with the current gtk and 
pywebkit bindings.  These bindings suffer several shortcomings:
(1) They require special compilation of native code, a difficult feat to 
have happen across multiple platforms
(2) They are behind the latest versions and cannot take advantage of many 
web html developments
(3) They are not available as simple easy_install or pip scripts
(4) They have incomplete APIs

And it hit me that there is a much easier way to do this. The Gtk and PyWebKitGtk 
interfaces are out there on the web in easy-to-parse C-haeader style code.
This is the beuaty of Gtk!  Using ctypes it should, in principle, be able 
to write a parser in python to convert this API into a python class-based
API form the latest C APIs and enjoy the use of more modern technologies!

With that, the project begins.  And it is a race to get the html APIs 
pushed copy and pasted into interface definition files for conversion.  The
rest should be an automated and joyous process ;-).


-John Rusnak
