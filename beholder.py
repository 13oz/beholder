#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Process arguments...')
parser.add_argument('--api_key', type='str', help='Add your SHODAN API key to connect to SHODAN search engine')
parser.add_argument('--config_file', help='Add search config file')


def connectShodan(api_key='foo'):
	return 0

if __name__ == "__main__":
	connectShodan