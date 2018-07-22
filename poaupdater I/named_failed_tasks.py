#!/usr/bin/python

from poaupdater import uSysDB
from poaupdater import uLogging
from poaupdater import openapi

## Disable logging to the console
uLogging.log_to_console = False

## Show all tasks' numbers
con = uSysDB.connect()
cur = con.cursor()
print("\nThere are the following failed/rescheduled named tasks:")
cur.execute("select task_id from tm_tasks where name like \'%pdate named%\' and status in ('f', 's')")
res = cur.fetchall()
for x in range(0, len(res)):
        print("--- %s ---" % res[x])

## Show all tasks with their outputs:
print("\nTask log for these tasks:")
cur.execute("select task_id, action_output from tm_logs where task_id in (select task_id from tm_tasks where name like \'%pdate named%\' and status in ('f', 's'))")
res2 = cur.fetchall()
for x in range(0, len(res2)):
        print("Task #%s Output: \"%s\"" %  (res2[x][0], res2[x][1]))

## Restart all of the tasks
print("\nPlease wait. The tasks are restarting...")
api = openapi.OpenAPI()
for x in range(0, len(res)):
        taskId=res[x][0]
        result = api.pem.tasks.rescheduleTask(task_id=taskId, timeout=3600)
        print("Task #%s has been restarted." % res[x])
print("All of the tasks have been restarted.")