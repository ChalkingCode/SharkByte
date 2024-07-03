import scapy.all
from scapy.all import sniff
import requests
import datetime


def get_pcap():
    print("----------------------------------------------")
    print("|                                             |")
    print("|                                             |")
    print("|                                             |")
    print("|                Shark Byte                   |")
    print("|                                             |")
    print("|         Simple Packet sniffer script        |")
    print("|             Cloudshark and Scapy            |")
    print("|                  created by                 |")
    print("|                 CHALKINGCODE                |")
    print("|                                             |")
    print("|                                             |")
    print("----------------------------------------------")

    # Grabbing the date and time so we can use it in our file naming convention
    pcap_date = datetime.datetime.now()
    file = f"capturedon_{pcap_date}.pcap"
    # Just sniffing around on the network
    capture = sniff(count=50)
    # Writing out what was found to a pcap file
    print("Writing packets out to pcap")
    scapy.all.wrpcap(f"{file}", capture)
    # sending our data to cloud shark to get a better look at it 
    send_pcap(file)



def send_pcap(file):
    # You can get a 30 day free account for cloudshark no credit card needed once you create an account you can get a key
    token = "Your_API_KEY_HERE"
    pcap_file = f"{file}"
    files = {'file': open(pcap_file, 'rb'),}
    print("Sending it")
    send_it = requests.post(f"https://www.cloudshark.org/api/v1/{token}/upload", files=files)
    test = print(send_it.text)
    return test

get_pcap()
