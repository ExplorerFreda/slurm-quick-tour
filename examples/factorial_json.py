import copy
import dotdict
import sys
from factorial import F
from hyperparam import search_hyperparams

if __name__ == '__main__':
    idx = int(sys.argv[1])
    meta_configs = dotdict.DotDict(
        {
            'n': {
                'values': [3, 4, 5],
                'flag': None
            },
            'plus_one': {
                'values': [True, False],
                'flag': None
            }
        }
    )
    config_list = list(search_hyperparams(meta_configs))
    configs = config_list[idx]
    print(F(**configs))