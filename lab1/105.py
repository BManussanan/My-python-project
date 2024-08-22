block_length = 12
block_width = 9
house_length = 7
house_width = 6

MOW_RATE = 35.0
blockcost = block_length*block_width*MOW_RATE
housecost = house_length*house_width*MOW_RATE
total = blockcost-housecost
print("Mowing cost is",total,"baht.")
