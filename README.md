# SharkByte
A super simple Packet sniffer script leveraging Scapy and Cloudshark


## Table of contents
* [Features](#features)
* [Setup](#setup)
* [HowTo](#howto)

## Features
- sniffs packets using scapy. You can set the count as how many you would like as its configurable
- Outputs packet results to a pcap file
- Uploads your pcap file to cloudshark

## Setup

### Prerequisites

#### Enviroment
```
1.) ensure you have python 3.x installed 
$ python3 -m venv /path/you/want/the/env/in
$ source /path/you/want/the/env/in/bin/activate 
```
2.) You will need a cloudshark account. They will give a free account for 30 days no credit card required https://www.qacafe.com/analysis-tools/cloudshark/qa-cloudshark-personal-saas/
#### Clone repository 

        $ git clone https://github.com/ChalkingCode/SharkByte.git
        $ cd Sharkbyte


#### Install Packages on env
```       
scapy
requests

# This only needs to be ran once per env 
$ pip install -r requirements.txt
```
## HowTo

How to run the script 

```
$ sudo python sharkbyte.py
Password:
WARNING: No IPv4 address found on anpi1 !
WARNING: No IPv4 address found on anpi0 !
WARNING: more No IPv4 address found on en3 !
----------------------------------------------
|                                             |
|                                             |
|                                             |
|                Shark Byte                   |
|                                             |
|         Simple Packet sniffer script        |
|             Cloudshark and Scapy            |
|                  created by                 |
|                 CHALKINGCODE                |
|                                             |
|                                             |
----------------------------------------------
Writing packets out to pcap
Sending it
{"id":"3739f330eb8f","filename":"capturedon_2024-07-03 16:55:10.399768.pcap"}
```
