#!/usr/bin/env python2

from pwn import *


def calculate_dispersment(change):
    cash = []
    cash.append('0') # 10,000
    cash.append('0') # 5,000
    cash.append('0') # 1,000
    cash.append('0') # 500
    cash.append('0') # 100
    cash.append('0') # 50
    cash.append('0') # 20 
    cash.append('0') # 10
    cash.append('0') # 5 
    cash.append('0') # 1 
    cash.append('0') # .50

    remainder = float(change)
    if float(change) >= 0.25:
        cash.append('1')
        remainder = remainder % .1
    else:
        cash.append('0')

    if float(change) >= 0.1:
        cash.append('1')
        remainder = remainder % .1
    else:
        cash.append('0')

    if remainder >= .05:
        cash.append('1')
        remainder = remainder % .05
    else:
        cash.append('0')

    print "remainder: %s" % remainder
    remainder = remainder * 100.0
    print "remainder: %s" % int(remainder)
    cash.append(str(int(remainder)))
    return cash


def send_answers(cash):
    print r.recvuntil('$10,000 bills: ')
    r.sendlinethen('$5,000 bills: ', cash[0])
    r.sendline(cash[1])
    print r.recvuntil('$1,000 bills: ')
    r.sendline(cash[2])
    print r.recvuntil('$500 bills: ')
    r.sendline(cash[3])
    print r.recvuntil('$100 bills: ')
    r.sendline(cash[4])
    print r.recvuntil('$50 bills: ')
    r.sendline(cash[5])
    print r.recvuntil('$20 bills: ')
    r.sendline(cash[6])
    print r.recvuntil('$10 bills: ')
    r.sendline(cash[7])
    print r.recvuntil('$5 bills: ')
    r.sendline(cash[8])
    print r.recvuntil('$1 bills: ')
    r.sendline(cash[9])
    print r.recvuntil('half-dollars (50c): ')
    r.sendline(cash[10])
    print r.recvuntil('quarters (25c): ')
    r.sendline(cash[11])
    print r.recvuntil('dimes (10c): ')
    r.sendline(cash[12])
    print r.recvuntil('nickels (5c): ')
    r.sendline(cash[13])
    print r.recvuntil('pennies (1c): ')
    r.sendline(cash[14])
    print r.recvline_contains('correct')

r = remote('misc.chal.csaw.io', 8000)

while True:
    change = float(r.recvline(keepends=False)[1:])
    print "change: %s" % change
    print change    
    send_answers(calculate_dispersment(change))
