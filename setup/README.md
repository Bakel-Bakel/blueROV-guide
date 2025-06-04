# Setting up the blueROV for the first time

1. Disconnect the battery from the battery compartment and read the voltage using a multimeter, above 16v is full battery. Below 12v is not so good but manageable. The lower the worse, it is advised to charge once it gets to 12v.

2. Pressure test the two compartment with the pump. Pump till 15

3. Connect the blueROV to your laptop/PC (machine) via the ethernet/USB link.

4. It is advised to run and install the following, as it will help with future debugging.

sudo apt install net-tools

![alt text](assets/img/image.png)

enx00e04c3600f3 – This looks like your USB-to-Ethernet adapter (likely the BlueROV tether interface), but it has no IP address and no data traffic (RX 0, TX 0).

1. Set a Static IP Manually
The BlueROV companion computer expects your PC to be at 192.168.3.20.

Run the following command in your terminal:


sudo ip addr add 192.168.3.20/24 dev enx00e04c3600f3

ping 192.168.3.21


RED light on the raspberry pi indicates insufficient power to the ROV. You could try turning off and on the ROV or charging/replacing the battery.