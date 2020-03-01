import os
import json


def filepath(filename):
    return '{}/{}'.format(
        os.path.dirname(os.path.realpath(__file__)),
        filename
        )


def load_config():
    try:
        with open(filepath('config.json')) as f:
            config = json.load(f)
    except:
        config = []
    finally:
        return config


def main():
    pass


if __name__ == "__main__":
    main()
