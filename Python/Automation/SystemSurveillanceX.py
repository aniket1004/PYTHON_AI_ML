# Command line input
import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-" * 50
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
    fobj.write(Border + "\n")
    fobj.write("----- Marvellous Platform Surveillance System ----" + "\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    fobj.write("------------- System Report ------------\n")

    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    fobj.write(Border + "\n")

    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border + "\n")

    fobj.write("Disk Usage Report\n")
    fobj.write(Border + "\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass
    
    fobj.write(Border + "\n")
    
    net = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border + "\n")

    # Process Log
    Data = ProcessScan()
    fobj.write("\n\n{:<10} {:<48} {:<20} {:<15} {:<25} {:<20} {:<20}\n"
               .format("PID", "Name", "Username", "Status", "Create Time", "CPU Percent", "Memory Percent"))
    fobj.write(Border + Border + Border + Border + "\n")
    for info in Data:
        fobj.write("{:<10} {:<48} {:<20} {:<15} {:<25} {:<20} {:<20}\n"
                   .format(info.get("pid"),info.get("name"),info.get("username"),
                        info.get("status"),info.get("create_time"),info.get("cpu_percent"),info.get("memory_percent")))
        # fobj.write("PID : %s\n" % info.get("pid"))
        # fobj.write("Name : %s\n" % info.get("name"))
        # fobj.write("Username : %s\n" % info.get("username"))
        # fobj.write("Status : %s\n" % info.get("status"))
        # fobj.write("Start time : %s\n" % info.get("create_time"))
        # fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
        # fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("---------------- End of Log File -----------------" + "\n")
    fobj.write(Border + "\n")

def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter(attrs=["pid", "name", "username", "status",  "create_time"]):
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status",  "create_time"])
            # Convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))
            except :
                info["create_time"] = "NA"
            
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess
    
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
        CreateLog(sys.argv[2])
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