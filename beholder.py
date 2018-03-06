#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Process arguments...')


def connectShodan(api_key='foo'):
	return 0

if __name__ == "__main__":
	args = parser.parse_args()
	print(args.api)