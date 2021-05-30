from services import poestashhistory
import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # argument parsing and overall setup here

    # Initializes Poe Stash Service
    service = poestashhistory.PoeStashHistoryService()
    
    # TODO: Potentially add a Test Method to PoeStashHistoryService while in Development
    # Runs a full retrace as far back as the API allows for
    service.processRecords()

if __name__ == "__main__":
    sys.exit(main())