# Command line input
import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import SendMailer
   
def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    # open the zip file
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)
    
    zobj.close()

    return zip_name

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

def GetFileExtension(FileName):
    Extension = None
    
    SplitList = FileName.split(".")
    if len(SplitList) > 1:
        Extension = "." + SplitList[ len(SplitList)- 1 ]

    return Extension

def GetIgnoreExtension():
    extension_ignored = []
    extension_file = ".extension_ignore"
    try:
        if os.path.exists(extension_file) and os.path.isfile(extension_file):
            fobj = open(extension_file, "r")
            extension_ignored = fobj.readlines()
            fobj.close()     
  
        
        for i in range(len(extension_ignored)):
            extension_ignored[i] = extension_ignored[i].replace("\n", "")

    except Exception as eobj:
        msg = str(eobj)

    return extension_ignored

def BackupFiles(Source, Destination):
    copied_files = []
    print("Creating the backup folder for backup process")


    os.makedirs(Destination, exist_ok=True)
    total_files = 0
    ignored_extensions = GetIgnoreExtension()
    #print(ignored_extensions)
    for root, dirs, files in os.walk(Source):

        for file in files:
            src_path = os.path.join(root, file) # Data/DirectoryScan_4.py
            
            relative = os.path.relpath(src_path, Source) # DirectoryScan_4.py
            dest_path = os.path.join(Destination, relative) # MarvellousBackup/DirectoryScan_4.py

            file_extension = GetFileExtension(src_path)
            #print(file_extension)
            if file_extension is not None:
                if ignored_extensions is not None and len(ignored_extensions) > 0:
                    if file_extension in ignored_extensions:
                        if os.path.exists(dest_path):
                            os.remove(dest_path)

                        continue

            # print(src_path)
            # print(relative)
            # print(dest_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            total_files += 1
            # Copy the file if it is new / updated
            if (not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files, total_files

def MarvellousDataShieldStart(Source = "Data", LogDirectory = "Logs", ReceiverEmail=""):
    Border = "-" * 50
    BackupName = Source + "_MarvellousBackup"
    LogFileName = ""

    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    LogFileName = "DataShieldLogMarvellous_%s.log" % timestamp
    if not os.path.exists(LogDirectory):
        os.mkdir(LogDirectory)
    
    LogFileName = os.path.join(LogDirectory, LogFileName)
    fobj = open(LogFileName, "w")
    fobj.write(Border + "\n")
    fobj.write("----------- Marvellous Data Shield System ----------\n")
    fobj.write(Border + "\n")

    fobj.write(f"\nBackup Process Started Successfully at : {time.ctime()}\n")
    
    files = None
    total_files = 0
    try:
        files, total_files  = BackupFiles(Source, BackupName)
        fobj.write(f"Total number of files found : {total_files}\n")
        fobj.write(f"Total number of files copied : {len(files) if files is not None else 0}\n")
    except Exception as eobj:
        fobj.write(str(eobj))
    
    zip_file = ""
    try:
        if files is not None:
            zip_file = make_zip(BackupName)
            zip_size = os.path.getsize(zip_file)
            fobj.write(f"Zip file has been successfully created as named : {zip_file}.\n")
            hobj = None
            try:
                hobj = open("history.log", "a")
                hobj.write(os.path.basename(zip_file) + "|" + time.ctime() + "|" + str(total_files) + "|" + str(zip_size) + "\n")
            except Exception as exception:
                fobj.write(str(exception))
            finally:
                if hobj is not None:
                    hobj.close()

    except Exception as eobj:
        fobj.write(str(eobj))

    fobj.write(f"Backup completed at : {time.ctime()}\n\n")

    fobj.write(Border + "\n")
    fobj.write("----------- Thank you for using our script -----------\n")
    fobj.write(Border + "\n")

    if fobj is not None and (not fobj.closed):
        fobj.close()

    if ReceiverEmail is not None and ReceiverEmail != "":
        sender_email = "aniketdhole.test@gmail.com"

        # App password generated from Google account
        app_password = "XXXXXXXXXXXX"

        # Your second email for testing
        receiver_email = ReceiverEmail

        subject = "Data Shield System Alert"

        body = f"""
        Hello,
        Please find attached log of Data Shield System Script.
        
        Regards,
        Aniket Dhole
        """
        attachements = []
        attachements.append(os.path.abspath(LogFileName))
        attachements.append(zip_file)

        SendMailer.send_mail(sender_email, app_password, receiver_email, subject, body, attachements)
        print(f"Email has been sent to {receiver_email}")
    else:
        print(f"Receiver email found empty/invalid")

def DisplayHistory():
    HistoryFileName = "history.log"
    if os.path.exists(HistoryFileName):
        fobj = open(HistoryFileName, "r")
        lines = fobj.readlines()

        print("{:<50} {:<28} {:<15} {:15}".format("Zip Name", "Created Date", "No of files", "Size (in bytes)"))
        print("-" * 120)
        if lines is not None and len(lines) > 0:
            for line in lines:
                parameters = line.split("|")
                if parameters is not None and len(parameters) == 4:
                    print("{:<50} {:<28} {:<15} {:15}".format(parameters[0], parameters[1],parameters[2], parameters[3]))

def RestoreZip(Source, Destination):
    if os.path.exists(Source) and os.path.isfile(Source):
        try:
            zobj = zipfile.ZipFile(Source, "r")
            os.makedirs(Destination, exist_ok=True)
            zobj.extractall(Destination)
            print("Zip file successfully restored/extracted in destination.")
        except Exception as eobj:
            print(str(eobj))
    else:
        print("There is no such a file")

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
            print("3 : Create an archieve of the backup periodically.")
            print("4 : It will be ignore extension files which added in .extension_ignore file.")
            print("4 : Maintain the history of all generated zip backup files.")
            print("4 : Send log and zip file through email to provided mail id.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as ")
            print(f"{sys.argv[0]} TimeInterval SourceDirectory")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")
            print("LogDirectory : Name of directory to store logs under it.")
            print("Receiver Mail ID : Mail id who you want sent log.")
            print("---------------------------------------------------")
            print(f"{sys.argv[0]} --history")
            print("Display backup history of zip files.")
        
        elif sys.argv[1].lower() == "--history":
            DisplayHistory()

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u for more details")
    elif len(sys.argv) == 4:
        if sys.argv[1].lower() == "--restore":
            RestoreZip(sys.argv[2], sys.argv[3])

    # python Demo.py 5 Data Logs abs@gmail.com
    elif len(sys.argv) == 5:
        
        print("Time Interval : ", sys.argv[1])
        print("Directory Name : ", sys.argv[2])
        
        # Apply the schedular
        #MarvellousDataShieldStart(sys.argv[2], sys.argv[3], sys.argv[4])
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2], sys.argv[3], sys.argv[4])

        print(Border)
        print("Data Shield System started successfully")
        print("Time interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

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