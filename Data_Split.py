from logging.config import valid_ident
import time

value="$NR,ATOM000002,TRACKABOX1,ATOM000001__,0.00.01,00,00,L,863221042483816,A,171122,090754,000004,12.962927,N,080.252892,E,0.0,173.46,1,1.6,0.00,7.00,1,0000,0150,0,0,28,404,10,20,9767634,000000,000.0,000.0,000.0,921142010035,0000,0.000,0.000,0000,000017*04"
# "$CW,AG2T000028,TRACKABOX1,000000000000,2.02.03,02,SUCCESS,000093*74"

# "DC,0,0,0,0,0,0300,0,0300,0,0300,0,0300,60.00,0300,10.00,0,0300,10.00,0300,60.00,0,0,000000300,0300,0,300,0,300,300,0,000033,1,0,000300,000300,1,1,0040,45.00,1,0020,25.00,ATOM000001__,TRACKABOX1,64694E3E0E00,1,0,000073*07"


def d1(value):
    print(len(value))
    valid_id=value.split(",")
    print(valid_id)
    for i in range(0,len(valid_id)):
        print("Index|{}|Vlaue|{}|Len|{}|".format(str(i),valid_id[i],str(len(valid_id[i]) )))
    
    
d1(value=value)