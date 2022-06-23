print("Welcome to the secret auction program.");
bids = {};

choice = "yes";
while choice == "yes":
    name = input("What is your name? ");
    bid = int(input("What is your bid? "));
    bids[name] = bid;
    choice = input("Are there any more bidders? yes/no: ");

max_bid = 0;
max_bidder = "";
for name in bids:
    if bids[name] > max_bid:
        max_bidder = name;
        max_bid = bids[name];
        

print("The highest bid is by",max_bidder,":",bids[max_bidder],"ruppees");