from app.main import get_data_from_json, write_to_json
from app.identities import merge_identities


class TestIdentities:
    def setup(self):
        self.identities_data = get_data_from_json("app/data/identities.json")

    def test_identities(self):
        identities_expected = get_data_from_json("app/tests/data/identities_expected.json")

        write_to_json(
            json_data=merge_identities(
                get_data_from_json(
                    path="app/data/identities.json"
                )
            ),
            path='app/data/merged_identities.json')

        identities_result = get_data_from_json("app/data/merged_identities.json")
        assert identities_result == identities_expected, "Identities failed"
