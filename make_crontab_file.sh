#!/bin/bash
cat >cron.my <<EOF
# m     h     dom     mon     dow     command
  @reboot                             /home/YN_Wang/little_py_scripts/wk_restart.sh

EOF

#==Submit the cron jobs====

