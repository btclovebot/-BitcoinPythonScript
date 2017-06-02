#!/usr/bin/env python
## The @BITCOINRATBOT TWITTER SCRIPT
## Import the modules required
import bitcoin
import bitcoin.rpc
from twython import Twython
#import sys
#import os
#import json
#from exchanges.coinapult import Coinapult
import math
import datetime
import time
## Connect to the bitcoin RPC Proxy
myproxy = bitcoin.rpc.Proxy()
## Get the block number
block_no = myproxy.getblockcount()
## Grab the block using the RPC
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))
btime = block_info.nTime
btime  = datetime.datetime.fromtimestamp(btime) 
bversion = block_info.nVersion
bbits = block_info.nBits
bdiff = block_info.difficulty
bhash = bitcoin.core.b2lx(block_info.GetHash())
pbhash = bitcoin.core.b2lx(block_info.hashPrevBlock)
mroot = bitcoin.core.b2lx(block_info.hashMerkleRoot)
## Grab the block from the bitcoin proxy using the command line augment data
#best_hash = str(sys.argv[1])
#block_bytes = bitcoin.core.lx(best_hash)
#block_info = myproxy.getblock(block_bytes)
## Prepare your twitter, you will need it for everything
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
## Now we can use the block to tell us stuff
vtx = block_info.vtx
tx_count = len(vtx)
## Declare some variables used in our script
outputs = 0
halving = 210000
diffadjust = 2016
nexthalving = 0
diffchange = 0
rewarded = 0
reward = 0
fees = 0
tmp_block_no = 0
newdiff = 0 
btcformatted = ""
satoshis = 0 
satoshislen = 0
satoshisleft = ""
satoshisright = ""
satoshismid = ""
## Function to Format Satoshis into BTC eg 12,345,678.12345678
def btcformat (satoshis) :
    if satoshis == 0 :
        btcformatted = "0.00000000"
    else :
        satoshis = str(satoshis)
        satoshislen = len(satoshis)
        if satoshislen == 1 :
            btcformatted = "0.0000000" + satoshis
        if satoshislen == 2 :
            btcformatted = "0.000000" + satoshis
        if satoshislen == 3 :
            btcformatted = "0.00000" + satoshis
        if satoshislen == 4 :
            btcformatted = "0.0000" + satoshis
        if satoshislen == 5 :
            btcformatted = "0.000" + satoshis
        if satoshislen == 6 :
            btcformatted = "0.00" + satoshis
        if satoshislen == 7 :
            btcformatted = "0.0" + satoshis
        if satoshislen == 8 :
            btcformatted = "0." + satoshis
        if satoshislen == 9 :
            satoshisleft = satoshis[:1]
            satoshisright = satoshis[1:]
            btcformatted = satoshisleft + "." + satoshisright
        if satoshislen == 10 :
            satoshisleft = satoshis[:2]
            satoshisright = satoshis[2:]
            btcformatted = satoshisleft + "." + satoshisright
        if satoshislen == 11 :
            satoshisleft = satoshis[:3]
            satoshisright = satoshis[3:]
            btcformatted = satoshisleft + "." + satoshisright
        if satoshislen == 12 :
            satoshisleft = satoshis[:4]
            satoshisright = satoshis[4:]
            btcformatted = satoshisleft[:1] + "," + satoshisleft[1:] + "." + satoshisright
        if satoshislen == 13 :
            satoshisleft = satoshis[:5]
            satoshisright = satoshis[5:]
            btcformatted = satoshisleft[:2] + "," + satoshisleft[2:] + "." + satoshisright      
        if satoshislen == 14 :
            satoshisleft = satoshis[:6]
            satoshisright = satoshis[6:]
            btcformatted = satoshisleft[:3] + "," + satoshisleft[3:] + "." + satoshisright
        if satoshislen == 15 :
            satoshisleft = satoshis[:7]
            satoshisright = satoshis[7:]
            btcformatted = "," + satoshisleft[4:] + "." + satoshisright
            satoshismid = satoshisleft
            satoshisleft = satoshisleft[:1]
            satoshismid = satoshismid[:4]
            satoshismid = satoshismid[1:]
            btcformatted =  satoshisleft + "," + satoshismid + btcformatted
        if satoshislen == 16 :
            satoshisleft = satoshis[:8]
            satoshisright = satoshis[8:]
            btcformatted = "," + satoshisleft[5:] + "." + satoshisright
            satoshismid = satoshisleft
            satoshisleft = satoshisleft[:2]
            satoshismid = satoshismid[:5]
            satoshismid = satoshismid[2:]
            btcformatted =  satoshisleft + "," + satoshismid + btcformatted
    return btcformatted
    
