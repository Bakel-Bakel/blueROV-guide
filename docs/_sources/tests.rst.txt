Test Scripts for the blueROV
===============


📷 Testing the Camera via Terminal
----------------------------------

To test the video stream from the BlueROV camera, use the following GStreamer command:

.. code-block:: bash

   gst-launch-1.0 -v udpsrc port=5600 caps="application/x-rtp, media=video, encoding-name=H264, payload=96" \
   ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink

.. note::

   This command opens a window to display the live H264 video stream coming in on **UDP port 5600**.
