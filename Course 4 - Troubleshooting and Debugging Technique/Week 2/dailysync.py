#!/usr/bin/env python
import subprocess
src = "/home/student-01-4427a2630649/data/prod/"
dest = "/home/student-01-4427a2630649/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
