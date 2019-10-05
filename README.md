###### The Python Tkinter GUI Roku Remote
<img src="https://github.com/rootVIII/roku_remote/blob/master/screenshot.png" alt="example1" height="575" width="230">
<br><br>
<b>First follow these quick/simple steps to enable your Roku Server:</b>
<br>
https://blog.roku.com/developer/developer-setup-guide
<br>
* Remember its IP address as you'll need to
enter it as shown in the image above.
<br><br>
Do not press enter after entering your IP: Just leave it in the
text-field and start using the remote.
<br><br>
You shouldn't really need to use the power button as most Rokus
will turn on when the input receives power from the TV.
However it may be useful for turning the Roku OFF.
<br><br>
requires Python3 (and python3-tk if on Linux)
<pre>
  <code>
    

Clone roku_remote, navigate to project root, and run the following command
(ensure pip points to Python3 or use pip3):

pip install -e .

or install directly from Git:

pip install git+https://github.com/rootVIII/roku_remote

Then run the command from any location in your shell: roku_remote


  </code>
</pre>
Runs on Linux, Mac, and Windows
<br>
This was developed on Ubuntu 16.04.4 LTS.
<hr>
<b>Author: rootVIII 18AUG2018</b><br>
