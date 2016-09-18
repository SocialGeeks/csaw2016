#!/usr/bin/env python2

from pwn import *
from decimal import Decimal

def how_many(change, amount):
    i = 0
    remainder = float(change)
    count = 0
    if Decimal(str(change)) >= Decimal(str(amount)):
        count, remainder = divmod(Decimal(str(change)), Decimal(str(amount)))
    return int(count), remainder

def calculate_dispersment(change):
    cash = []
    remainder = float(change)
    count, remainder = how_many(remainder, 10000.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 5000.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 1000.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 500.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 100.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 50.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 20.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 10.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 5.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 1.0)
    cash.append(str(count))
    count, remainder = how_many(remainder, 0.5)
    cash.append(str(count))
    count, remainder = how_many(remainder, 0.25)
    cash.append(str(count))
    count, remainder = how_many(remainder, 0.10)
    cash.append(str(count))
    count, remainder = how_many(remainder, 0.05)
    cash.append(str(count))
    count, remainder = how_many(remainder, 0.01)
    cash.append(str(count))
    return cash


def send_answers(cash):
    r.recvuntil('$10,000 bills: ')
    r.sendlinethen('$5,000 bills: ', cash[0])
    r.sendline(cash[1])
    r.recvuntil('$1,000 bills: ')
    r.sendline(cash[2])
    r.recvuntil('$500 bills: ')
    r.sendline(cash[3])
    r.recvuntil('$100 bills: ')
    r.sendline(cash[4])
    r.recvuntil('$50 bills: ')
    r.sendline(cash[5])
    r.recvuntil('$20 bills: ')
    r.sendline(cash[6])
    r.recvuntil('$10 bills: ')
    r.sendline(cash[7])
    r.recvuntil('$5 bills: ')
    r.sendline(cash[8])
    r.recvuntil('$1 bills: ')
    r.sendline(cash[9])
    r.recvuntil('half-dollars (50c): ')
    r.sendline(cash[10])
    r.recvuntil('quarters (25c): ')
    r.sendline(cash[11])
    r.recvuntil('dimes (10c): ')
    r.sendline(cash[12])
    r.recvuntil('nickels (5c): ')
    r.sendline(cash[13])
    r.recvuntil('pennies (1c): ')
    r.sendline(cash[14])
    print r.recvline()

r = remote('misc.chal.csaw.io', 8000)

rounds = 0
while True:
    rounds += 1
    change = float(r.recvline(keepends=False)[1:])
    print "Round %d" % rounds
    print "change: %s" % change
    send_answers(calculate_dispersment(change))
