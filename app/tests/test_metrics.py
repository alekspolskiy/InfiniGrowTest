from app.main import get_data_from_json, write_to_json
from app.metrics import create_metrics_dataset_v1, create_metrics_dataset_v2


class TestMetrics:
    def setup(self):
        self.metrics_data = get_data_from_json("app/data/metrics.json")

    def test_metrics_v1(self):
        metrics_expected = get_data_from_json("app/tests/data/metrics_expected.json")

        write_to_json(
            json_data=create_metrics_dataset_v1(
                data=get_data_from_json(
                    path="app/data/metrics.json"
                )
            ),
            path='app/data/metrics_result_v1.json'
        )

        metrics_result = get_data_from_json("app/data/metrics_result_v1.json")
        assert metrics_result == metrics_expected, "Metrics v1 failed"

    def test_metrics_v2(self):
        metrics_expected = get_data_from_json("app/tests/data/metrics_expected.json")

        write_to_json(
            json_data=create_metrics_dataset_v2(
                data=get_data_from_json(
                    path="app/data/metrics.json"
                )
            ),
            path='app/data/metrics_result_v2.json'
        )

        metrics_result = get_data_from_json("app/data/metrics_result_v2.json")
        assert metrics_result == metrics_expected, "Metrics v2 failed"
