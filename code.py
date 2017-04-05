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

s = "Bitcoin CBlock Object Information: Block Height "

x = myproxy.getblockcount()

Z = s + str(x)

twitter.update_status(status=Z)

