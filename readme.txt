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
    port      The port number of the remote host.
              For my test server, this is 51701.
    debug     Whether or not to display socket/serial status, and packet relay to console
              "true" | "false"
    mode      Whether to run the bridge for serial (calc to server) or pipe (CEmu to server)
              Serial Mode = "default" | "serial"
              CEmu Mode = "pipe" | "cemu"
    pipe-in   Path to a file to use as the in-pipe for CEmu
    pipe-out  Path to a file to use as the out-pipe for CEmu

3) _Usage (Serial)_
	Upon successfully configuring the project, you can run the bridge via the Terminal command: `python3 bridge.py` from within the project directory. Ensure that the client program (TITREK) is running, and on the splash screen/main menu. The "Networking disabled!" alert should show up momentarily on the main menu screen, then disappear. When this occurs you can run the bridge.
  Assuming no errors, the bridge should inform you that both the serial connection and the tcp socket are connected. You can now proceed to use TI-Trek from your calculator and all packets should be relayed. To exit the bridge, you can Keyboard Interrupt (Ctrl+C).
  
4) _Usage (CEmu)_
	Using the bridge in this mode is more or less the same as above, with a few caveats. First, it is recommended to have the bridge running before you start CEmu, or at least, before you start TITREK. If you get an error about missing Pipe files, simply launch CEmu, run TITREK once to the main menu screen, then exit it and close CEmu. Now try to run the bridge again. It should open the Pipe files now but not open a Serial link. Now open CEmu again, and run TITREK. You should then see Serial connected. If everything happens like this, you can proceed. If not, try again.
	NOTE: If you've already gone through this process and the bridge is still running, you do not need to repeat this process if you close/reopen TITREK. This is more or less needed the first time you are running CEmu from a reboot. Once the bridge is running, as long as you don't close CEmu, you should be ok. However, if you close/reopen CEmu, you can simply relaunch the bridge before reopening CEmu again without needing to recreate the pipe files.
	

  

