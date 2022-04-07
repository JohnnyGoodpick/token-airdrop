# token-airdrop
Solana token airdrop python program - short and clear for people with some basic knowledge on Python

Too many messy airdrop program with 300+ lines of code, this one is simple and reliable

- Loop on wallet list 
- Check if wallet owns token
- If not => airdrop
- Done

Because solana network can be so bad especially when you want to mint, the program can be restarted and people won't receive the airdrop twice;
And ofc, we skip the validation waiting time, this allow a lightspeed airdrop

CAVEAT: If someone moves your airdrop token out of the wallet and you RESTART the script, it'll be airdropped again because it's not in their wallet anymore
but I guess that's a minor problem since airdrop is happening really fast in general.
Could be replaced by a check that search if there's an associated token account for this mint, but we might loses speed
