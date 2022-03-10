# rank: 2,3,4,5,6,7,8,9,T,J,Q,K,A
# suit: c,d,h,s (clubs,diamonds,hearts,spades)
rank = "A"
suit = "s"
if (rank == "A") and (suit == "s"):
    print("First prize")    # ace of spades
elif rank == "A":          # any other ace
    print("Second prize")
else:
    print("No prize")