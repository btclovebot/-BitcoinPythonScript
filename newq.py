#!/usr/bin/env python
## Import the modules required
import bitcoin
import bitcoin.rpc
from twython import Twython
import os
from exchanges.coindesk import CoinDesk
import math
## Create a proxy object and connect to the bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()
## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

#Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''

## Get the value
the_price = CoinDesk().get_current_price(currency='GBP')
the_price = round(the_price, 2)
#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break
#/home/pi/Music/first1.py is AN EXAMPLE path location of the file to run it
txt1 = "#bitcoin CBlock Object Info: Height "
txt2 = " Hash: "
txt3 = " TXVol: "
txt4 = " GBP"
tx_count = len(block_info.vtx)
block_hash = bitcoin.core.b2lx(block_info.GetHash());
block_number = myproxy.getblockcount()
twit = txt1 + str(block_number) + txt2 + str(block_hash) + txt3 + str(tx_count) + " " + str(the_price) + txt4
if tx_count == 1 :
    twit = twit + " #emptyblock"
tweet = twitter.update_status(status=twit)
print tweet
