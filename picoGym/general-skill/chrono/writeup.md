# DESCRIPTION
How to automate tasks to run at intervals on linux servers?

# SOLUTION
one of known tools for automation is cron or crontab, the goals are read and locate the
cron script

# STEP
immediately after connecting with ssh `ls` will return nothing

first i need to locate where the cron environment are, after i googled and cron/crontab are
located in `/etc/crontab`

so next, locate where the etc directory is, its usually in root `cd /`

immediately `ls` would return many directories, and one of the directories were etc `cd etc`

`ls` inside etc dir, and there will be the crontab script 

`cat crontab` would return the flag
