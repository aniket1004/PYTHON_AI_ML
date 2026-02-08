# Command line input
import sys
import os
import time
import schedule
import shutil
import hashlib
   
def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path, "rb")
    
    buffer = fobj.read(1024)
    
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1024)

    return hobj.hexdigest()
    # while True:
    #     data = fobj.read(1024)
    #     if not data:
    #         break
    #     else:
    #         hobj.update(data)

    # return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_files = []
    print("Creating the backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):

        for file in files:
            src_path = os.path.join(root, file) # Data/DirectoryScan_4.py
            relative = os.path.relpath(src_path, Source) # DirectoryScan_4.py
            dest_path = os.path.join(Destination, relative) # MarvellousBackup/DirectoryScan_4.py

            # print(src_path)
            # print(relative)
            # print(dest_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the file if it is new / updated
            if (not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files

def MarvellousDataShieldStart(Source = "Data"):
    BackupName = "MarvellousBackup"

    print("Backup Process Started Successfully at : ", time.ctime())
    files = BackupFiles(Source, BackupName)
    print("Report about the backup : ")
    for name in files:
        print(name)

def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Data Shield System ----")
    print(Border)

    if len(sys.argv) == 2 :
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to : ")
            print("1 : Takes auto backup at given time.")
            print("2 : Backup only new and updated files.")
            print("3 : Create an archiew of the backup periodically.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as ")
            print(f"{sys.argv[0]} TimeInterval SourceDirectory")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u for more details")
    # python Demo.py 5 Data
    elif len(sys.argv) == 3:
        
        print("Time Interval : ", sys.argv[1])
        print("Directory Name : ", sys.argv[2])
        
        # Apply the schedular
        MarvellousDataShieldStart(sys.argv[2])
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])
    
        print("Data Shield System started successfully")
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