from datetime import datetime

def log_error(action = "runtime action", message = "unexpected error", **details_error):

    str_details_error = ""
    for key, value in details_error.items():
        str_details_error += f"\n[ ({key}) : {value}]"
    
    local_date_time = datetime.now().isoformat(timespec='minutes') 
    
    print(f"\n\n[{local_date_time}] action: {action}\nmessage: {message}\ndetails: {str_details_error}\n\n")