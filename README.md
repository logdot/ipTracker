# ipTracker
ipTracker is a crude and basic python program to track the ammount of ip in a 4chan thread over time. It also includes some basic graphing.
It uses the [4Chan API](https://github.com/4chan/4chan-API) to get it's information while a thread is active, then stores it in a sqlite database.
By default it tracks the /wah/ thread on /vt/ but support for tracking via arguments is planned.

## Graphs
The graphs are made using matplotlib
![Graph over time](https://i.imgur.com/ZvxKvf3.png)
![Graph over week](https://i.imgur.com/UF8Oc17.png)
