# Command line input
import psutil
import sys
import os
import time
import schedule
import SendMailer

def ProcessLog(FolderName, ReceiverEmail):
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
    fobj.write("\n\n{:<10} {:<50} {:<15} {:<15} {:<25} {:<15} {:<25} {:<15} {:<15}\n"
               .format("PID", "Name", "Username", "Status", "Create Time","No Of Threads", "No Of Open Files", "CPU Percent", "Memory Percent"))
    fobj.write(Border + Border + Border + Border + "\n")
    for info in Data:
        fobj.write("{:<10} {:<50} {:<15} {:<15} {:<25} {:<15} {:<25} {:<15} {:<15}\n"
                   .format(info.get("pid"),info.get("name"),info.get("username"),
                        info.get("status"),info.get("create_time"),info.get('no_of_threads'), info.get('no_of_open_files'),info.get("cpu_percent"),info.get("memory_percent")))
        
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write("\n\nTOP 10 Memory Consuming Processes")
    Sorted_Data = sorted(Data, key = lambda info : info.get('memory_percent'), reverse = True)
    Sorted_Data = Sorted_Data[:10]
    fobj.write("\n\n{:<10} {:<50} {:<15} {:<25} {:<20} {:<20} {:<20} {:<15}\n"
               .format("PID", "Name", "Username", "Memory Percent", "RSS (in MB)", "VMS (in MB)", "Status", "Create Time")
               )
    fobj.write(Border + Border + Border + Border + "\n")
    for info in Sorted_Data:
        fobj.write("{:<10} {:<50} {:<15} {:<25} {:<20} {:<20} {:<20} {:<15}\n"
                .format(info.get("pid"), info.get("name"), info.get("username"), info.get("memory_percent"),
                        info.get("rss"), info.get("vms"),info.get("status"),info.get("create_time"))
                )
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write("\n\nSummary of log file\n")
    fobj.write(f"Total Processes : {len(Data)}\n\n")

    fobj.write("TOP 10 CPU Usage Processes")
    fobj.write("\n\n{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n".format("PID", "Name", "Username", "CPU Percent", "Status", "Create Time"))
    top_cpu_usage_data = sorted(Data, key = lambda info : info.get("cpu_percent"), reverse= True)
    top_cpu_usage_data = top_cpu_usage_data[:10]
    for info in top_cpu_usage_data:
        fobj.write("{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n"
                .format(info.get("pid"), info.get("name"), info.get("username"), info.get("cpu_percent"),
                        info.get("status"),info.get("create_time"))
                )
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write("\n\nTOP 10 Memory Usage Processes")
    fobj.write("\n\n{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n".format("PID", "Name", "Username", "Memory Percent", "Status", "Create Time"))
    top_memory_usage_data = sorted(Data, key = lambda info : info.get("memory_percent"), reverse= True)
    top_memory_usage_data = top_memory_usage_data[:10]
    for info in top_memory_usage_data:
        fobj.write("{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n"
                .format(info.get("pid"), info.get("name"), info.get("username"), info.get("memory_percent"),
                        info.get("status"),info.get("create_time"))
                )
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write("\n\nTOP 10 Thread Count Processes")
    fobj.write("\n\n{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n".format("PID", "Name", "Username", "No of Threads", "Status", "Create Time"))
    top_num_of_threads_data = sorted(Data, key = lambda info : info.get("no_of_threads"), reverse= True)
    top_num_of_threads_data = top_num_of_threads_data[:10]
    for info in top_num_of_threads_data:
        fobj.write("{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n"
                .format(info.get("pid"), info.get("name"), info.get("username"), info.get("no_of_threads"),
                        info.get("status"),info.get("create_time"))
                )
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write("\n\nTOP 10 Most Open File Processes Processes")
    fobj.write("\n\n{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n".format("PID", "Name", "Username", "Open files", "Status", "Create Time"))
    top_open_files_data = sorted(Data, key = lambda info : info.get("no_of_open_files"), reverse= True)
    top_open_files_data = top_open_files_data[:10]
    for info in top_open_files_data:
        fobj.write("{:<10} {:<50} {:<15} {:<25} {:<20} {:<15}\n"
                .format(info.get("pid"), info.get("name"), info.get("username"), info.get("no_of_open_files"),
                        info.get("status"),info.get("create_time"))
                )
        fobj.write(Border + Border + Border + Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("---------------- End of Log File -----------------" + "\n")
    fobj.write(Border + "\n")

    fobj.close()

    sender_email = "aniketdhole.test@gmail.com"

    # App password generated from Google account
    app_password = "zsxdkkbrmszoytnh"

    # Your second email for testing
    receiver_email = ReceiverEmail

    subject = "Platform Surveillance System Alert"

    body = f"""
    Hello,
    Please find attached log of Platform Surveillance System Script.
    
    Regards,
    Aniket Dhole
    """
    attachments = [FileName]
    SendMailer.send_mail(sender_email, app_password, receiver_email, subject, body, attachments)

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
            info["no_of_threads"] = proc.num_threads()
            try:
                info["no_of_open_files"] = proc.num_fds()
            except PermissionError as pobj:
                info["no_of_open_files"] = 0
            except Exception as eobj:
                info["no_of_open_files"] = 0
            
            mem_full = proc.memory_info()
            if mem_full.rss is not None:
                info["rss"] = mem_full.rss / (1024 * 1024)
            if mem_full.vms is not None:
                info["vms"] = mem_full.vms / (1024 * 1024)

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
            print(f"{sys.argv[0]} TimeInterval DirectoryName ReceiverEmail")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")
            print("Email id : Email id where log will be send")
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u for more details")
    elif len(sys.argv) == 4:
        
        # python Demo.py 5 Marvellous
        print("Time Interval : ", sys.argv[1])
        print("Directory Name : ", sys.argv[2])

        #CreateLog(sys.argv[2])
        
        # Apply the schedular   
        ProcessLog(sys.argv[2], sys.argv[3])     
        schedule.every(int(sys.argv[1])).minutes.do(ProcessLog, sys.argv[2], sys.argv[3])
    
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