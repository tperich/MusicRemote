import pyglet, socket, glob, os
from modules import check_os

# Define Pyglet and music variables and add songs
# to the music player queue.
clear = check_os.clear()
song_playlist = glob.glob("*.mp3")
music_player = pyglet.media.Player()
for item in range(len(song_playlist)):
	song = pyglet.resource.media(song_playlist[item])
	music_player.queue(song)


class PacketListener():
	def __init__(self, l_host, l_port):
		# Bind sockets to l_host and l_port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((l_host,l_port))

	def udp_listener(self):
		print("[x] Server Started")
		while True:
			# Listen for incoming UDP traffic
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
			# None or other data received, go back to listening
			pass


class Music():
	def play_song(self):
		music_player.play()
		os.system(clear)
		print("[x] Music playing")

	def stop_song(self):
		music_player.pause()
		os.system(clear)
		print("[x] Music stopped")

	def next_song(self):
		# Take next song from queue
		music_player.next_source()
		os.system(clear)
		print("[x] Next song")

# Pass local address and port.
# If the address is left empty
# the packets are received from
# all hosts.
PacketListener("",1337).udp_listener()
