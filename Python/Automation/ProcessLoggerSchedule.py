# Command line input
import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Ret = False
    Ret = os.path.exists(FolderName)

    if Ret:
        Ret = os.path.isdir(FolderName)
        if not Ret:
            print("Unable to create folder")
            sys.exit(0)
    else:
        os.mkdir(FolderName)
        print("Directory for log created sucessfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)
    print("Log file gets created with name : ", FileName)
    
    fobj = open(FileName, "w")
    

def main():
    Border = "-" * 50
    print(Border)
    print("----- Marvellous Platform Surveillance System ----")
    print(Border)

    if len(sys.argv) == 2 :
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processes")
            print("5 : Store information about CPU usage")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u for more details")
    elif len(sys.argv) == 3:
        
        # python Demo.py 5 Marvellous
        print("Time Interval : ", sys.argv[1])
        print("Directory Name : ", sys.argv[2])

        #CreateLog(sys.argv[2])
        
        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])
    
        print("Platform Surveillance System started successfully")
        print("Directory created with name : ", sys.argv[2])
        print("Time interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u for more details")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

if __name__ == "__main__":
    main()