import time




min_data=int(input("Please input min data : "))
sec_data=int(input("please input sec data : "))

sec_count=min_data*60+sec_data

if min_data <= 2 and min_data >= 0:
    endtime = time.asctime( time.localtime(time.time()+ sec_count) )
    print("time out at ",endtime[11:19])

if min_data >=3:
    print("wait......")
    time.sleep(sec_count-3*60)
    endtime = time.asctime( time.localtime(time.time()+ 3*60) )
    print("time out at ",endtime[11:19])



