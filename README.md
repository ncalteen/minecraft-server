# Minecraft Server

This repo is used to create Minecraft servers for my daughter and I to play and learn about modding/programming.

## Usage

Before attempting to start a server, launch the `base.json` AWS CloudFormation stack. This creates the core resources needed to launch the Minecraft server on Amazon EC2.

### Start

To start a server, run `scripts/start.py`. Once complete, the script will output the CloudFormation stack ID, Minecraft server IP address, and commands to run on the server to start Minecraft.

### Stop

To stop the server, run `scripts/stop.py`. It will delete the instance's CloudFormation stack to save money.

## Future Development

1. Review [`server.properties`](https://minecraft.gamepedia.com/Server.properties) for setup options.
  - Set `max-players` to 2.
1. [MSM](http://msmhq.com/)
1. Update python startup script.
  - Load from backup.
1. Update python shutdown script.
  - Create backup.
1. Look into [Spigot](https://www.spigotmc.org/) (modded Minecraft server).
1. [Tynker](https://www.tynker.com/learn-to-code/minecraft/)
1. Look into modding. [https://www.feed-the-beast.com](https://www.feed-the-beast.com)
1. User management.
  - How do I only allow certain users (me/sophie)?
1. Create daughter's Minecraft account.