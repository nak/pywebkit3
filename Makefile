IF_FILES=$(wildcard *.if)

all:
	echo ""> src/gobject.py
	echo ""> src/webkit.py
	echo "from gtk_types import * "> src/gtk.py
	echo "from gtk_enums import *">>gtk.py
	for file in $(IF_FILES); do \
	  echo "Converting file $$file";\
	  ./c2py.py $$file || exit 9; \
	  namespace=`echo $$file| sed 's/_//1' | sed 's/_.*//g' `;\
	  echo "from `basename $$file .if` import *" >> src/$$namespace.py; \
	done;