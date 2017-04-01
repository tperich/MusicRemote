import pyglet, socket, glob, os

# This script listens to the UDP stream on a given
# host address and port, and acts accordingly to
# the incoming data. It should play music at the
# moment.
# The UDP packets are sent from an Android phone
# to the listening host using the MacroDroid app.
#
# The process can be improved if port in use (1337)
# is forwarded and the user has a static IP address
# or uses a DNS syncing service.
#
# Pyglet is used for playing music, not mandatory
# for the script to work. Note: You will also need
# AVlib for playing mp3 files using Pyglet.


# Define Pyglet and music variables and add songs
# to the player queue.
song_playing = 0
playlist = glob.glob("*.mp3")
player = pyglet.media.Player()
for song in range(len(playlist)):
	song = pyglet.resource.media(playlist[song])
	player.queue(song)

# song = pyglet.media.load("Music/dope_dod-dealwiththedevil.mp3")
# looper = pyglet.media.SourceGroup(song.audio_format, None)
# looper.loop = True
# looper.queue(song)


class PacketListener():
	def __init__(self, l_host, l_port):
		# Bind sockets to l_host and l_port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((l_host,l_port))

	def udp_listener(self):
		print("[x] Server Started")
		# Listen for incoming UDP traffic
		while True:
			inbound_data, client_address = self.sock.recvfrom(1024)
			self.music_controller(inbound_data.decode("utf-8"))

	def music_controller(self, inbound_data):
		if inbound_data == "0":
			Music().play_song()
		elif inbound_data == "1":
			Music().stop_song()
		elif inbound_data == "2":
			Music().next_song()
		else:
			# No data received, go back to listening
			pass


class Music():
	'''def __init__(self):
		if song_playing == 0:
			self.play_song()
		else:
			self.stop_song()'''

	def play_song(self):
		song_playing = 1
		player.play()
		os.system("cls")
		print("[x] Music playing")

	def stop_song(self):
		song_playing = 0
		player.pause()
		os.system("cls")
		print("[x] Music stopped")

	def next_song(self):
		# Take next song from queue
		player.next_source()
		os.system("cls")
		print("[x] Next song")
		#print("No more songs :(")

# Pass local address and port
# If the address is left empty
# the packets are received from
# all hosts.
PacketListener("",1337).udp_listener()
