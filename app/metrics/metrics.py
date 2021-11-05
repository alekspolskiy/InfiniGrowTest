def create_metrics_dataset_v1(data):
    unique_filters = []
    for obj in [i for i in data["metricsCustomFilters"].values()]:
        if obj not in unique_filters:
            unique_filters.append(obj)

    return [
        {
            "metrics": [metric for metric in data["metricsCustomFilters"].keys()
                        if data["metricsCustomFilters"][metric] == unique_filter],
            "filters": unique_filter

        }
        for unique_filter in unique_filters
    ]


def create_metrics_dataset_v2(data):
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
        res_dict["filters"] = unique_filter
        return res_dict

    return list(map(generator, unique_filters))
