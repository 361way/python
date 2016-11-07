#!/usr/bin/python

import pwd
import os
import re
import glob

PROC_TCP4 = "/proc/net/tcp"
PROC_UDP4 = "/proc/net/udp"
PROC_TCP6 = "/proc/net/tcp6"
PROC_UDP6 = "/proc/net/udp6"
PROC_PACKET = "/proc/net/packet"
TCP_STATE = {
        '01':'ESTABLISHED',
        '02':'SYN_SENT',
        '03':'SYN_RECV',
        '04':'FIN_WAIT1',
        '05':'FIN_WAIT2',
        '06':'TIME_WAIT',
        '07':'CLOSE',
        '08':'CLOSE_WAIT',
        '09':'LAST_ACK',
        '0A':'LISTEN',
        '0B':'CLOSING'
        }

def _tcp4load():
    ''' Read the table of tcp connections & remove the header  '''
    with open(PROC_TCP4,'r') as f:
        content = f.readlines()
        content.pop(0)
    return content

def _tcp6load():
    ''' Read the table of tcpv6 connections & remove the header'''
    with open(PROC_TCP6,'r') as f:
        content = f.readlines()
        content.pop(0)
    return content

def _udp4load():
    '''Read the table of udp connections & remove the header '''
    with open(PROC_UDP4,'r') as f:
        content = f.readlines()
        content.pop(0)
    return content

def _udp6load():
    '''Read the table of udp connections & remove the header '''
    with open(PROC_UDP6,'r') as f:
        content = f.readlines()
        content.pop(0)
    return content

def _packetload():
    ''' Read the contents of /proc/net/packet for finding processes with packet sockets '''
    with open(PROC_PACKET,'r') as f:
        content = f.readlines()
        content.pop(0)
    return content

def _hex2dec(s):
    return str(int(s,16))

def _ip(s):
    ip = [(_hex2dec(s[6:8])),(_hex2dec(s[4:6])),(_hex2dec(s[2:4])),(_hex2dec(s[0:2]))]
    return '.'.join(ip)

def _ip6(s):
    #this may need to be converted to a string to work properly.
    ip = [s[6:8],s[4:6],s[2:4],s[0:2],s[12:14],s[14:16],s[10:12],s[8:10],s[22:24],s[20:22],s[18:20],s[16:18],s[30:32],s[28:30],s[26:28],s[24:26]]
    return ':'.join(ip)

def _remove_empty(array):
    return [x for x in array if x !='']

def _convert_ipv4_port(array):
    host,port = array.split(':')
    return _ip(host),_hex2dec(port)

def _convert_ipv6_port(array):
    host,port = array.split(':')
    return _ip6(host),_hex2dec(port)

def netstat_tcp4():
    '''
    Function to return a list with status of tcp connections on Linux systems.
    Please note that in order to return the pid of of a network process running on the
    system, this script must be ran as root.
    '''

    tcpcontent =_tcp4load()
    tcpresult = []
    for line in tcpcontent:
        line_array = _remove_empty(line.split(' '))     # Split lines and remove empty spaces.
        l_host,l_port = _convert_ipv4_port(line_array[1]) # Convert ipaddress and port from hex to decimal.
        r_host,r_port = _convert_ipv4_port(line_array[2])
        tcp_id = line_array[0]
        state = TCP_STATE[line_array[3]]
        uid = pwd.getpwuid(int(line_array[7]))[0]       # Get user from UID.
        inode = line_array[9]                           # Need the inode to get process pid.
        pid = _get_pid_of_inode(inode)                  # Get pid prom inode.
        try:                                            # try read the process name.
            exe = os.readlink('/proc/'+pid+'/exe')
        except:
            exe = None

        nline = [tcp_id, uid, l_host+':'+l_port, r_host+':'+r_port, state, pid, exe]
        tcpresult.append(nline)
    return tcpresult

