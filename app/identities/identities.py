from app.utils import get_unique_values


def merge_identities(data):

    keys = get_unique_values([j for i in data for j in i.keys()])

    def get_values(key):
        return get_unique_values([i[key] for i in data if i[key]])

    values = list(map(get_values, keys))
    return [
        {
            key: values[num]
            for num, key in enumerate(keys)
        }
    ]
