#!/usr/bin/env python3

nmap = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
             90: 'Ninety', 0: 'Zero'}

def n2w(n):
    if n == 0: return ''
    if n == 1000: return 'One thousand'
    if n >= 100: 
        if n % 100 == 0: return f'{nmap[(n-n % 100) // 100]} hundred'
        else: return f'{nmap[(n-n % 100) // 100]} hundred and {n2w(n % 100).lower()}'
    if n > 20: return nmap[n -n % 10] + n2w(n % 10).lower()
    else: return nmap[n]

w = [n2w(i).replace(' ', '') for i in range(1, 1001)]
s = sum(map(lambda w: len(w.strip()), w))
print(s)