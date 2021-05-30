from services.poestashhistory import PoeStashHistoryService
import time
import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # argument parsing and overall setup here

    # Initializes Poe Stash Service
    service = PoeStashHistoryService()
    starttime = time.time()
    # TODO: Potentially add a Test Method to PoeStashHistoryService while in Development
    # Running Transaction processing in a loop
    while True:
        service.processRecords()
        time.sleep(15.0 - ((time.time() - starttime) % 15.0))


if __name__ == "__main__":
    sys.exit(main())