def get_matches_dict(df_x, df_y):
    # List values are (<key_equivalent_in_target_variable>, <matches>, <mismatches>)
    matches_dict = {
        'A': [1, 0, 0], 
        'B': [2, 0, 0], 
        'C': [3, 0, 0], 
        'D': [4, 0, 0]
    }
    
    for i, row in df_x.iterrows():
        for k, v in matches_dict.items():
            if row[f'ASIA - Admission_{k}'] == 1:
                if df_y[i] == v[0]:
                    v[1] += 1
                else:
                    v[2] += 1
                break
    
    return matches_dict

def display_matches_dict(df_x=None, df_y=None, matches_dict=None, only_rate=False):
    '''
    Must provide one of df_x/df_y OR matches_dict
    '''
    if matches_dict is None:
        matches_dict = get_matches_dict(df_x, df_y)

    for k, v in matches_dict.items():
        if not only_rate:
            print(f'ASIA {k} Matches:    {v[1]}')
            print(f'ASIA {k} Misses:     {v[2]}')
        print(f'ASIA {k} Match Rate: {round(v[1] / (v[1] + v[2]), 4)}')
    
    return matches_dict
