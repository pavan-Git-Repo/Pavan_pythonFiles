if __name__ == '__main__':
    names = []
    scores = []
    dict_input = {} 
    
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        names.append(name)
        scores.append(score)
        dict_input[names] = scores
        second_lowest = list(set(sorted(score)))[1]
        print(second_lowest)