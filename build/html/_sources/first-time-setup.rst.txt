Setting Up the BlueROV for the First Time
=========================================

This section will guide you through preparing your BlueROV for initial use.

.. note::

   Make sure you are using **Ubuntu Linux** (20.04 or 22.04 recommended) and have direct hardware access via native installation or dual boot. Avoid WSL, VMware, or other virtual machines for this setup.

.. contents::
   :local:
   :depth: 1



Step 1: Check Battery Voltage
--------------------------------

- Disconnect the battery from the battery compartment.
- Use a multimeter to read the voltage:
  
  - **Above 16V** → Full battery.
  - **12V - 16V** → Acceptable but not full.
  - **Below 12V** → Weak battery; charging is highly recommended.

.. tip::

   Charge the battery when it drops to **12V** to maintain healthy power levels and avoid under-voltage issues.



Step 2: Pressure Test the Compartments
----------------------------------------

- Use the pump to perform a pressure test.
- Pump the compartment to **15 PSI**.
- Monitor for air leaks and ensure all seals are secure.



Step 3: Connect BlueROV to Your Machine
------------------------------------------

- Use the USB-to-Ethernet interface to connect the BlueROV to your laptop/PC.
- The interface should appear as a device similar to:

  ``enx00e04c3600f3``

- You can check this using:

  .. code-block:: bash

     ip addr

.. image:: ../assets/img/image.png
   :alt: Network interface with no IP
   :align: center
   :width: 600

If the RX (received) and TX (transmitted) data is **0**, and there's **no IP address**, proceed with the next step.



Step 4: Install Network Utilities
------------------------------------

Install `net-tools` to gain access to helpful debugging utilities:

.. code-block:: bash

   sudo apt install net-tools


Step 5: Assign Static IP to USB-Ethernet Interface
-----------------------------------------------------

The BlueROV’s companion computer expects your PC to use the static IP: **192.168.3.20**

Run the following commands in your terminal:

.. code-block:: bash

   sudo ip addr add 192.168.3.20/24 dev enx00e04c3600f3
   ping 192.168.3.21

- Replace `enx00e04c3600f3` with the correct interface name on your machine if it's different.





.. hint::

   Once the ping to `192.168.3.21` is successful, you can access the BlueROV's web interface at:

   `http://192.168.3.1:2770` in your browser.
