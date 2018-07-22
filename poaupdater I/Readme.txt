This script will find all failed "Update named" tasks in queue, paste their output and re-run them.

How to emulate such situation on your lab:

oss=> select * from tm_tasks where name like '%pdate named%' and status in ('f', 's');
task_id |               name                |                        description                         |   location   |     method     | run_num |     next_start      | cancelled_by | ti
me_cancelled | status | timeout | prio | subscription_id | parent_task_id | non_legacy
---------+-----------------------------------+------------------------------------------------------------+--------------+----------------+---------+---------------------+--------------+---
-------------+--------+---------+------+-----------------+----------------+------------
   17838 | Update named MN.seven.zero.com(1) | Make DNS zones hosted on named server MN.seven.zero.com(1) | SCREF:BIND:0 | thUpdateServer |       1 | 2018-03-15 05:30:12 |            0 |
             | s      |    3600 |    0 |               0 |              0 |
   17821 | Update named MN.seven.zero.com(1) | Make DNS zones hosted on named server MN.seven.zero.com(1) | SCREF:BIND:0 | thUpdateServer |       5 | 2018-03-15 05:21:09 |            0 |
             | f      |    3600 |    0 |               0 |              0 |
(2 rows)

oss=> select task_id, action_output from tm_logs where task_id in (select task_id from tm_tasks where name like '%pdate named%');
task_id |                                                                                                                                                                                action_output
---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   17838 | Multiple errors during NS update: test-your-might.trn.(6): lstat /var/named/test-your-might.trn.: No such file or directory (errno 2). PA agent endpoint: https://10.39.87.23:8352
/process\012test-your-might.trn.(6): lstat /var/named/test-your-might.trn.: No such file or directory (errno 2). PA agent endpoint: https://10.39.87.23:8352/process\012._____dns_____5000
   17821 | Multiple errors during NS update: test-your-might.trn.(6): lstat /var/named/test-your-might.trn.: No such file or directory (errno 2). PA agent endpoint: https://10.39.87.23:8352
/process\012._____dns_____5000