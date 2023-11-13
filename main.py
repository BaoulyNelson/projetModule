from ilogger.ilogger import log, get_logs

if __name__ == "__main__":
    log("se yon mesaj erreur.", "ERROR")
    log("se yon mesaj avetisman an.", "WARNING")

    error_logs = get_logs("ERROR")
    warning_logs = get_logs("WARNING")

    print("Error Logs:")
    for log_entry in error_logs:
        print(log_entry.strip())

    print("\nWarning Logs:")
    for log_entry in warning_logs:
        print(log_entry.strip())
