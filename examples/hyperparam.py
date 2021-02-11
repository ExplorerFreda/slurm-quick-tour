import copy
import dotdict


def search_hyperparams(dictionary, current_hparams={}):
    if len(dictionary) == 0:
        yield copy.deepcopy(current_hparams)
        return
    current_dictionary = dict()
    current_key = list(dictionary.keys())[0]
    current_flag = dictionary[current_key].get('flag', None)
    if current_flag is not None:
        for key in copy.deepcopy(dictionary):
            if dictionary[key].get('flag', None) == current_flag:
                current_dictionary[key] = copy.deepcopy(dictionary[key])
                del dictionary[key]
    else:
        current_dictionary[current_key] = copy.deepcopy(
            dictionary[current_key]
        )
        del dictionary[current_key]
    num_values = len(current_dictionary[current_key]['values'])
    for key in current_dictionary:
        assert num_values == len(current_dictionary[key]['values']), \
            'hparams with the same flag must have the same #values\n' \
            'check {:s} and {:s}'.format(key, current_key)
    for i in range(num_values):
        for key in current_dictionary:
            current_hparams[key] = current_dictionary[key]['values'][i]
        for item in search_hyperparams(dictionary, current_hparams):
            yield item
    for key in current_dictionary:
        dictionary[key] = copy.deepcopy(current_dictionary[key])


if __name__ == '__main__':
    meta_configs_free = dotdict.DotDict(
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
    config_list_free = list(search_hyperparams(meta_configs_free))
    from IPython import embed; embed(using=False)

    meta_configs_bind = dotdict.DotDict(
        {
            'n': {
                'values': [3, 4, 5],
                'flag': 'group1'
            },
            'plus_one': {
                'values': [True, False, True],
                'flag': 'group1'
            }
        }
    )
    config_list_bind = list(search_hyperparams(meta_configs_bind))
    from IPython import embed; embed(using=False)
