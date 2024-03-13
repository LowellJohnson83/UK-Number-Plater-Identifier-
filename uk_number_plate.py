print()

suffix_plate_1 = "ANG 314D"
suffix_plate_2 = "JON 3S"
suffix_plate_3 = "GH0 5T"
suffix_plate_4 = "KEN 1X"
suffix_plate_5 = "EDW 412D"
suffix_plate_6 = "RAC 3R"

prefix_plate_1 = "L4 URA"
prefix_plate_2 = "E12 ROR"
prefix_plate_3 = "G3 MMA"
prefix_plate_4 = "J46 UAR"
prefix_plate_5 = "X999 ROB"
prefix_plate_6 = "N16 GKM"

current_plate_1 = "YU11 MMY"
current_plate_2 = "OO07 RAY"
current_plate_3 = "XK03 JRC"
current_plate_4 = "SH21 RLZ"
current_plate_5 = "BO55 RPJ"
current_plate_6 = "AN63 LAJ"




reg_letters = ['A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'J', 'K',
               'L', 'M', 'N', 'P', 'R',
               'S', 'T', 'V', 'W', 'X',       
               'Y']

reg_suffix_letter = []
reg_suffix_year = []
reg_suffix_lst = []

reg_prefix_letter = []
reg_prefix_year = []
reg_prefix_lst = []

# Create Letter list for both suffix and prefix systems
for x in range(21):
    reg_suffix_letter.append(reg_letters[x])
    reg_prefix_letter.append(reg_letters[x])

# Plates 1963 to 1983 (letter / suffix system)
for x in range(5):
    reg_suffix_year.append(x + 1963 + 0.0)
for x in range(4, 21):
    reg_suffix_year.append(x + 1963 - 0.5)

# Plates 1983 to 2001 (letter / prefix system)
for x in range(16):
    reg_prefix_year.append(x + 1983 + 0.5)
for x in range (16, 20):
    reg_prefix_year.append((0.5 * x) + 1983 + 0.25 + 8)
for x in range(20, 21):
    reg_prefix_year.append((0.5 * x) + 1983 + 0.25 + 8)


plate = current_plate_6

def plate_parser(number):
    sys = ""
    date = ""
    number = str(number)
    plate_parsed = number.split()
    
    # print(plate_parsed)
    if plate_parsed[1][-2].isnumeric():
        # print("Suffix Digit Style Number Plate (1963 to 1983)")
        char = "" + plate_parsed[0]
        sys = "suffix letter"
    elif plate_parsed[0][1].isnumeric():
        # print("Prefix Digit Style Number Plate (1983 to 2002)")
        char = "" + plate_parsed[-1]
        sys = "prefix letter"
    elif plate_parsed[0][2].isnumeric() and plate_parsed[0][3].isnumeric():
        # print("Current Style Number Plate (2002 onwards)")
        char = "" + plate_parsed[0][2] + plate_parsed[0][3]
        sys = "'current' (post-2001)"

    if sys == "suffix":
        for l in range(len(reg_suffix_letter)):
            if char == reg_suffix_letter[l]:
                date = reg_suffix_year[l]
    elif sys == "prefix":
        for l in range(len(reg_suffix_letter)):
            if char == reg_prefix_letter[l]:
                date = reg_prefix_year[l]
    elif sys == "'current' (post-2001)":
        date = int(char) + 2000
        if int(char[0]) >= 5:
            date -= 50

    year = int(date)
    month = ""

    if date % 1 == 0:
        month = "January"
    elif date % 1 == 0.25:
        month = "March"
    elif date % 1 == 0.5:
        month = "Aug"
    elif date % 1 == 0.75:
        month = "September"

    return sys, year, month


def plate_identifier(number):
    
    pl_id = plate_parser(number)
    sys, year, month = pl_id[0], pl_id[1], pl_id[2]

    sentence = f"\nThis number plate is a {sys} number plate.\n\ The approximate registered date is {month} {year}.\n"
    
    return sentence


print(plate_identifier(current_plate_6))

