# MusicRemote
Use your phone to control the music on your computer

### Prerequisites
* [Python 3+](https://www.python.org/downloads/)
* [Pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Download) - Multimedia Library
* [AVlib](https://avbin.github.io/AVbin/Download.html) - Mp3 Playback
* [Macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) - Android Automation

Notes:
> AVbin is necessary for mp3 playback. It is otherwise not needed.

> You can use other ways of sending UDP packets to the host,
>Macrodroid is not necessary.

### Usage
1. Install required software
2. Connect the phone to the Wifi network
3. Run [MusicRemote.py](/MusicRemote.py)
4. Use Macrodroid to send *0, 1 or 2* to the host

### Description
This script listens to the UDP stream on a given
host address and port, and acts accordingly to
the incoming data.
The UDP packets are sent from an Android phone
to the listening host using the MacroDroid app.

The process can be improved if port in use is
forwarded and the user has a static IP address
or uses a DNS syncing service.
