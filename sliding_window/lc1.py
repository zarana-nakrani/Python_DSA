def countDays(days, meetings):
    new_list = sorted(meetings, key=lambda x: x[0])
    merged = []
    for i in range(len(new_list)):
        if i + 1 < len(new_list) and new_list[i][1] > new_list[i + 1][0] and new_list[i][1] < new_list[i + 1][1]:
            merged.append([new_list[i][0], new_list[i + 1][1]])
    return merged
print(countDays(10, [[5,7],[1,3],[9,10]]))