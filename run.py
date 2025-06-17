from balala import *

flush = Score(125, 16)

clubs_3_glass = Card("Clubs 3 (glass)", 3, mult_x=2)
clubs_3 = Card("Clubs 3 (glass)", 3)
clubs_A_mult = Card("Clubs Ace (mult)", 11, mult_plus=4)
clubs_K = Card("Clubs King", 10)
clubs_7 = Card("Clubs 7", 7)
clubs_4 = Card("Clubs 4", 4)

# blueprint on hanging chad ... 2 332 998
# evaluate(flush, [
#     clubs_3_glass,
#     HangingChad(clubs_3_glass), # blueprint
#     HangingChad(clubs_3_glass),
#     clubs_A_mult,
#     clubs_K,
#     clubs_7,
#     clubs_4,
#     Baron(),
#     Baron(),
#     Baron(),
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# blueprint on hanging chad, but no Campfire ... 2 332 998
evaluate(flush, [
    clubs_3_glass,
    HangingChad(clubs_3_glass), # blueprint
    HangingChad(clubs_3_glass),
    clubs_A_mult,
    clubs_K,
    clubs_7,
    clubs_4,
    Baron(),
    Baron(),
    Baron(),
    Foil(),
    Holographic(),
    DriversLicence()
])

# blueprint on hanging chad, but only one King ... 1 044 288 + 133 910 = 1 178 198
# evaluate(flush, [
#     clubs_3_glass,
#     HangingChad(clubs_3_glass), # blueprint
#     HangingChad(clubs_3_glass),
#     clubs_A_mult,
#     clubs_K,
#     clubs_7,
#     clubs_4,
#     Baron(),
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# blueprint on hanging chad, but it is the AK-47 setup :) ... 2 332 998
# evaluate(flush, [
#     clubs_3_glass,
#     HangingChad(clubs_3_glass), # blueprint
#     HangingChad(clubs_3_glass),
#     clubs_A_mult,
#     clubs_K,
#     clubs_4,
#     clubs_7,
#     Baron(),
#     Baron(),
#     Baron(),
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# blueprint on hanging chad, but no glass ... 200 406
# evaluate(flush, [
#     clubs_A_mult,
#     HangingChad(clubs_A_mult), # blueprint
#     HangingChad(clubs_A_mult),
#     clubs_3,
#     clubs_K,
#     clubs_4,
#     clubs_7,
#     Baron(),
#     Baron(),
#     Baron(),
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# blueprint on baron, but no glass ... 457 881
# evaluate(flush, [
#     clubs_A_mult,
#     HangingChad(clubs_A_mult),
#     clubs_3,
#     clubs_K,
#     clubs_4,
#     clubs_7,
#     Baron(), # blueprint
#     Baron(),
#     Baron(), # blueprint
#     Baron(),
#     Baron(), # blueprint
#     Baron(),
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# blueprint on hanging chad, no baron ... 700 632
# evaluate(flush, [
#     clubs_3_glass,
#     HangingChad(clubs_3_glass), # blueprint
#     HangingChad(clubs_3_glass),
#     clubs_A_mult,
#     clubs_K,
#     clubs_7,
#     clubs_4,
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# blueprint on baron ... 1 961 577
# evaluate(flush, [
#     clubs_3_glass,
#     HangingChad(clubs_3_glass),
#     clubs_A_mult,
#     clubs_K,
#     clubs_7,
#     clubs_4,
#     Baron(), # blueprint
#     Baron(),
#     Baron(), # blueprint
#     Baron(),
#     Baron(), # blueprint
#     Baron(),
#     Foil(),
#     Holographic(),
#     Campfire(x=2),
#     DriversLicence()
# ])

# old setup, no baron and no campfire ... 413 586
# evaluate(flush, [
#     Gluttonous(clubs_3_glass),
#     HangingChad(Gluttonous(clubs_3_glass)), # blueprint
#     HangingChad(Gluttonous(clubs_3_glass)),
#     Gluttonous(clubs_A_mult),
#     Gluttonous(clubs_K),
#     Gluttonous(clubs_7),
#     Gluttonous(clubs_4),
#     Foil(),
#     DriversLicence()
# ])
