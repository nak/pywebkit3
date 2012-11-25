IF_FILES=$(wildcard *.if)

all:
	echo ""> pywebkit3/gobject.py
	echo "from webkit_types import *"> pywebkit3/webkit3.py
	echo "from gtk_types import * "> pywebkit3/gtk3.py
	echo "from gtk_enums import *">>pywebkit3/gtk3.py
	for file in $(IF_FILES); do \
	  echo "Converting file $$file";\
	  ./c2py.py $$file || exit 9; \
	  echo "??????????$$file"; \
	  if test -f pywebkit3/`basename $$file .if`.py-addons; then \
	     cat pywebkit3/`basename $$file .if`.py-addons >> pywebkit3/`basename $$file .if`.py; \
	  fi; \
	  namespace=`echo $$file| sed 's/_//1' | sed 's/_.*//g' `;\
	  echo "from $$namespace"_types" import *" >> pywebkit3/$$namespace.py;\
	  echo "from `basename $$file .if` import *" >> pywebkit3/$$namespace.py; \
	done; 


egg:
	