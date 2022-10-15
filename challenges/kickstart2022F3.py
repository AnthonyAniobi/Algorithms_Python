def solve(test_case:int, num_days:int, seed_per_day:int, seeds:list):
    seed_quality = dict()
    for seed in range(len(seeds)):
        seed_quality[seed[2]/seed[1]] = seed
    sorted_quality = sorted(seed_quality.keys())
    
    plant_index = 0
    for n_d in range(num_days):
        for s_d in range(seed_per_day):
            plant_seed:bool = True
            while plant_seed:
                try:
                    pass
                except:
                    pass
    

test_case = int(input())
for t in range(test_case):
    num_days, seed_types, seed_per_day = [int(x) for x in input().split()]
    seeds = list()
    for seed in range(seed_types):
        seed = [int(s) for s in input().split()]
    print(solve(t+1, seed_per_day, num_days, seeds))