def nicediff(diff) :
    if diff == 0 :
        diffformatted = "0"
    else :
        diff = str(diff)
        difflen = len(diff)
        #if difflen
        diffformatted = "0"
    return diffformatted
    
## Maths for halvening reporting
if block_no < halving :
    nexthalving = halving - block_no
    reward = 5000000000
if block_no >= halving :
    nexthalving = halving*2 - block_no
    reward = 2500000000
if block_no >= halving*2 :
    nexthalving = halving*3 - block_no
    reward = 1250000000
if block_no >= halving*3 :
    nexthalving = halving*4- block_no
    reward = 625000000 
if block_no >= halving*4 :
    nexthalving = halving*5 - block_no
    reward = 312500000
if block_no >= halving*5 :
    nexthalving = halving*6 - block_no
    reward = 156250000
if block_no >= halving*6 :
    nexthalving = halving*7 - block_no
    reward = 78125000
if block_no >= halving*7 :
    nexthalving = halving*8 - block_no
    reward = 39062500
if block_no >= halving*8 :
    nexthalving = halving*9 - block_no
    reward = 19531250
if block_no >= halving*9 :
    nexthalving = halving*10 - block_no
    reward = 9765625
if block_no >= halving*10 :
    nexthalving = halving*11 - block_no
    reward = 4822813
if block_no >= halving*11 :
    nexthalving = halving*12 - block_no
    reward = 2441406
if block_no >= halving*12 :
    nexthalving = halving*13 - block_no
    reward = 1220703
if block_no >= halving*13 :
    nexthalving = halving*14 - block_no
    reward = 610352
if block_no >= halving*14 :
    nexthalving = halving*15 - block_no
    reward = 305176
if block_no >= halving*15 :
    nexthalving = halving*16 - block_no
    reward = 152588
if block_no >= halving*16 :
    nexthalving = halving*17 - block_no
    reward = 76294
if block_no >= halving*17 :
    nexthalving = halving*18 - block_no
    reward = 38147
if block_no >= halving*18 :
    nexthalving = halving*19 - block_no
    reward = 19073
if block_no >= halving*19 :
    nexthalving = halving*20 - block_no
    reward = 9537
if block_no >= halving*20 :
    nexthalving = halving*21 - block_no
    reward = 4768
if block_no >= halving*21 :
    nexthalving = halving*22 - block_no
    reward = 2384
if block_no >= halving*22 :
    nexthalving = halving*23 - block_no
    reward = 1192
if block_no >= halving*23 :
    nexthalving = halving*24 - block_no
    reward = 596
if block_no >= halving*24 :
    nexthalving = halving*25 - block_no
    reward = 298
if block_no >= halving*25 :
    nexthalving = halving*26 - block_no
    reward = 149
if block_no >= halving*26 :
    nexthalving = halving*27 - block_no
    reward = 75
if block_no >= halving*27 :
    nexthalving = halving*28 - block_no
    reward = 37
if block_no >= halving*28 :
    nexthalving = halving*29 - block_no
    reward = 19
if block_no >= halving*29 :
    nexthalving = halving*30 - block_no
    reward = 9
if block_no >= halving*30 :
    nexthalving = halving*31 - block_no
    reward = 5
if block_no >= halving*31 :
    nexthalving = halving*32 - block_no
    reward = 2
if block_no >= halving*32 :
    nexthalving = halving*33 - block_no
    reward = 1
if block_no >= halving*33 :
    # ????
    nexthalving = 0
    reward=0
## Calculate fees by subtracting expected reward from miner assigned reward
thetx = vtx[0]
vout = thetx.vout
vo = vout[0]
rewarded = vo.nValue
fees = rewarded-reward
## Calulate blocks until difficulty change
tmp_block_no = block_no
while tmp_block_no >= 0 :
    tmp_block_no = tmp_block_no - diffadjust
diffchange = tmp_block_no+diffadjust
diffchange = diffadjust-diffchange
if diffchange == 0 :
    diffchange = diffadjust
    newdiff = block_diff
    
