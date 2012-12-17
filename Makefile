IF_FILES=$(wildcard *.if)

all:
	./c2py.py $$file || exit 9; \
	echo ""> pyggi/gobject.py
	echo "from webkit3_types import *"> pyggi/webkit3.py
	echo "from gtk3_types import * "> pyggi/gtk3.py
	echo "from gtk3_enums import *">>pyggi/gtk3.py
	echo "from javascriptcore_enums import *">pyggi/javascriptcore.py
	echo "from javascriptcore_types import *">>pyggi/javascriptcore.py
	for file in $(IF_FILES); do \
	  if test -f pyggi/`basename $$file .if`.py-addons; then \
	     cat pyggi/`basename $$file .if`.py-addons >> pyggi/`basename $$file .if`.py; \
	  fi; \
	  namespace=`echo $$file| sed 's/_//1' | sed 's/_.*//g' `;\
	  echo "from $$namespace"_types" import *" >> pyggi/$$namespace.py;\
	  echo "from `basename $$file .if` import *" >> pyggi/$$namespace.py; \
	done; 


egg:
	./setup.py clean --all
	./setup.py bdist_egg upload
