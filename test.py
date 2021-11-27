headers = ["Daily", "Status"]
data = [
    ['header1', 'status'],
    ['header2', 'status'],
    ['header3', 'status'],
] 

format_row = "{:>12}" * (len(headers) + 1)

print(format_row.format(*headers))
