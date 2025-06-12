Task 4

Simple Packet Sniffer 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is a basic network packet sniffer written in Python using the Scapy library. It’s a command-line tool that watches network traffic and shows you what’s happening behind the scenes on your computer's network.
You can use it to learn how data travels over the internet and what’s inside the packets being sent and received.

What Does It Do?


When you run the script:
It captures live network traffic.
For each packet it sees, it shows:
The time it was captured
The source and destination IP addresses
The protocol used (like TCP or UDP)
The port numbers
Any raw data or payload inside the packet (decoded if possible)
This all prints out live in your terminal window.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What we Need?


To use this script, make sure you have:
Python 3 installed
The Scapy library (install it with pip install scapy)
If you’re on Windows, you’ll also need Npcap installed
On Windows, make sure you run the script as Administrator or it may not work properly.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to Run It ?


Save the script as sniffer.py
Open your terminal or command prompt
python sniffer.py
You’ll start seeing packet info in real time

Press Ctrl + C when you want to stop it

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Why Use This?

This script is great if you’re:
Learning about networking
Curious how TCP, UDP, and IP packets work
Wanting to see what kind of data is being sent across your network

Use It Responsibly
!!! Please only use this tool on networks you own or have permission to monitor.
Sniffing traffic on other people’s networks without permission is illegal and unethical.