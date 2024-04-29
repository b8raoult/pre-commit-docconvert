import argparse
import logging

from docconvert import configuration, core


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--style", help="The output style to use.", default="google")
    parser.add_argument("files", nargs="+", help="The files to convert.")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s:%(levelname)s: %(message)s",
    )

    config = configuration.DocconvertConfiguration.create_default()

    logging.info("Using output style: %s", args.style)

    config.output_style = args.style

    for path in args.files:
        core.convert(path, config=config, in_place=True)


if __name__ == "__main__":
    main()