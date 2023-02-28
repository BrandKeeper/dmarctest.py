#!/usr/bin/python3

import smtplib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ef", help='Envelope From', required=False, type=str)
parser.add_argument("--hf", help='Header From', required=True, type=str)
parser.add_argument("--to", help='To', required=True, type=str)
args = parser.parse_args()

# If return-path is not set, use header-from as return-path.
if args.ef is None:
    _ef = args.hf
else:
    _ef = args.ef

_hf = args.hf
_to = args.to

message ="""\
To: Test Reciever <%s>
From: DMARC Tester <%s>
Subject: DMARC test

Hello,

This is a test mail from %s.

""" % (_to, _hf, _hf)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.set_debuglevel(1)
    smtpObj.connect()
    smtpObj.sendmail(_ef, _to, message)
    print("Successfully sent.")
except smtplib.SMTPException as err:
    print("Error in sending a mail.")
    print(err)

