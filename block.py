#!/usr/bin/env python

## Import the modules required
import bitcoin
import bitcoin.rpc
from twython import Twython

## Create a proxy object and connect to the bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

#Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token =''
oauth_token_secret = ''

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

p2 = "TXVol: "

p3 = len(block_info.vtx)

U = p2 + str(p3)

string = bitcoin.core.b2lx(block_info.GetHash());

b1 = "Block Hash: "

O = b1 + str(string)

#lp = bitcoin.core.b2lx(block_info.GetHash())

#O = b1 + str(lp)

a = "CBlock Object Info: Height "

w = myproxy.getblockcount()

P = a + str(w)


s = twitter.update_status(status='New Block: ' + P + "\n" + O + "\n" + U)
print (s)


