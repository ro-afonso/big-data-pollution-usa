from sys import stdin
import logging

last_id = None
last_county = None

def main():
    stdin.readline()
    for line in stdin:
        line = line.strip()
        id, county, state = line.split(':')
        if id != last_id or county != last_county:
            print(f"{id}:{state}")
            last_id = id
            last_county = county


if __name__ == '__main__':
    logging.basicConfig(filename='./map-reduce/debug.log', level=logging.DEBUG)
    main()