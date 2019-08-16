for para in doc.paragraphs:
    text = para.text
    email_list = re.findall (r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
    phone_list = re.findall (r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]',text)
    
    for email in email_list:
        emails.append(email)
    
    for phone in phone_list:
        phones.append(phone)
        
    for run in para.runs:
        if run.bold :
            bolds.append(run.text)
