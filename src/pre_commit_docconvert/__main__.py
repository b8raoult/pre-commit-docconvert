import argparse

from docconvert import configuration, core


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--style", help="The output style to use.", default="google")
    parser.add_argument("files", nargs="+", help="The files to convert.")
    args = parser.parse_args()

    config = configuration.DocconvertConfiguration.create_default()

    config.output_style = args.style

    for path in args.files:
        core.convert(path, config=config, in_place=True, threads=1)


if __name__ == "__main__":
    main()
