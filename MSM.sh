# See manual installation steps.
# http://msmhq.com/docs/installation.html
export PATH=$PATH:/usr/local/bin
yum update -y
yum install -y screen rsync zip jq
wget http://git.io/6eiCSg -O /etc/msm.conf
mkdir /opt/msm
useradd minecraft --home /opt/msm
chown minecraft /opt/msm
chmod -R 775 /opt/msm
mkdir /dev/shm/msm
chown minecraft /dev/shm/msm
chmod -R 775 /dev/shm/msm
wget http://git.io/J1GAxA -O /etc/init.d/msm
chmod 755 /etc/init.d/msm
chkconfig --add msm
ln -s /etc/init.d/msm /usr/local/bin/msm
msm update -y
wget http://git.io/pczolg -O /etc/cron.d/msm
service crond reload
msm jargroup create minecraft minecraft
msm server create bee-server
msm bee-server jar minecraft
echo 'msm-version=minecraft/1.14.0' >> /opt/msm/servers/bee-server/server.properties
msm bee-server start
sed -i 's/eula=false/eula=true/g'  /opt/msm/servers/bee-server/eula.txt
msm bee-server start
# What about worldstorage? http://msmhq.com/docs/concepts/layout.html