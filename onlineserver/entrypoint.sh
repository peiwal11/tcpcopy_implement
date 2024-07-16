#!bin/sh

python3 /usr/local/bin/app.py &

/usr/local/tcpcopy/sbin/tcpcopy -x 9999-10.191.7.16:10231 -s 10.191.7.16 
	

