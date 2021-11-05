import json
from app.metrics import create_metrics_dataset_v1, create_metrics_dataset_v2
from app.identities import merge_identities


def get_data_from_json(path):
    with open(path, "r") as file:
        json_data = json.load(file)
    return json_data


def write_to_json(json_data, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # metrics v1
    write_to_json(
        json_data=create_metrics_dataset_v1(
            data=get_data_from_json(
                path="data/metrics.json"
            )
        ),
        path='data/metrics_result_v1.json'
    )
    # metrics v2
    write_to_json(
        json_data=create_metrics_dataset_v2(
            data=get_data_from_json(
                path="data/metrics.json"
            )
        ),
        path='data/metrics_result_v2.json'
    )
    write_to_json(
        json_data=merge_identities(
            get_data_from_json(
                path="data/identities.json"
            )
        ),
        path='data/merged_identities.json')
