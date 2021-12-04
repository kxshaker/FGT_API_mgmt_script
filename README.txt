# FGT_API
FGT API MGMT script

Python tool to interact with FGT firewall policy api for now

Arguments:
 
  -h, --help            show this help message and exit
  -o, --old             Old Interface name
  -n, --new             New Interface name
  -d , --direction      DIRECTION Src/Dst Interface
  -A, --ALL             All Policies to be updated
  -p, --policy          One Policy to be updated must use -id if -p switch is used
  -id, --id ID          Policy ID Number
  -bk, --backup         Back up global config in current directory
  -k, --key             {Key:value} pair name
  
  example: -o port1 port2 port3 port4 port5 -n virtual-wan-link -d dstintf -p -id 10
           -o port1 port2 port3  -n SASE -d srcintf -A
           --backup

imgs/2021-12-04 10_06_04-cap.png
