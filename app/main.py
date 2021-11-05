import json


def get_data_from_json():
    with open("data/test1.json", "r") as file:
        json_data = json.load(file)
    return json_data


def write_to_json(json_data):
    with open('data/result.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def create_data_set(data):
    unique_filters = []
    for obj in [i for i in data["metricsCustomFilters"].values()]:
        if obj not in unique_filters:
            unique_filters.append(obj)

    def generator(unique_filter):
        res_dict = {
            "metrics": [],
            "filters": []
        }
        for metric, data_filter in data["metricsCustomFilters"].items():
            if unique_filter == data_filter:
                res_dict["metrics"].append(metric)
        res_dict["filters"].append(unique_filter)
        return res_dict

    return list(map(generator, unique_filters))


if __name__ == "__main__":
    write_to_json(create_data_set(get_data_from_json()))
