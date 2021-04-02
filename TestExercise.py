import os
import sqlite3

import FileChanges

FileChanges.getbasefile()
FileChanges.connectdb()
#FileChanges.corecursor()
result = FileChanges.tableexists("people")
print(result)