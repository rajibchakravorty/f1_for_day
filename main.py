
from datetime import date

import calendar

import numpy as np


## assupmtion is that there is NO sklearn package available
## if there were:

## from sklearn.metrics import f1_score
## f1 = f1_score( true, pred )

def f1_score( true, pred ):

    true = np.array( true )
    pred = np.array( pred )

    true_pos_perf = pred[ true == 1 ]

    recall = sum( true_pos_perf )/float( len( true_pos_perf ) )

    pred_pos_perf = true[ pred == 1 ]

    precision = sum( pred_pos_perf ) / float( len( pred_pos_perf ) )

    #f1 by definition
    f1 = 2. * precision * recall / ( precision + recall )

    return f1

def collect_result( weekday, result_list ):

    y = []
    yhat = []

    for res in result_list:

        if res[0][0] == weekday:

            y.append( res[0][1] )
            yhat.append( res[0][2] )


    return y, yhat


def get_weekday_data( day_info ):

   #print day_info
   date_string = day_info[0]
   dt = [x for x in date_string.split( '-' )]
   year = int( dt[0] )
   mon  = int( dt[1] ) 
   day  = int( dt[2] )
   
   date_obj = date( year, mon, day )
   weekday = calendar.day_name[ date_obj.weekday()] 
   
   return (weekday, int( day_info[1] ), int( day_info[2] ) ) 
 

def read_csv( csv_file ):

    with open( csv_file ) as f:

        file_content = f.readlines()

    file_content = [x.strip() for x in file_content]

    file_content = file_content[2:]

    info = [[x.split('|')] for x in file_content]


    info = [ map(get_weekday_data, x) for x in info]

    return info

if __name__ == '__main__':

    f1_for_day = 'Thursday'

    result = read_csv( 'test.psv' )

    y, yhat = collect_result( f1_for_day, result )

    f1 = f1_score( y, yhat )

    print 'F1 for {0} {1}'.format( f1_for_day, f1 )
