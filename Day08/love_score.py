def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    t_count = 0
    r_count = 0
    u_count = 0
    e_count = 0
    l_count = 0
    o_count = 0
    v_count = 0
    true_count = 0
    love_count = 0
    true_love_count = ""
    
    for letter in name1:
        if letter == "t":
            t_count += 1
        if letter == "r":
            r_count += 1
        if letter == "u":
            u_count += 1
        if letter == "e":
            e_count += 1
        if letter == "l":
            l_count += 1
        if letter == "o":
            o_count += 1
        if letter == "v":
            v_count += 1

    for letter in name2:
        if letter == "t":
            t_count += 1
        if letter == "r":
            r_count += 1
        if letter == "u":
            u_count += 1
        if letter == "e":
            e_count += 1
        if letter == "l":
            l_count += 1
        if letter == "o":
            o_count += 1
        if letter == "v":
            v_count += 1
    true_count = t_count + r_count + u_count + e_count
    love_count = l_count + o_count + v_count + e_count
    true_love_count = str(true_count) + str(love_count)
    
    # print(f"T occurs {t_count} times")
    # print(f"R occurs {r_count} times")
    # print(f"U occurs {u_count} times")
    # print(f"E occurs {e_count} times")
    # print(f"TOTAL = {true_count}")
    
    # print(f"L occurs {l_count} times")
    # print(f"O occurs {o_count} times")
    # print(f"V occurs {v_count} times")
    # print(f"E occurs {e_count} times")
    # print(f"TOTAL = {love_count}")
    
    # print(f"Love Score {true_love_count}")
    print(true_love_count)

calculate_love_score("Angela Yu", "Jack Bauer")