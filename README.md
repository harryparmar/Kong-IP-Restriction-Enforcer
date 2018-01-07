# Kong-IP-Restriction-Enforcer 
Python Program to enforce Private IPv4 address spaces to APIs on Kong API Gateway server and email If server is down. Open source community has given us some great tools like Kong API Gateway (https://github.com/Kong/kong)  and Konga (https://github.com/pantsel/konga), now is my turn to contribute

## Prerequisites
These libraries should be available on your environment requests, argparse, smtplib and slackclient. If not then install with command
python -m pip install SomePackage
In addition add :getkong: emoji into your slack environment with slack customization or use preexisting emoji in chat.py

## Running the program
Run with arguments -u (Kong server address) -e (from email) -t (to email) -s (smtp server) -st (slack token) -sc (slack channel)

## Description
Program gets all APIs on Kong server passed from arguments and then looks at plug-ins for those APIs to see if IP Restriction is being used If not then it installs it with data for private address range making that API effectively for LAN only. In order to expose the APIs to Internet which have genuine need to be you can just make IP Restriction plug-in disabled, I will add exception list in this program sometime in future as well.

## More features coming -
Additional features will be added in later commits. I will in future scan if API being exposed to Internet(maybe look in LAN only APIs too) has one of Authentication/security features enabled.
