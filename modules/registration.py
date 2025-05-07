import re 

def validation_code(code):
    pattern = r'^L[0-9]{2}$'
    return bool(re.match(pattern, code))

def defensive_code(name, services_code):
    if not name:
        raise ValueError("Nama tidak boleh kosong")
    if not validation_code(services_code):
        raise ValueError("Kode harus sesuai format LXX")
    
    return {
        'name': name,
        'services_code': services_code
    }



