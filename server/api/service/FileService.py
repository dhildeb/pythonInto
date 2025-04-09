from fastapi import HTTPException
import json
import logging

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            file_content = f.read().strip()
            file_data = json.loads(file_content)
    except Exception as e:
            logging.error(e)
            file_data = []

    return file_data 

def write_file(file_name, data):
    try:
        existing_data = read_file(file_name)
        existing_data.append(data) 

        with open(file_name, 'w') as f:
            json.dump(existing_data, f, indent=0) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File write error: {str(e)}") 
    
def override_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=0) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File override error: {str(e)}") 
    