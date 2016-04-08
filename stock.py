import csv


stock_dict = dict()
date_dict  = dict()

def stock_fun( search_str ):
    
    stock_dict[ search_str ] = [ ]
    
    print( type( search_str ) )
    print( search_str )
    
    for year in [ '2012' ]:

        for month in range( 1, 13, 1 ):
            
            month_str = '{:02d}'.format( month )
        
            filename = 'otc_' + year + month_str          
            
            try:
        
                with open( filename + '.csv', 'r', encoding = 'utf8' ) as csv_file:

                    stock = csv.DictReader( csv_file )

                    for line in stock:
                        print( '123' )
                                
                        if( line['公司代號'] == search_str ):
                            print( line[ '公司名稱' ], year + month_str + '當月營收', line['當月營收'] )                       
                            date_dict[ year + '{:02d}'.format( month ) ] = line['當月營收']
                            break
                        
            except:
                print( filename + '.csv is not exist' )     
            
            stock_dict[ search_str ].append( date_dict )          
  
    #print( stock_dict.items() )
    #print( stock_dict.get( search_str  ) )