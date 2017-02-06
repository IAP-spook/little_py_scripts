#! /usr/bin/python
# -*- coding:utf-8 -*-
# Use function get_ip_address('lo')&get_ip_address('eth0') get the ipaddress
# write_ip_2file record the ip and time
# send_ipfile send the file to the server 
import socket
import fcntl
import struct
import time
import subprocess


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24])


def write_ip_2file(ip_fn):
	f = open(ip_fn,'a')
	f.write(time.strftime('%Y%m%d%H%M',time.localtime()))
	f.write(' '+get_ip_address('eth0')+'\n')


def send_ipfile(ip_fn):
	pwd='CO2Monit '
	scp_cmd='scp '+ip_fn+' sense2@sense1.cn:/home/sense2/wyn'
	child1=subprocess.Popen('sshpass -p '+pwd+scp_cmd,shell=True)
	child1.wait()
if __name__ =="__main__":
	#print get_ip_address('lo')
	#print get_ip_address('eth0')
	fn='ip_address.txt'
	write_ip_2file(fn)
	send_ipfile(fn)

