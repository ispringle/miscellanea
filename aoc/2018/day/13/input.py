initial = """                 /-----------------------------⧵                                             /-------------------------------⧵                        
       /---------+-----------------------------+---------------------------------------------+--------------------⧵          |                        
       |         |            /----------------+------------------------------------------⧵  |                    |          |                        
       |         |            |                |                          /---------------+--+--------------⧵     |          |                        
       |         |            |  /-------------+-------------⧵            |               |  |              |     |          |                        
       |         |            |  |             |         /->-+------------+---------------+--+------------⧵ |     |          |                        
   /---+---------+----------⧵ |  |             |         |   |   /--------+---------------+--+----------⧵ | |     |         /+-------------------⧵    
   |   |         |          | |  |            /+---------+---+---+------<-+---------------+--+---------⧵| | |  /--+---------++---------------⧵   |    
   |   |    /----+--------<-+-+--+------------++---------+---+---+--------+---------------+--+---------++-+-+--+--+-⧵       ||               |   |    
   |   |    |    | /--------+-+--+---------⧵  ||         |   |   |        |     /---------+--+-⧵      /++-+-+--+-⧵| |       ||               |   |    
/--+---+----+----+-+--------+-+--+---------+--++---------+---+---+--------+-----+---------+--+-+-----⧵||| | |  | || |       ||               |   |    
|  |   |    |    | |    /---+-+--+---------+-⧵||      /--+---+---+--------+-----+---------+--+-+-----++++-+⧵|  | || |       ||               |   |    
|  |   |   /+----+-+----+--⧵|/+--+---------+-+++------+⧵ |   |   |        |     |         |  | |     |||| |||  | || |       ||               |   |    
|  |   |   ||    | |    |  ||||  |         | |||      || |   |   |        |     |      /--+--+-+-----++++-+++--+-++-+------⧵||               |   |    
|  |   |   ||    | |    |  ||||  |    /----+-+++------++-+---+---+--------+-----+------+--+--+-+-----++++-+++--+-++-+------+++-----------⧵   |   |    
|  |   |   ||    | |   /+--++++--+----+----+-+++-⧵    || |   |   |        |     |      |  |  | |     |||| |||  | || |      |||           |   |   |    
|  |   |   ||    ⧵-+---++--++++--+----+----+-++/ |    || |   |   |        |     |      |  |  | |     |||| |||  | || |      |||           |   |   |    
|  |   |   ||      |   ||  ||||  |    |    | ||  | /--++-+---+---+--------+-----+------+⧵ |  | |     |||| |||  | || |      |||           |   |   |    
|  |   |   ||      |   ||  ||||  |    |    | ||  | |  || |   |   |        ⧵-----+------++-+--+-+-----++++-++/  | || |      |||           |   |   |    
|  |   |   ||      |   ||  ||||  |    |    | ||  | |/-++-+---+---+--------------+------++-+--+-+-----++++-++---+⧵|| |      |||           |   |   |    
|  |   |   ||      |   |⧵--++++--+----+----+-/|  | || || |   |   |              |      || |/-+-+-----++++-++---++++-+------+++-----------+---+---+---⧵
|  |   |   ||      |   |   ||||/-+----+----+--+--+-++-++-+---+---+--------------+------++-++-+-+-----++++-++---++++-+---⧵  |||           |   |   |   |
|  |   |   ||      |   |   ||||| |    |    |  |  | || || |   |   |              |      || || ⧵-+-----++++-++---++++-+---+--++/           |   |   |   |
|  ⧵---+---++------+---+---+/||| | /--+----+--+--+-++-++⧵|   |   |         /----+------++-++---+-----++++-++---++++-+---+--++------------+---+⧵  |   |
|     /+---++------+---+---+-+++-+-+--+--⧵ |  |  | || ||||   |   |  /------+----+-⧵    || ||   |     |||| ||   |||| |   |  ||  /---------+---++--+-⧵ |
|     ||   ||      |   |   | ⧵++-+-+--+--+-+--+--+-++-+/||/--+---+--+------+----+-+----++-++---+-----++++-++---++++-+---+--++--+---------+⧵  ||  | | |
|     ||   ||      |   |   |  || | |  |  | |  |  | || | |||  |   |  |/-----+----+-+----++-++---+-----++++-++---++++-+---+⧵ ||  |         ||  ||  | | |
|     ||   ||      |   ⧵---+--++-+-+--+--+-+--+--/ || | |||  |   |  ||     |    | |    || ||   |     |||| ||   |||| |   || ||  |         ||  ||  | | |
⧵-----++---++------+-------+--++-+-+--+--+-+--+----++-+-+++--+---+--++-----+----+-+----++-++---+-----/||| ||   |||| |   || ||  |         ||  ||  | | |
      ||   ||      |       |  || |/+--+--+-+--+----++-+-+++--+---+--++⧵    |    | |/---++-++---+------+++-++⧵  |||| |   || ||  |         ||  ||  | | |
      ||   ||      |       |  || |||  |  | |  |    || | |||  |   |  |||    |    | ||   || ||   |      ||| |||  |||| |   || ||  |         ||  ||  | | |
      ||   ||      |       |  || |||  |  | |  |/---++-+-+++--+---+--+++----+⧵   | ||   || ||   |      ||| |||  |||| |   || ||  |         ||  ||  | | |
      ||   ||      |       |  || |||  |  | |  ||   || | |||  |   |  |||    ||   | || /-++-++---+------+++-+++--++++-+---++-++--+--------⧵||  ||  | | |
      ||   ⧵+------+-------/  || |||  |  | |  ||   || | |||  |  /+--+++----++---+-++-+-++-++---+------+++⧵|||  |||| |   || |⧵--+--------+++--++--/ | |
 /----++----+------+---⧵      ⧵+-+++--+--+-+--++---++-+-+++--+--++--+++----++---+-++-+-++-/|   |      |||||||  |||| |   || |   |        |||  ||    | |
 |    || /--+------+---+----⧵  | |||  |  | |/-++---++-+-+++--+--++--+++⧵   || /-+-++-+-++--+---+------+++++++--++++-+---++-+---+--------+++⧵ ||    | |
 |    || |  |  /---+---+----+--+-+++--+--+-++-++--⧵|| | |||  |  ||  ||||/--++-+-+-++-+-++--+---+------+++++++--++++-+---++-+---+--------++++-++---⧵| |
 |    || |  |  |   |   |    |  | |||  |  | |v ||  ||| | |||  |  ||  |||||  ⧵+-+-+-++-+-++--+---+------+++++++--++++-+---++-+---+--------++++-+/   || |
 |    || |  |  |   |   |    |  | |||  |  | || || /+++-+-+++--+--++--+++++---+-+-+-++-+-++--+---+------+++++++--++++-+---++-+---+---⧵    |||| |    || |
 |    || |  |  |   ⧵---+----+--+-+++--+--+-/| || |||| | |⧵+--+--++--+++++---+-+-+-++-+-++--+---+------++++/||  |||| |   || |   |   |    |||| |    || |
 |    || |  |  |/------+-⧵  |  | |||  | /+--+-++-++++-+-+-+--+--++--+++++---+-+-+-++-+-++--+---+------++++-++-⧵|||| |   || |   |   |    |||| |    || |
 | /--++-+--+--++------+⧵|  |  | |||  |/++--+-++-++++-+-+⧵|  |  ||  |||||   | | | |⧵-+-++--+---+------++++-+/ ||||| |   || |  /+---+----++++-+----++⧵|
/+-+--++-+--+⧵ ||      |||  |  ⧵-+++--++++--+-++-++++-+-+++--+--++--+++++---+-+-+-+--+-++--+---+------++++-+--+++++-+---/| |  ||   | /--++++-+--⧵ ||||
|| |  ||/+--++-++------+++--+---⧵|||  ||||  | || |||| | |||  |  ||  |||||   | | ⧵-+--+-++--+---/      |||| |  ||||| |    | |  ||   | |  |||| |  | ||||
|| |  ||||  || ||      |||  |   ||||  ||||  | || |||| ⧵-+++--+--++--+++++---+-+---+--+-++--+----------++++-/  ||||| |    | |  ||   | |  |||| |  | ||||
|| |  v|||  || ||  /---+++--+---++++--++++--+-++-++++---+++--+--++--+++++---+-+---+--+-++--+-------⧵  ||||    ||||| |    | |  ||   | |  |||| |  | ||||
|| |  ||||  || ||  |   |||  |   ||||  ||||  | || ||||   |||  |/-++--+++++---+-+---+--+-++--+⧵      |  ||||    |⧵+++-+----+-+--++---+-+--++++-/  | ||||
|| |  ||||  || ||  |   |||  |  /++++--++++--+-++-++++---+++--++-++--+++++---+-+---+--+-++--++----⧵ |  ||||    | ||| |    | |  ||   | |  ||||    | ||||
|| |  ||||  || ||  |   |||  |  ||||| /++++--+-++-++++---+++--++-++--+++++---+-+---+--+-++--++----+-+--++++----+-+++-+----+-+--++---+-+--++++----+⧵||||
|| |  ||||  || ||  |   |||  |  ||||| |||||  | || |||⧵---+++--++-++--+++++---+-+---+--+-++--++----+-+--++++----+-/|| |    | |  ||   | |  ||||    ||||||
|| |  ||||  || ||  |   |||  |  ||||| |||||  | ||/+++----+++--++-++--+++++---+-+---+--+-++--++----+-+--++++----+--++-+----+-+--++---+-+--++++⧵   ||||||
|| |  ||||  || ||  |   |||  |  ||||| |||||  | ||||||    |||  || ||  |||||   | |   |  | ||  ||    | |  ||||    |  || |    | |  ||   | |  |||||   ||||||
|| |  ||||  || ||  |   |||  |  |||||/+++++--+-++++++----+++--++-++--+++++---+-+---+--+-++--++----+-+--++++----+⧵ || |    | |  ||   | |  |||||   ||||||
|| |  |⧵++--++-++--+---+++--+--+++++++++++--+-++++++----+++--++-++--+++++---+-+---+--+-++--++----+-+--++++----++-+/ |    | |  ||   | |  |||||   ||||||
|| |  | ||  || ||  |   |||  |  |||||||||||  |/++++++----+++--++-++-⧵|||||   | |   |  | ||  ||    | |  ||||    || |  |    | |  ||   | |  |||||   ||||||
|| |  | ||  || ||  |   |||  |  ||||⧵++++++--++++++++----/||  || || ||||||   | |   |  | ||  ||    | |  ||||    || |  |    | |  ||   | |  |||||   ||||||
|| |  | ||  || ||  |   ||| /+--++++-++++++--++++++++-----++--++-++-++++++---+-+---+--+-++--++----+-+--++++----++-+--+----+-+--++---+-+⧵ |||||   ||||||
|| |  | ||  || ||  |   ||| ||  |||| ||||||  |||⧵++++-----++--++-++-++++++---/ |   |  | ||  ||    | |  ||||    || |  |    | |  ||   | || |||||   ||||||
|⧵-+--+-++--++-++--+---/|| ||  |||| ||||||  ||| ||||     ||  || || ||||||     |   |  | ||  ||    | |  ||||    || |  |    | |  ||   | || |||||   ||||||
|  |  | ||  || ||  |    || ||  |||| ||||||  ||| |^||     || /++-++-++++++-----+---+⧵ | ||  ||   /+-+--++++----++-+--+----+-+--++---+-++-+++++--⧵||||||
|  |  | ||  || ||  |    || ||  |||| ||||||  ||| ||||     || ||| || |⧵++++-----+---/| | ||  ||   || |  ||||    || |  |    | |  ||   | || |||||  |||||||
| /+--+-++--++-++--+----++-++--++++-++++++--+++-++++-----++-+++-++-+-++++⧵    |    | | ||  ||   || |  ||||  /-++-+--+⧵   ^ |  ||   | || |||||  |||||||
| ||  | ||  ||/++--+----++-++--++++-++++++--+++-++++-----++-+++-++-+-+++++----+----+-+-++--++---++-+⧵ ||||  | || |  ||   | |  ||   | || |||||  |||||||
| ||  | ||  |||||  | /--++-++--++++-++++++--+++-++++-----++-+++-++-+-+++++----+----+-+-++--++---++-++-++++--+-++-+--++---+-+--++-⧵ | || |||||  |||||||
| ||  | ||  ||||| /+-+--++-++--++++-++++++--+++-++++-----++-+++-++-+-+++++---⧵|    | | ||  ||   || ||/++++--+-++⧵|  ||   | |  || | | || |||||  |||||||
| ||  | ||  ||||| || |  || ||  |||| ||||||  ||| |||| /---++-+++-++-+-+++++---++----+-+-++--++---++-+++++++--+-++++--++---+-+-⧵|| | | || |||||  |||||||
| ||  | ||  ||||| || |  || ||  |||| ⧵+++++--+++-++++-+---++-+++-++-+-+++++---++----+-+-++--++---++-+++++++--+-+/||  ||   | | ||| | | || |||||  |||||||
| ||  | ||  |||||/++-+--++-++--++++--+++++--+++-++++-+---++-+++-++-+-+++++---++----+-+-++--++---++-+++++++--+-+-++⧵ ||   | | ||| | | || |||||  |||||||
| ||  | ||  |||||||| |  || ||  |||⧵--+++++--+++-++++-+---++-+++-++-+-+/|||   ||    | | ||/-++---++-+++++++--+-+-+++-++---+-+-+++-+⧵| || |||||  |||||||
| ||  | ||  |||||||| |  || ||  |||   |||||  ||| |||| |   || ||| || | | |||   ||    | | ||| ||   || |||||||  | | ||| ||   | | ||| ||| || |||||  |||||||
| ||  | ||/-++++++++-+--++-++--+++---+++++--+++-++++-+---++-+++-++-+-+-+++---++----+-+-+++-++-⧵ || |||||||  | | |v| ||   | | ||| ||| || |||||  |||||||
| ||  | ||| |||||||| |  || ||  |||   |||||  ||| |||| |   || ||| || | | |||   ||    | | ||| || | || |||||||  | | ||| ||   | | ||| ||| || |||||  |||||||
| ||  | ||| ||||⧵+++-+--+/ || /+++---+++++--+++-++++-+---++-+++-++-+-+-+++---++----+-+-+++-++-+-++-+++++++--+-+-+++-++⧵  | | ||| ||| || |||||  |||||||
| ||  | ||| |||| ||| |  |  || ||||   |||||  ||| |||| |   || ||| || | | |||   ||    | | ||| || | || |||||||  | | ||| |||  | | ||| ||| || |||||  |||||||
| ||  | ||| |||| ||| |  |  || ||||   |||||  ||| |||| |/--++-+++-++-+-+⧵|||   ||    | | ||| || | || |||||||  | | ||| |||  | | ||| ||| || |||||  |||||||
| ||  | ||| |||| ||| |  |  || ||||   |||||  ||| |||| ||  || ⧵++-++-+-+++++---++----/ | ||| || | || |||||||  | | ||| |||  | | ||| ||| || |||||  |||||||
| ||  |/+++-++++-+++⧵|  |  || ||||   |||||  ||| |||| ||  ||  || || | |||||   ||      | ||| || | || |||||||  | | ||| |||  | | ||| ||| || |||||  |||||||
| ||  ||||| |||⧵-+++++--+--++-++++---+++++--+++-++/| ||  ||  || || | |||||   ||      | ||| || | || |||||||  | | ||| |||  | | ||| ||| || |||||  |||||||
| ||  ||||| |||  |||||  |  || ||||   |||||  ||| || | ||  ||  || || | |||||   ||      | ||| || | || |||||||  | | ||| |||  | | ||| ||| || |||||  |||||||
| ||  ||||| |||  |||||  |  || ||||   |||||  ||| || | ||  ||  || || | |||||   ||      | ||| ⧵+-+-++-+++++++--+-+-+++-+++--+-+-+++-+++-++-+++++--++++++/
| ||  ||||| |||  |||||  |  ⧵+-++++---+++++--+++-++-+-++--++--++-++-+-+++++---++------+-+++--+-+-++-+++++++--+-+-+++-+++--+-+-+++-+++-+/ |||||  |||||| 
| ||  ||||| |||  |||||  |   | |⧵++---+++++--+++-++-+-++--++--++-++-+-+++++---++------+-+++--+-+-+/ |||||||  | | ||| |||  | | ||| ||| |  |||||  |||||| 
| ||  ||||| |||  |||||  |   | | |⧵---+++++--+++-++-+-++--++--/| || | |||||   ||      | |||  | | |  |||||||  | | ||| |||  | | ||| ||| |  |||||  |||||| 
| ||  ||||| |||  |||||  |/--+-+-+----+++++--+++-++-+-++--++⧵  | || | ⧵++++---++------+-+++--+-+-+--+++++++--+-+-+++-+++--/ | ||| ||| |  |||||  |||||| 
| ||  ||||| |||  |||||  ||  | | |    |||||  ||| || | ||  |||  | || |  ||||   ||      | |||  | | |  |||||||  | | ||| |||    | ||| ||| |  |||||  |||||| 
| ||  ||||| |||  |||||  ||  | | |    |||||  ||| || | ||  |||  | || |  ||||   ||      | |||  | | |  |||||||  ⧵-+-+++-+/|    | ||| ||| |  |||||  |||||| 
| ||  ||||| |||  |||||  ||  | | |    ||⧵++--+++-++-+-++--/||  | || |  ||||   ||      | |||  | | ⧵--+++++++----+-+++-+-+----+-+++-+++-+--+++++--/||||| 
| ||  ||||| |||  |||||  ||  | | |    || ||  ||| || | ||   ||  | || |  ||||   ||      | |||  | |    |||||||    | ||| | |    | ||| ||| |  |||||   ||||| 
| ||  ||||| |||  |||||  ||  |/+-+----++-++--+++-++-+-++---++--+-++-+--++++---++------+-+++--+-+----+++++++--⧵ | ||| | |    | ||| ||| |  |||||   ||||| 
| ||  ||||| |||  |||||  || /+++-+----++-++--+++-++-+-++---++--+-++-+--++++---++------+-+++--+-+⧵   |||||||  | | ||| | |    | ||| ||| |  |||||   ||||| 
| ||  ||||| |||  |||||  || |||| |    || ||  ||| || | ||   ||  | || |  ||||   || /----+-+++--+-++---+++++++--+-+-+++-+-+----+-+++-+++-+--+++++---+++++⧵
| ||  ||||| |||  |||||  || |||| |    || ||  ||| || | ||/--++--+-++-+--++++---++-+----+-+++--+-++---+++++++⧵ | | ||| | |    | ||| ||| |  |||||   ||||||
| ||  ||||| |||  |||||  || |||| |/---++-++--+++-++-+⧵|||  ||  | |⧵-+--++++---++-+----+-+++--+-++---+++++/|| | | ||| | |    | ||| ||| |  |||||   ||||||
| ||/-+++++-+++--+++++--++-++++-++⧵  || ||  ||| || |||||  ||  | |  |  ||||   || |    | |||  | ||   ||⧵++-++-+-+-/|| | |    | ||| ||| |  |||||   ||||||
| ||| ||||| |||  |||||  || |||| |||  || ||  ||⧵-++-+++++--++--+-+--+--++++---++-+----+-+++--+-++---++-+/ || | | /++-+-+--⧵ | ||| ||| |  |||||   ||||||
| ||| ||||| |||  |||||  || |||| |||  || ||  ||  || |||||  ||  | |  |  ||||   || |    ⧵-+++--+-++---++-+--++-+-+-+++-+-+--+-+-+++-+++-+--/||||   ||||||
| ||| ||||| |||  |||||  || |||| |||  || ||  || /++-+++++--++--+-+--+--++++---++-+------+++⧵ | ||   || |  || | | ||| | |  | | ||| ||| |   ||||   ||||||
| |⧵+-+++++-+++--+++++--/| |||| |||  || ||  || ||| |||||  ||  | |  |  ||||   || |      |||| | ||   || ⧵--++-+-+-+/| | |  | | ||| ||| ⧵---++++---/|||||
| | | ||||| |||  |||||   | |||| |||  || ||  || ||| |||||  ||  | |  |  ||||   || |      |||| | ||   ||    || | | | | | |  | | ||^ |v|     ||||    |||||
| | | ||||| |||  ||⧵++---+-++++-+++--++-++--++-+++-+++++--++--+-+--+--++++---++-+------++++-+-++---/|    || | | | | | |  | | ||| |||     ||||    |||||
| | | ||||| |||  || ||   | |||| |||  || ||  || ||| |||||  ||  | |  |  ||||   || |      |||| | ||    |    || | | | | | |  | | ||| |||     ||||    |||||
| | | ||||| |||  || ||   | |||| |||  |⧵-++--++-+++-+++++--++--+-+--+--++++---++-+------++++-+-++----+----++-+-+-+-+-+-+--+-+-+++-+++-----/|||    |||||
| | | ||||| |||  || ||   | |||| |||  |  ||  || ||| ||||⧵--++--+-+--+--++++---++-+------++++-+-++----+----+/ | | | | | |  | | ||| |||      |||    |||||
| | | ||||| |||  || ||   | |||| |||  |  ||  || ||| ||||   ⧵+--+-+--+--++++---++-+------++++-+-++----+----+--+-+-+-+-+-+--+-+-+++-+++------/||    |||||
| | | ||||| |||  || ||   | |||| |||  |  || /++-+++-++++----+--+-+⧵ |  ||||   || |      ||||/+-++----+----+--+-+-+-+-+-+--+-+-+++-+++---⧵   ||    |||||
| | | ||||| |||/-++-++---+-++++-+++--+--++-+++-+++-++++----+--+-++-+--++++---++-+⧵     |||||| ||    |    |  | | | |/+-+--+-+-+++⧵|||   |   ||    |||||
| | | ||||| |||| || ||   | |||| |||  |  || ||| ||| ⧵+++----+--+-++-+--++++---++-++-----+/|||| ||    |    |  | | | ||| |  | | |||||||   |   ||    |||||
| | | |||⧵+-++++-++-++---+-+/|| |||  |  || ||| |||  |||    |  | || |  ||||   || ||     ⧵-++++-++----+----+--+-+-+-+++-+--+-/ |||||||   |   ||    |||||
| | | ||| ⧵-++++-++-++---+-+-++-+++--+--++-+++-+++--+++----+--+-++-+--++++---++-++-------++++-/|    |    |  | | | ||| |  |   |||||||   |   ||    |||||
| | | ⧵++---++++-++-++---+-+-++-+++--+--+/ ||| |||  |||    |  | || |  ||||   ||/++-------++++--+----+----+--+-+-+-+++-+--+---+++++++-⧵ |   ||    |||||
| | |  ||   |||| || ||   | | || |||  |  ⧵--+++-+++--+++----+--+-++-+--++++---+++++-------++++--+----+----+--+-/ | ||| |  |   ||||||| | |   ||    |||||
| | |  ||   |||| || ||   | | || |||  ⧵-----+++-+++--+++----+--+-++-+--++++---+++++-------++++--+----+----+--+---+-+++-+--+---+++++++-+-+---++----/||||
| | |  ||   ^||| || ||   | | || |||        ||| |||  |||    |  | || |  ||||   |||||       ||||  |    |    |  |   | ||| |  |   ||||||| | |   ||     ||||
| | |  ||   ⧵+++-++-++---+-+-++-+++--------+++-+++--+++----+--+-++-+--++++---+++++-------++++--+----+----+--+---+-++/ |  |   ||||||| | |   ||     ||||
| | |  ||    ||| || ||   | | || |||      /-+++-+++--+++----+--+-++-+--++++---+++++-------++++--+----+----+--+---+⧵||  |  |   ||⧵++++-+-+---++-----+/||
| | |  ||    ||| || ||   | | || |||/-----+-+++-+++⧵ |||  /-+--+-++-+--++++---+++++-------++++--+----+----+--+---++++-⧵|  |   || |||| | |   ||     | ||
| | |  ⧵+----+++-++-/|   | | || ||||     | ||⧵-++++-+++--+-+--+-++-/  ||||   |||||       ||||  |    |    |  |   ||||/++--+---++⧵|||| | |   ||     | ||
| | |   |    ||| ||  ⧵---+-+-++-++++-----+-++--++++-+++--+-+--+-++----++++---+++++-------++++--+----+----+--+---+++++++--+---++++/|| | |   ||     | ||
| | |   |    ||| ||      | | || ||||     | ||  |||| |||  | |  |/++----++++⧵  |||||       ||||  |    |    |  |   |||||||  |   |||| || | |   ||     | ||
| | |   |    ||| ||      | | || ||||     | ||  |||| |||  | |  |||| /--+++++--+++++-------++++--+----+----+--+<--+++++++--+---++++-++-+-+---++--⧵  | ||
| | |   |    ||| ||      | | || ||||     | ||  ⧵+++-+++--+-+--++++-+--+++++--+++++-------+/||  |    |    |  |   |||⧵+++--+---+++/ || | |   ||  |  | ||
| | |   ⧵----+++-++->----+-+-++-/⧵++-----+-++---+++-/||  | |  |||| |  |||||  |||||       | ||  |    |    |  |   ||| |||  |   |||  || | |   ||  |  | ||
| | |        ||| ||      | | ||   ||     | ||   |||  ⧵+--+-+--++++-+--+++++--+++++-->----+-++--+----+----+--+---+++-+++--+---/||  || | |   ||  |  | ||
| | |        ||| ||      | | ⧵+---++-----+-++---+++---+--+-+--++++-+--+++++--+++++-------+-++--+----+----+--/   ||| |||  |    ||  || | |   ||  |  | ||
| | |        ||| ||      | |  |   |⧵-----+-++---++//--+--+-+-⧵|||| |  |||||  |||||       ⧵-++--+----+----+------+++-+++--+----++--/| | |   ||  |  | ||
| | |        ||| ||      | |  |   |      | ||   || |  |  | | ||||| |  |||||  |||||         ||  |    |    |      ||| |||  |    ||/--+-+-+---++-⧵|  | ||
⧵-+-+--------/|| ||      | |  |   |      | ||   || |  |  | | ||||| |  |||||  ||⧵++---------++--+----+----+------+++<+++--+----+++--+-/ |   || ||  | ||
  | |         || |⧵------+-+--+---+------+-++---++-+--+--+-+-+++++-+--+++++--/| ||         ⧵+--+----+----+------+++-+++--+----+++--+---/   || ||  | ||
  | |         || | /-----+-+--+---+------+-++⧵  || |  |  | | |||⧵+-+--+++++---+-++----------+--+----+----/      ||| |||  |    |||  |       || ||  | ||
  | |         || | |     | |  |   |      | |||  || |  |  | | ||| | |  |||||   | ⧵+----------+--+----+-----------+++-+++--+----+++--+-------++-++--+-+/
  | |         || | |     | |  |   |      | |||  || |  ⧵--+-+-+++-+-+--/|⧵++---+--+----------+--+----+------>----+++-+++--+----+++--+-------++-++--/ | 
  | ⧵---------++-+-+-----+-+--+---/      | |||  || |     | | |⧵+-+-+---+-++---+--+----------/  |    |           ||| |||  |    |||  |       || ||    | 
  |           || | |     | ⧵--+----------+-+++--++-+-----+-+-+-+-+-+---+-++---+--+-------------/    |           ⧵++-+++--/    |||  |       || ||    | 
  ⧵-----------++-+-+-----+----+----------+-+++--++-+-----+-+-+-+-+-+---+-/|   |  |                  |            || |||       |||  |       || ||    | 
              || | |     |    |          | ⧵++--++-+-----+-+-+-+-/ ⧵---+--+---+--+------------------+------------++-+++-------+++--+-------++-+/    | 
              || | |     |    |          ⧵--++--++-+-----+-+-+-+-------+--+---+--+------------------+------------/| |||       |||  |       || |     | 
              || | |     |    |             ⧵+--++-+-----+-+-+-+-------/  |   |  |                  |             | |||       |||  |       || |     | 
              || | |     |    |              |  || ⧵-----+-+-/ |          |   ⧵--+------------------+-------------+-+++-------+++--+-------/| |     | 
              || | ⧵-----+----+--------------/  |⧵-------+-+---+----------+------+------------------+-------------+-+++-------+++--/        | |     | 
              || |       ⧵----+-----------------+--------+-/   |          |      |                  |             | |||       |||           | |     | 
              || |            |                 |        |     |          |      |                  |             | |||       |||           | |     | 
              || |            |                 |        |     |          |      |                  |             | |||       |||           | |     | 
              || ⧵------------+-----------------+--------+-----+----------+------+------------------+-------------/ |||       |||           | |     | 
              ||              |                 |        ⧵-----+----------+------+------------------+---------------+/|       ⧵++-----------+-+-----/ 
              ||              |                 |              |          |      |                  |               | |        ||           | |       
              ||              |                 ⧵--------------+----------+------+------------------+---------------+-+--------++-----------/ |       
              |⧵---<----------+--------------------------------+----------+------/                  |               | |        ||             |       
              |               |                                ⧵----------/                         |               ⧵-+--------/⧵-------------/       
              |               ⧵---------------------------------------------------------------------+-----------------/                               
              ⧵-------------------------------------------------------------------------------------/                                                 """
