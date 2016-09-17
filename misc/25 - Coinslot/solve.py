#!/usr/bin/env python2

from pwn import *
from math import floor


def calculate_dispersment(change):
    cash = []
    # cash.append('0')  # 10,000
    # cash.append('0')  # 5,000
    # cash.append('0')  # 1,000
    # cash.append('0')  # 500
    # cash.append('0')  # 100
    # cash.append('0')  # 50
    # cash.append('0')  # 20
    # cash.append('0')  # 10
    # cash.append('0')  # 5
    # cash.append('0')  # 1
    # cash.append('0')  # .50
    remainder = float(change)
    if remainder >= 10000.00:
        extra = remainder % 10000.00
        number = float((remainder-extra)/10000.0)
        cash.append(mkInt(number))
        remainder = (remainder - (number * 10000.0)) % 10000.0
    else:
        cash.append('0')

    if remainder >= 5000.00:
        cash.append('1')
        remainder = remainder % 5000.00
    else:
        cash.append('0')

    if remainder >= 1000.00:
        extra = remainder % 1000.00
        number = float((remainder-extra)/1000.0)
        cash.append(mkInt(number))
        remainder = (remainder - (number * 1000.0)) % 1000.0
    else:
        cash.append('0')

    if remainder >= 500.00:
        cash.append('1')
        remainder = remainder % 500.00
    else:
        cash.append('0')

    if remainder >= 100.00:
        extra = remainder % 100.00
        number = float((remainder-extra)/100.0)
        cash.append(mkInt(number))
        remainder = (remainder - (number * 100.0)) % 100.0
    else:
        cash.append('0')

    if remainder >= 50.00:
        cash.append('1')
        remainder = remainder % 50.00
    else:
        cash.append('0')

    if remainder >= 20.00:
        extra = remainder % 20.00
        number = float((remainder-extra)/20.0)
        cash.append(mkInt(number))
        remainder = (remainder - (number * 20.0)) % 20.0
    else:
        cash.append('0')

    if remainder >= 10.00:
        cash.append('1')
        remainder = remainder % 10.00
    else:
        cash.append('0')

    if remainder >= 5.00:
        cash.append('1')
        remainder = remainder % 5.00
    else:
        cash.append('0')

    if remainder >= 1.00:
        extra = remainder % 1.00
        number = float((remainder-extra)/1.00)
        cash.append(mkInt(number))
        remainder = remainder % 1.00
        print remainder
    else:
        cash.append('0')

    if remainder >= 0.50:
        cash.append('1')
        remainder = remainder % 0.50
        print remainder
    else:
        cash.append('0')

    if remainder >= 0.25:
        cash.append('1')
        remainder = remainder % 0.25
        print remainder
    else:
        cash.append('0')

    if remainder >= 0.10:
        extra = remainder % 0.10
        number = float((remainder-extra)/0.10)
        cash.append(mkInt(number))
        remainder = remainder % 0.10
        print remainder
    else:
        cash.append('0')

    if remainder >= .05:
        cash.append('1')
        remainder = remainder % .05
        print remainder
    else:
        cash.append('0')

    print "remainder: %s" % remainder
    test = rmDec(remainder)
    print "remainder: "+test
    if test < 1:
        test = '0'
    cash.append(test)
    return cash


def mkInt(number):
    number = str(number).split(".")[0]
    if number == "":
        number = '0'
    return number


def rmDec(number):
    number = (str(number).split(".")[-1]).split("0")[-1]
    if number == "":
        number = '0'
    return number


def send_answers(cash):
    print r.recvuntil('$10,000 bills: ')
    r.sendlinethen('$5,000 bills: ', cash[0])
    r.sendline(cash[1])
    print(cash[1])
    print r.recvuntil('$1,000 bills: ')
    print(cash[2])
    r.sendline(cash[2])
    print r.recvuntil('$500 bills: ')
    print(cash[3])
    r.sendline(cash[3])
    print r.recvuntil('$100 bills: ')
    print(cash[4])
    r.sendline(cash[4])
    print r.recvuntil('$50 bills: ')
    print(cash[5])
    r.sendline(cash[5])
    print r.recvuntil('$20 bills: ')
    print(cash[6])
    r.sendline(cash[6])
    print r.recvuntil('$10 bills: ')
    print(cash[7])
    r.sendline(cash[7])
    print r.recvuntil('$5 bills: ')
    print(cash[8])
    r.sendline(cash[8])
    print r.recvuntil('$1 bills: ')
    print(cash[9])
    r.sendline(cash[9])
    print r.recvuntil('half-dollars (50c): ')
    print(cash[10])
    r.sendline(cash[10])
    print r.recvuntil('quarters (25c): ')
    print(cash[11])
    r.sendline(cash[11])
    print r.recvuntil('dimes (10c): ')
    print(cash[12])
    r.sendline(cash[12])
    print r.recvuntil('nickels (5c): ')
    print(cash[13])
    r.sendline(cash[13])
    print r.recvuntil('pennies (1c): ')
    print(cash[14])
    r.sendline(cash[14])
    print r.recvline_contains('correct')

r = remote('misc.chal.csaw.io', 8000)

while True:
    change = float(r.recvline(keepends=False)[1:])
    print "change: %s" % change
    print change
    send_answers(calculate_dispersment(change))