## Loop the tx's and total the outputs ...
for x in range (0, tx_count) :  # so we loop the transactions
    thetx = vtx[x] # grabbing the CTransaction object
    vout = thetx.vout # grabbing the CTxOut object
    if len(vout) >= 1 :  
        for y in range (0,len(vout)) : # loops the outputs
            vo = vout[y] #grabbing each one as we go
            if vo.is_valid() : # check its valid
                if vo.nValue > 0 : # and has a value
                    outputs = outputs + vo.nValue # then we add it to total
## Build the output string with our data
txt1 = "#Bitcoin #block: " + str(block_no)
txt1 = txt1 + "\nOutputs: " + btcformat(outputs)  + " BTC"
if outputs == reward :
        txt1 = txt1 + "\n\n#emptyblock\n"
else :
        txt1 = txt1 + "\nFees: " + btcformat(fees) + " BTC"
        txt1 = txt1 + "\nTx: " + str(tx_count)
if diffchange != 2016 :
        txt1 = txt1 + "\nDiff Adj. in " + str(diffchange) + " blocks."
txt1 = txt1 + "\nBlock Time: " + str(btime)       
        
txt2 = ""
if reward == 0 :
    txt2 = txt2 + "REWARD ERA COMPLETE - LEVEL UP!"
    txt2 = txt2 + "\nNew Reward = " + btcformat(reward) + " BTC"
txt3 = ""
if diffchange == 2016 :
    txt3 = txt3 + "\nDifficulty adjustment!"
    txt3 = txt3 + "\nHalvening in " + str(nexthalving) + " blocks."
reply1 = "Block Hash:\n" + str(bhash)
reply2 = "Merkel Root:\n" + str(mroot)
reply3 = "Previous Block Hash:\n" + str(pbhash)   
BitFury = "Bitfury/SEGWIT"
AntPool = "Mined by AntPool"
ViaBTC = "ViaBTC"
Bitcoincom = "pool.bitcoin.com"
BWPool =  "BW Pool"
btctop = "BTC.TOP"
BitClubNetwork = "BitClub Network"
slush = "slush"
Bixin = "Bixin"
Canoe = "CANOE"
batpool  =" BATPOOL"
btcc = "BTCC"
## Get the block message    
thetx = vtx[0] 
vin = thetx.vin
vi = vin[0] 
vip = vi.scriptSig
vip=str(vip)
if vip.find(BitFury) != -1 :
    txt5 = "Mined by: BitFury SEGWIT"
if vip.find(AntPool) != -1 :
    txt5 = "Mined by: AntPool"
if vip.find(ViaBTC) != -1 :
    txt5 = "Mined by: ViaBTC"
if vip.find(Bitcoincom) != -1 :
    txt5 = "Mined by: pool.bitcoin.com"
if vip.find(BWPool) != -1 :
    txt5 = "Mined by: BWPool"
if vip.find(btctop) != -1 :
    txt5 = "Mined by: BTC.TOP"
if vip.find(BitClubNetwork) != -1 :
    txt5 = "Mined by: BitClub Network"
if vip.find(slush) != -1 :
    txt5 = "Mined by: Slush"
if vip.find(Bixin) != -1 :
    txt5 = "Mined by: Bixin"
if vip.find(Canoe) != -1 :
    txt5 = "Mined by: CANOE"
if vip.find(batpool) != -1 :
    txt5 = "Mined by: BATPOOL"
if vip.find(btcc) != -1 :
    txt5 = "Mined by: BTCC"
## Now we can tell everyone what we found
t1 = twitter.update_status(status=txt1)
#time.sleep(5)
r1 = twitter.update_status(status=reply1, in_reply_to_status_id=t1['id'])
r2 = twitter.update_status(status=reply2, in_reply_to_status_id=r1['id'])
r3 = twitter.update_status(status=reply3, in_reply_to_status_id=r2['id'])
## only show difficulty if we can id miner
if len(txt5) >=1 :
    reply4 = txt5
    reply4 = reply4 + "\nDifficulty: " + str(bdiff)
    reply4 = reply4 + "\nVersion: " + str(block_info.nVersion)
    r4 = twitter.update_status(status=reply4, in_reply_to_status_id=r3['id'])
if len(txt2) >=1 :
    twitter.update_status(status=txt2)
if len(txt3) >=1 :
    twitter.update_status(status=txt3)