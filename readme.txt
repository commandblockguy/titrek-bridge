####################################
## TI - TREK Bridge Documentation ##
####################################


1) Installation
  Simply extract or clone this project to a directory of your choice.
  You will need to install Python3 and pip3 if you haven't already.
  You will also need the serial library. To get it, run in Terminal `pip3 install pyserial`.
  
2) Configuration
  To configure this project, open the file `config.json` with your favorite flavor of text editor.
  You will need to edit the config options:
    server    The IP address or hostname of the server you want to connect to.
              For my test server, this is play.titrek.us.
    port      The port number of the remote host.
              For my test server, this is 51701.
    debug     Whether or not to display socket/serial status, and packet relay to console
              "true" | "false"
    mode      Whether to run the bridge for serial (calc to server) or pipe (CEmu to server)
              Serial Mode = "default" | "serial"
              CEmu Mode = "pipe" | "cemu"
    pipe-in   Path to a file to use as the in-pipe for CEmu
    pipe-out  Path to a file to use as the out-pipe for CEmu

2) Usage (Serial)
  Upon successfully configuring the project, you can run the bridge via the Terminal command:
    `python3 bridge.py`
  from within the project directory. Ensure that the client program (TITREK) is running, and on the splash screen/main menu.
  The "Networking disabled!" alert should show up momentarily on the main menu screen, then disappear.
  When this occurs you can run the bridge.
  Assuming no errors, the bridge should inform you that both the serial connection and the tcp socket are connected.
  You can now proceed to use TI-Trek from your calculator and all packets should be relayed.
  To exit the bridge, you can Keyboard Interrupt (Ctrl+C).
  
3) Usage (CEmu)


  

