#!/bin/bash
# setup_skippassword.sh
#	This script will automate the process of setting up scp without
#	a password.
#	Martin 2/2015
#---------------------------------------------------------------------------
# User defined variables #
OVERWRITE=n # overwrite ssh key? y or n?
REMHOST=sense1.cn # remote hostname
REMUSER=sense2 # remote user
REMPASS=CO2Monit # remote user's password

#!- Step 1: getting complete path of ssh key file
SCRIPTDIR=`pwd`; cd ~; IDFILE=`pwd`/.ssh/id_rsa.pub; cd $SCRIPTDIR

#!- Step 2: generate the ssh key
ssh-keygen -t rsa << END1
$IDFILE
$OVERWRITE

END1

#!- Step 3: copy key to remote host
cat > send_key.sh <<EOF
#!/usr/bin/expect
spawn ssh-copy-id $REMUSER@$REMHOST
expect "*?assword:"
send -- "$REMPASS\r"
send -- "\r"
expect eof
EOF
chmod +x send_key.sh
./send_key.sh

echo "Success! scp/ssh without password should now be enabled."

