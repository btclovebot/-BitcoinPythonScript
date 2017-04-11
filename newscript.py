#!/usr/bin/env python

## Create a proxy object and connect to the bitcoin.rpc
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()
import math
from twython import Twython

#Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''

## Grab the block and its number
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))
block_no = myproxy.getblockcount()

## Grab data from the block
vtx = block_info.vtx 
block_diff = block_info.difficulty
tx_count = len(vtx)
#block_nonce = block_info.nNonce

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

## Build the output string
txt1 = "#bitcoin #blockchain #block " + str(block_no)

if reward == 0 :
	txt1 = txt1 + "\nREWARD ERA COMPLETE!."
else :
	txt1 = txt1 + " Reward: " + btcformat(reward) + " BTC"
	txt1 = txt1 + "\nHalvening in " + str(nexthalving) + " blocks."



#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
 

from coinmarketcap import Market
import json
coinmarketcap = Market()
s = coinmarketcap.ticker('bitcoin')

s = json.loads(s)

total_supply = s[0]['total_supply']

#8 chars to left of decimal point
#? chars to the right of decimal point

total_supply_str = str(total_supply)
total_left = total_supply_str[:8]
total_right = total_supply_str[9:] #as we dont care for the decimal point
adj_total_supply  = total_left + total_right
while len(adj_total_supply) < 16 :
		adj_total_supply = adj_total_supply + "0"

CoinCap = "Total Supply: " + btcformat(adj_total_supply)

## Output
s = twitter.update_status(status=txt1 + '\n' + CoinCap)

print s
