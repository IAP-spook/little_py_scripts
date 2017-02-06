#! /usr/bin python
# -*-coding:utf-8-*-
# Use function get_ip_address('lo')&get_ip_address('eth0') get the ipaddress
import socket
import fcntl
import struct
from time import gmtime, strftime


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24])


def write_ip_2file():
	f = open('ip_address.txt','a')
	f.write(strftime('%Y%m%d%H%M',gmtime()))
	f.write(' '+get_ip_address('eth0')+'\n')


if __name__ =="__main__":
	#print get_ip_address('lo')
	#print get_ip_address('eth0')
	write_ip_2file()


