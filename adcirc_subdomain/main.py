from adcirc_subdomain.parser import *
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="adcirc_subdomain",
        description="Create a new file fort.14.renum which contains renumbered nodes from fort.14"
    )

    parser.parse_args()

    f14 = Fort14("fort.14")
    f14.write("fort.14.renum")


if __name__ == "__main__":
    main()
