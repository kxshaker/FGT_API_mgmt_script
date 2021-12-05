# FGT_API
FGT API MGMT script <br/>

Python tool to interact with FGT firewall policy api for now

Arguments:
 
  -h, --help            show this help message and exit  <br/>
  -o, --old             Old Interface name  <br/>
  -n, --new             New Interface name  <br/>
  -d , --direction      DIRECTION Src/Dst Interface  <br/>
  -A, --ALL             All Policies to be updated  <br/>
  -p, --policy          One Policy to be updated must use -id if -p switch is used  <br/>
  -id, --id ID          Policy ID Number  <br/>
  -bk, --backup         Back up global config in current directory  <br/>
  -k, --key             {Key:value} pair name <br/>
  
  example: <br/>
  -o port1 port2 port3 port4 port5 -n virtual-wan-link -d dstintf -p -id 10 <br/>
  -o port1 port2 port3 -n SASE -d srcintf -A <br/>
  --backup  <br/>

![2021-12-04 10_06_04-cap](https://user-images.githubusercontent.com/57874692/144706144-7b85b85c-c175-4aa5-bf2d-74fe95884597.png)![2021-12-04 10_07_25-cap](https://user-images.githubusercontent.com/57874692/144706145-c6d98acb-897a-40f8-85a4-0f2cbf7db5b1.png)
![2021-12-04 10_21_19-cap](https://user-images.githubusercontent.com/57874692/144706146-bef12279-b46a-4929-8216-0dd6f49f9220.png)
![2021-12-04 11_08_36-cap](https://user-images.githubusercontent.com/57874692/144706147-25d54f6e-1944-4271-bd15-43aabdc38d0a.png)
![2021-12-04 11_09_53-cap](https://user-images.githubusercontent.com/57874692/144706148-7835b12c-73db-48c7-9890-3e3b6c262103.png)
![2021-12-04 11_11_22-cap](https://user-images.githubusercontent.com/57874692/144706149-fab11b49-080b-492b-9859-e8e04caf7fde.png)
![2021-12-04 11_11_50-cap](https://user-images.githubusercontent.com/57874692/144706150-ba5bf1b6-2998-467b-b93e-7e598c12f650.png)
![2021-12-04 11_13_49-cap](https://user-images.githubusercontent.com/57874692/144706152-1051a898-8616-40c5-ba6a-95f62db64857.png)
![2021-12-04 11_19_55-cap](https://user-images.githubusercontent.com/57874692/144706153-0ba5e4ad-f2a4-4b8d-9a26-41af66cc9749.png)
![2021-12-04 11_22_01-cap](https://user-images.githubusercontent.com/57874692/144706155-4810a162-32c2-47c5-94e7-a17d1f521355.png)
![2021-12-04 11_23_02-cap](https://user-images.githubusercontent.com/57874692/144706157-0b2879e9-b87e-443e-8814-919fe28b3b70.png)
![2021-12-04 11_27_20-cap](https://user-images.githubusercontent.com/57874692/144706158-117d4f4c-28a2-475d-a515-e3909cb7d586.png)
![2021-12-04 11_27_42-cap](https://user-images.githubusercontent.com/57874692/144706159-51542b4c-c212-4a09-9469-44d14313c6d1.png)
![2021-12-04 11_28_05-cap](https://user-images.githubusercontent.com/57874692/144706160-62274d2e-484c-43cd-b6a7-5667f87281c7.png)
![2021-12-04 11_33_19-cap](https://user-images.githubusercontent.com/57874692/144706163-4187f90b-0c13-4915-9fa4-6ba637dcc2ac.png)
![2021-12-04 11_33_39-cap](https://user-images.githubusercontent.com/57874692/144706164-da15be3b-87b6-47eb-be53-8952204f5178.png)
![2021-12-04 11_34_49-cap](https://user-images.githubusercontent.com/57874692/144706165-cfc40704-c59c-4516-a66e-f01706ac5c16.png)
![2021-12-04 11_35_46-cap](https://user-images.githubusercontent.com/57874692/144706167-354b6591-d87e-4439-a755-96546f6c16ce.png)
![2021-12-04 11_37_32-cap](https://user-images.githubusercontent.com/57874692/144706169-6ab9e2ff-8483-42e0-a28c-d78be6e454ca.png)
![2021-12-04 11_46_55-cap](https://user-images.githubusercontent.com/57874692/144706170-b5fec6f3-1fab-44ae-8cdd-7c422dfbbf30.png)
