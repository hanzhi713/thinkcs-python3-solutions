# copy modules to python lib prior to importing modules
import mymodule1
import mymodule2

# !!!Error will occur in following triple-quoted code because of missing parentheses!!!
'''print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )
'''

# correct version
print((mymodule2.myage() - mymodule1.myage()) ==
      (mymodule2.year() - mymodule1.year()))
# return True since my birthday is on July 13th.
