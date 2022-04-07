import solana
import spl
import subprocess

def get_token_count_for_address(token_mint, wallet_address):
    resp = subprocess.Popen(["spl-token", "accounts", token_mint, "--owner", wallet_address], stdout=subprocess.PIPE)
    resp.wait()
    msg,err = resp.communicate()
    msg = str(msg, 'utf-8')
    if 'Balance' in msg:
        token_count = msg.splitlines()[2]
        return token_count
    if 'None' in msg:
        print('no token held')
        return 0
    else:
        print('error, cannot fetch balance')
        return None


token_mint = "4eFU1TAigNZtv4nyDcAsUTZfUUgK6bTdpFSQEgn2H2u6"

with open('airdrop.txt', 'r') as f: #r+ does the work of rw
    lines = set(f.readlines())
    lines = [line.strip() for line in lines]
    print(len(lines), 'to airdrop')
    for i, wallet_address in enumerate(lines):
        token_count = get_token_count_for_address(token_mint, wallet_address)
        
        if token_count != 0 or token_count == None:
            print('we dont airdrop ', wallet_address)
        
        else:
            print('airdropping 1 token to ', wallet_address)
            resp = subprocess.Popen(["spl-token", "transfer", "--fund-recipient", "--allow-unfunded-recipient" , token_mint, "1", wallet_address, '--no-wait'], )
            resp.wait()
        
