from streak import send_request
from operator import itemgetter

def write_message():
    teams = send_request()
    for team in sorted(teams, key=itemgetter('wins')):
        print("{:2d} {:14s} STREAK OF {}".format(
            team['wins'], team['name'], team['streak']
        ))

if __name__ == '__main__':
    write_message()
