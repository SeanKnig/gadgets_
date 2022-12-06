async def fetch_insert(json, table_name):
    import json, unicodedata
    TABLE_NAME = table_name

    sqlstatement = ''

    keylist = "("
    valuelist = "("
    firstPair = True
    for key, value in json.items():
        if not firstPair:
            keylist += ", "
            valuelist += ", "
        firstPair = False
        keylist += key
        if type(value) in (str, unicodedata):
            valuelist += "'" + value + "'"
        else:
            valuelist += str(value)
    keylist += ")"
    valuelist += ")"

    sqlstatement += "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist +";"+"\n"
    return(sqlstatement)
