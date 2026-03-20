def find_duplicate_pans(records):
    pan_map = {}
    result = []

    for record in records:
        pan = record["pan"].strip()  # remove extra spaces
        if pan not in pan_map:
            pan_map[pan] = []
        pan_map[pan].append(record["application_id"])

    for record in records:
        pan = record["pan"].strip()
        if len(pan_map[pan]) > 1:
            result.append(record["application_id"])

    return result

records = [
 {"application_id": "APP001", "pan": "ABCDE1234F"},
 {"application_id": "APP002", "pan": "PQRST6789L"},
 {"application_id": "APP003", "pan": "ABCDE1234F"},
 {"application_id": "APP004", "pan": "ABCDE1234F "}
]

output = find_duplicate_pans(records)
print(output)