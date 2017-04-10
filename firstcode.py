## Import the modules required
import bitcoin
import bitcoin.rpc
from twython import Twython

## Create a proxy object and connect to the bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

#Setting these as variables will make them easier for future edits
app_key =          ''
app_secret =       ''
oauth_token =          ''
oauth_token_secret =   ''

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

s = "CBlock Height: "

x = myproxy.getblockcount()

Z = s + str(x)

P1 = "Bitcoin nNonce: "

O = block_info.nNonce

C = P1 + str(O)

U = "Previous Block Hash: "

P2 = bitcoin.core.b2lx(block_info.hashPrevBlock)

P4 = U + str(P2)

twitter.update_status(status=Z + '\n' + C + '\n' + P4)

