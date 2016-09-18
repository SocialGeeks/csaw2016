# mfw

Hey, I made my first website today. It's pretty cool and web7.9.

http://web.chal.csaw.io:8000/

--

Found an exposed .git directory.  

Used DVCS-Pillage to pull down files. 

https://github.com/evilpacket/DVCS-Pillage

After reviewing the code an injection vulnerability was found in both assert
statements in index.php  Arbitrary PHP code could be executed at this point.
The flag was in the source code of templates/flag.php

http://web.chal.csaw.io:8000/?page=%27)%20%7C%7Creadfile(%27templates/flag.php%27)%7C%7C%20strpos(%27

flag{3vald_@ss3rt_1s_best_a$$ert}