def netstat_tcp6():
    '''
    This function returns a list of tcp connections utilizing ipv6. Please note that in order to return the pid of of a
    network process running on the system, this script must be ran as root.
    '''
    tcpcontent = _tcp6load()
    tcpresult = []
    for line in tcpcontent:
        line_array = _remove_empty(line.split(' '))
        l_host,l_port = _convert_ipv6_port(line_array[1])
        r_host,r_port = _convert_ipv6_port(line_array[2])
        tcp_id = line_array[0]
        state = TCP_STATE[line_array[3]]
        uid = pwd.getpwuid(int(line_array[7])) [0]
        inode = line_array[9]
        pid = _get_pid_of_inode(inode)
        try:                                            # try read the process name.
            exe = os.readlink('/proc/'+pid+'/exe')
        except:
            exe = None

        nline = [tcp_id, uid, l_host+':'+l_port, r_host+':'+r_port, state, pid, exe]
        tcpresult.append(nline)
    return tcpresult

def netstat_udp4():
    '''
    Function to return a list with status of udp connections on Linux systems. Please note that UDP is stateless, so
    state will always be blank. Please note that in order to return the pid of of a network process running on the
    system, this script must be ran as root.
    '''

    udpcontent =_udp4load()
    udpresult = []
    for line in udpcontent:
        line_array = _remove_empty(line.split(' '))
        l_host,l_port = _convert_ipv4_port(line_array[1])
        r_host,r_port = _convert_ipv4_port(line_array[2])
        udp_id = line_array[0]
        udp_state ='Stateless' #UDP is stateless
        uid = pwd.getpwuid(int(line_array[7]))[0]
        inode = line_array[9]
        pid = _get_pid_of_inode(inode)
        try:
            exe = os.readlink('/proc/'+pid+'/exe')
        except:
            exe = None

        nline = [udp_id, uid, l_host+':'+l_port, r_host+':'+r_port, udp_state, pid, exe]
        udpresult.append(nline)
    return udpresult

def netstat_udp6():
    '''
    Function to return a list of udp connection utilizing ipv6. Please note that UDP is stateless, so state will always
    be blank. Please note that in order to return the pid of of a network process running on the system, this script
    must be ran as root.
    '''

    udpcontent =_udp6load()
    udpresult = []
    for line in udpcontent:
        line_array = _remove_empty(line.split(' '))
        l_host,l_port = _convert_ipv6_port(line_array[1])
        r_host,r_port = _convert_ipv6_port(line_array[2])
        udp_id = line_array[0]
        udp_state ='Stateless' #UDP is stateless
        uid = pwd.getpwuid(int(line_array[7]))[0]
        inode = line_array[9]
        pid = _get_pid_of_inode(inode)
        try:
            exe = os.readlink('/proc/'+pid+'/exe')
        except:
            exe = None

        nline = [udp_id, uid, l_host+':'+l_port, r_host+':'+r_port, udp_state, pid, exe]
        udpresult.append(nline)
    return udpresult

def packet_socket():
    '''
    Function to return a list of pids and process names utilizing packet sockets.
    '''

    packetcontent = _packetload()
    packetresult = []
    for line in packetcontent:
        line_array = _remove_empty(line.split(' '))
        inode = line_array[8].rstrip()
        pid = _get_pid_of_inode(inode)
        try:
            exe = os.readlink('/proc/'+pid+'/exe')
        except:
            exe = None

        nline = [pid, exe]
        packetresult.append(nline)
    return packetresult

def _get_pid_of_inode(inode):
    '''
    To retrieve the process pid, check every running process and look for one using
    the given inode.
    '''
    for item in glob.glob('/proc/[0-9]*/fd/[0-9]*'):
        try:
            if re.search(inode,os.readlink(item)):
                return item.split('/')[2]
        except:
            pass
    return None

if __name__ == '__main__':
    print "\nLegend: Connection ID, UID, localhost:localport, remotehost:remoteport, state, pid, exe name"
    print "\nTCP (v4) Results:\n"
    for conn_tcp in netstat_tcp4():
        print conn_tcp
    print "\nTCP (v6) Results:\n"
    for conn_tcp6 in netstat_tcp6():
        print conn_tcp6
    print "\nUDP (v4) Results:\n"
    for conn_udp in netstat_udp4():
        print conn_udp
    print "\nUDP (v6) Results:\n"
    for conn_udp6 in netstat_udp6():
        print conn_udp6
    print "\nPacket Socket Results:\n"
    for pack_sock in packet_socket():
        print pack_sock
