def solution(players, callings):
    rank_dict = {}
    player_dict = {}
    for i in range(len(players)):
        player_dict[players[i]] = i
        rank_dict[i] = players[i]

    for call in callings:
        rank = player_dict[call]
        
        target_rank = rank - 1
        target_call = rank_dict[target_rank]
        
        player_dict[call], player_dict[target_call] = player_dict[target_call], player_dict[call]
        rank_dict[rank], rank_dict[target_rank] = rank_dict[target_rank], rank_dict[rank]
        
    return list(rank_dict.values())