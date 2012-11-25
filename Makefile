IF_FILES=$(wildcard *.if)

all:
	echo ""> src/gobject.py
	echo "from webkit_types import *"> src/webkit3.py
	echo "from gtk_types import * "> src/gtk3.py
	echo "from gtk_enums import *">>src/gtk3.py
	for file in $(IF_FILES); do \
	  echo "Converting file $$file";\
	  ./c2py.py $$file || exit 9; \
	  echo "??????????$$file"; \
	  if test -f src/`basename $$file .if`.py-addons; then \
	     cat src/`basename $$file .if`.py-addons >> src/`basename $$file .if`.py; \
	  fi; \
	  namespace=`echo $$file| sed 's/_//1' | sed 's/_.*//g' `;\
	  echo "from $$namespace"_types" import *" >> src/$$namespace.py;\
	  echo "from `basename $$file .if` import *" >> src/$$namespace.py; \
	done; 