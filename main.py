from services.poestashhistory import PoeStashHistoryService
from services.poestashanalysis import PoeStashAnalysisService
import time
import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # argument parsing and overall setup here

    # Initializes Poe Stash Service
    stashService = PoeStashHistoryService()
    analysisService = PoeStashAnalysisService()
    starttime = time.time()
    # Running Transaction processing in a loop
    while True:
        stashService.processRecords()
        time.sleep(5)
        analysisService.analyseRecords()
        time.sleep(86400.0 - ((time.time() - starttime) % 86400.0))


if __name__ == "__main__":
    sys.exit(main())