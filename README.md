# cumulusvxbreakout
Cumulus VX script to support breakout devices

This allows devices such as S5248F etc to support the breakout of the 100G links into 4 links.
This means the device needs a lot more network interfaces, #
so for an S5232F you have 32 100G + 1 mgmt =33 ports = so breakout swp1s2 becomes interface swp33 (as mgmt is eth0), so in total 128 +1 interfaces are needed
so if you have an S5248F it has 48 25G + 6 100G network interfaces (& 2 not seen) + 1 mgmt = 57 interfaces required now with breakouts we need 
now the system is simple so the first breakout is assigned to swp57 ( as 56 normal + 1 eth0) but the first port cant breakout in realterms but system doesnt know this so it needs 56*4 interfaces = 225 configured
