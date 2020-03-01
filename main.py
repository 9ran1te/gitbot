import os


def filepath(filename):
    return '{}/{}'.format(
        os.path.dirname(os.path.realpath(__file__)),
        filename
        )


def load_config():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
