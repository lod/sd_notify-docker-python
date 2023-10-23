import sdnotify
import time

print("Test starting up...", flush=True)
# In a real service, this is where you'd do real startup tasks
# like opening listening sockets, connecting to a database, etc...
time.sleep(10)
print("Test startup finished", flush=True)

# Inform systemd that we've finished our startup sequence...
n = sdnotify.SystemdNotifier(debug=True)
n.notify("READY=1")

count = 1
while True:
	print("Running... {}".format(count), flush=True)
	n.notify("STATUS=Count is {}".format(count))
	count += 1
	time.sleep(2)
