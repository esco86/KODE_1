def phrase_search(object_list: list, search_string: str) -> int:
    ...
    # type your code here
    search_string = search_string.lower()
    for x in object_list:
        if not x['slots']:
            if search_string in x['phrase'].lower():
                return x['id']
        
        phrase_arr = []
        s_index = x['phrase'].find('{') 
        e_index = x['phrase'].find('}')
        rep_word1 = x['phrase'][s_index:e_index+1]

        sn_index = x['phrase'].find('{', s_index+1)

        if sn_index==-1:
            if s_index==-1:
                if search_string in x['phrase'].lower():
                    return x['id']
           
            phrase_arr = [x['phrase'].replace(rep_word1,y) for y in x['slots']]

        else:
            en_index = x['phrase'].find('}',sn_index)
            
            rep_word2 = x['phrase'][sn_index:en_index+1]
            phrase_arr_tmp = []

            if not x['slots']:
                if search_string in x['phrase'].lower():
                    return x['id']

            slot_len = len(x['slots'])
            for i, sl in enumerate(x['slots']):
                if (i<slot_len//2):
                    phrase_arr_tmp.append(x['phrase'].replace(rep_word1,sl))
                else:
                    for y in phrase_arr_tmp:
                        phrase_arr.append(y.replace(rep_word2,sl))

        for y in phrase_arr:
            if search_string in y.lower():
                return x['id']

            # return phrase_arr


    return 0
    




if __name__ == "__main__":
    """ 
    len(object) != 0
    object["id"] > 0
    0 <= len(object["phrase"]) <= 120
    0 <= len(object["slots"]) <= 50
    """
    object = [
        {"id": 1, "phrase": "Hello world!", "slots": []},
        {"id": 2, "phrase": "I wanna {pizza}", "slots": ["pizza", "BBQ", "pasta"]},
        {"id": 3, "phrase": "Give me your power", "slots": ["money", "gun"]},
        {"id": 4,"phrase": "I wanna {eat} and {drink}", "slots": ["pizza", "BBQ", "sushi", "pepsi", "tea", "beer"]}
    ]


    assert phrase_search(object, 'i wanna pasta') == 2
    assert phrase_search(object, 'Give me your power') == 3
    assert phrase_search(object, 'Hello world!') == 1
    assert phrase_search(object, 'I wanna nothing') == 0
    assert phrase_search(object, 'Hello again world!') == 0
    assert phrase_search(object, 'I need your clothes, your boots & your motorcycle') == 0
    assert phrase_search(object, 'I wanna sushi and tea') == 4
    assert phrase_search(object, 'I wanna sushi and vodka') == 0

