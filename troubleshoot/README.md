# Troubleshooting the ROV


To confirm that the BlueROV is sending data to port 5600, you can check a few things:

1. Use netstat or ss to Check Open Ports:
You can use netstat or ss to see if your system is listening on port 5600.

Using netstat:
bash
Copy
sudo netstat -tuln | grep 5600
Using ss:
bash
Copy
sudo ss -tuln | grep 5600
This will show if there is an active listener on port 5600. You should see something like:

markdown
Copy
udp    UNCONN     0      0         *:5600                 *:*
If you don’t see this, the BlueROV might not be sending data to that port.


Testing with VLC
Alternatively, you can also try opening the UDP stream in VLC:

sudo apt install vlc

Open VLC and go to Media > Open Network Stream.

Enter the URL: udp://@192.168.3.10:5600.

If the stream is being sent correctly, VLC should display the video.

2. wait_ready = False