#!/usr/bin/python

# data for database connection
host = "172.22.64.3"
user = "videowf"
passwd = "video2012WF"
database = "videoworkflow"
column = "inputfilepath"

# permissions for directories:
import stat
# stat.S_ISUID: Set user ID on execution.
# stat.S_ISGID: Set group ID on execution.
# stat.S_ENFMT: Record locking enforced.
# stat.S_ISVTX: Save text image after execution.
# stat.S_IREAD: Read by owner.
# stat.S_IWRITE: Write by owner.
# stat.S_IEXEC: Execute by owner.
# stat.S_IRWXU: Read, write, and execute by owner.
# stat.S_IRUSR: Read by owner.
# stat.S_IWUSR: Write by owner.
# stat.S_IXUSR: Execute by owner.
perm=stat.S_IREAD


