#!/usr/bin/env python3

import socket, json, threading, sys
try:
    import serial, serial.tools.list_ports
except ImportError:
    print("Dependency not found: please run 'pip3 install pyserial'")
    exit(1)

ce_id = (0x0451, 0xe008)
max_packet_size = 1024

def ser_recv(ser, s, debug):
	print("Serial listening.")
	while True:
		size = int.from_bytes(ser.read(3), 'little')
		if size > 1024:
			sys.stderr.write('Error: Got {} bytes from client, but the max packet size is {}\n'.format(size, max_packet_size))
			# todo: we should stop something, as this will 100% cause a desync
		else:
			data = ser.read(size)
			if debug_mode:
				print("C->S: Type {:>3}, size {}".format(data[0], size))
			status = s.send(data)
			if debug_mode:
				print("C->S completed: ", status)

f = open("config.json","r")
config = json.load(f)
f.close()

server = config["server"]
tcp_port = config["port"]

pipe_mode = False
if "mode" in config:
	if config["mode"] == "pipe":
		pipe_mode = True
	elif config["mode"] == "CEmu":
		pipe_mode = True
	elif config["mode"] == "cemu":
		pipe_mode = True
	elif config["mode"] == "serial":
		pipe_mode = False
	else:
		print("Invalid mode: " + config["mode"])
		exit(1)
serial_mode = not pipe_mode

debug_mode = False
if "debug" in config:
	debug_mode = config["debug"]

if debug_mode:
	print("Running in debug mode.")

if serial_mode:
	if "serial" in config:
		serial_name = config["serial"]
	else:
		ports = [x for x in serial.tools.list_ports.comports() if (x.vid, x.pid) == ce_id]
		if len(ports) == 0:
			print("No device detected.")
			exit(1)

		serial_name = ports[0].device

		if len(ports) > 1:
			print("Multiple devices detected - using {}".format(serial_name))

	ser = serial.Serial(serial_name, timeout=None)
	ser_in = ser
	ser_out = ser

if pipe_mode:
	oname = config["pipe_out"]
	iname = config["pipe_in"]
	if debug_mode:
		print("Out pipe: " + oname)
		print("In pipe: " + iname)
	ser_out = open(oname, "wb", buffering=0)
	ser_in = open(iname, "rb")
	if debug_mode:
		print("Pipes opened")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((server, tcp_port))

print("Connected.")

ser_thread = threading.Thread(target=ser_recv, args=(ser_in, s, debug_mode), daemon=True)
ser_thread.start()

print("^C to exit.")

try:
	while True:
		try:
			data = s.recv(max_packet_size)
			if data:
				if debug_mode:
					print("S->C: Type {:>3}, size {}".format(data[0], len(data)))
				status1 = ser_out.write(len(data).to_bytes(3, byteorder='little'))
				status2 = ser_out.write(data)
				if debug_mode:
					print("S->C completed: ", (status1, status2))

		except socket.error as e:
			sys.stderr.write('Error: {}\n'.format(e))


except KeyboardInterrupt:
	pass

if serial_mode:
	ser.close()
if pipe_mode:
	ser_in.close()
	ser_out.close()
s.close()
