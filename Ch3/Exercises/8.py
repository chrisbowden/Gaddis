# Calculate the number of hot dog ingredients required

hotdogs_per_packet = 10
buns_per_packet = 8

people = int(input("How many people are attending the BBQ? "))
hotdogs_per_person = int(input("How many hotdogs per person? "))

hotdogs_needed = people * hotdogs_per_person
hotdog_packets_needed = (hotdogs_needed // hotdogs_per_packet) + 1
bun_packets_needed = (hotdogs_needed // buns_per_packet) + 1
leftover_hotdogs = hotdogs_needed % hotdogs_per_packet
leftover_buns = hotdogs_needed % buns_per_packet

print("The number of hotdog packets required will be", hotdog_packets_needed)
print("The number of bun packets required will be", bun_packets_needed)
print("There will be", leftover_hotdogs, "left over")
print("There will be", leftover_buns, "buns left over")
