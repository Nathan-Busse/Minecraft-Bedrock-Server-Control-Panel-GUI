# Minecraft-Bedrock-Server-Control-GUI

A control dashboard to monitor and control your minecraft bedrock dedicated server through an easy user interface.  Created by Nathan-Busse  13 January 2022  Made with Python 3.8


![preview](https://user-images.githubusercontent.com/82398683/150782839-8f6a9bd4-a26f-4eb5-a096-b56fc82ede2a.png)


# Note!

This only works for Bedrock.

# Installation.

# Step 1:

Download the server from Minecraft: https://minecraft.net/download/server/bedrock

Here is a tutorial to help you setup your Minecraft Server

https://youtu.be/L36OdDIHkZg

Here is a tutorial to help you with port forwarding and setting up a Dynamic IP using a free and extremely reliable service called Dynu.

https://youtu.be/aiSla-5xq3w

# Step 2:
 Clone the repository.
``` git clone https://github.com/Nathan-Busse/Minecraft-Bedrock-Server-Control-GUI.git ```
 
 # Step 3:
 
 Move the cloned Repository inside your Minecraft Bedrock Dedicated Server directory and extract it.
 
 # Step 4:

Open the ```MCBE control gui.py``` Script in your IDE and change the directory to the location of your Minecraft Bedrock Dedicated Server.

```python
  
default_server_dir =  "C:/Users/Nathan/Documents/Minecraft Servers/bedrock-server-1.18.2.03" # Change directory to your server's location
```
# Step 5: 

Save and close the script.

# Step 6:

Run the ```install.py``` script.

It will install all the package requirements automatically.

It will automatically close the script.

# Step 7

Run ```MCBE control gui.py```.

Your Server should start automatically.

# How to use.
```Server Console``` Displays the inputs and outputs and other useful information of the server. 

```File``` button gives additional functions such as ```View folder directory```,  ```exit``` and ```force exit``` the script.

```Update``` Update the Server to the latest version. [DO NOT USE!] (Their is a bug that causes the programme to become unresponsive.)

```Start Server``` button Starts the server.

```Backup World``` button Creates a copy of your world.

```Players``` Lists the players connected to the server.

```Interact``` Send in-game commands through the control panel.

```Send Command``` Used to send console commands or in-game commands.

```SEND``` button Sends the command to the console.

Type ```stop``` in the ```Send Command``` tab and click ```SEND``` to shutdown the server or close the programme completely.

The server has shutdown successfuly when this message is displayed:

```
Quit correctly

```

Enjoy! 😉

