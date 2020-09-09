#include <Date.au3>
#first open new Edge instance tap to https://www.bing.com/news
WinActivate("Bing News","Microsoft Edge")
MouseClick("left",381,145,1)
send("incongruent trend following united states stock market volatility compared barrack 2098390406 4089431433" & _NowDate())
MouseClick("left",725,145,1)
sleep(2000)
for $i = 1 to 47 Step +1
   WinActivate("Bing News","Microsoft Edge")
   MouseClick("left",381,145,1)
   Send("{BS}")
   sleep(2000)
   Send("{ENTER}")
Next
