# Minecraft Server

This repo is used to create Minecraft servers for my daughter and I to play and learn about modding/programming.

## Usage

Before attempting to start a server, launch the `base.json` AWS CloudFormation stack. This creates the core resources needed to launch the Minecraft server on Amazon EC2.

### Restore From Backup

To restore from backup, run the following.

```bash
# TODO: Move this to a script file on the server.
# TODO: Test if file exists, only download if it does.
aws s3 cp s3://minecraftbase-minecraftbucket-1kx8ps5t2haao/backup/bee-server.zip /tmp
unzip /tmp/bee-server.zip -d /opt/msm/servers/
chown -R minecraft:minecraft /opt/msm/servers/
```

### Start

To start a server, run `scripts/start.py`. Once complete, the script will output the CloudFormation stack ID, Minecraft server IP address, and commands to run on the server to start Minecraft.

### Save

To save the server, run the following to save the server state and worlds.

```bash
# TODO: Move this to a script file on the server.
msm bee-server save all
msm bee-server worlds backup
msm bee-server stop
aws s3 cp /opt/msm/archives/backups/bee-server/ARCHIVE_NAME s3://BUCKET_NAME/backup/bee-server.zip
```

### Stop

To stop the server, run `scripts/stop.py`. It will delete the instance's CloudFormation stack to save money.

## Future Development

1. [MSM](http://msmhq.com/) //See MSM.sh
1. Update python startup script. //WIP
1. Update python shutdown script. //WIP
1. User management.
1. Create daughter's Minecraft account.

### Modding

1. [Tynker](https://www.tynker.com/learn-to-code/minecraft/)
1. Look into modding. [https://www.feed-the-beast.com](https://www.feed-the-beast.com)

### Post-Setup

1. Look into [Spigot](https://www.spigotmc.org/) (modded Minecraft server).