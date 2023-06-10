import sys
import yaml
import json


def main(payload: str) -> None:
    loaded_payload = json.loads(payload)

    payload_yaml = yaml.dump(loaded_payload)

    with open("_data/main.yaml", "r") as data_file:
        main_yaml = yaml.safe_load(data_file)

    main_yaml["events"] = main_yaml["events"] + [payload_yaml]

    with open("_data/main.yaml", "w") as data_file:
        yaml.dump(main_yaml, data_file, sort_keys=False)


if __name__ == "__main__":
    main(sys.argv[1])
