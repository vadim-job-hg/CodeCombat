#todo:
# http://codecombat.com/play/level/match-cord

'''
#Cheat Way

resultColumn = 1
mineDistance = 5
firstXPos = 15
firstYPos = 40
# Find which starting mine connects to the ogre Chieftain.
# resultColumn = 1 # fast way to win!!!!!!:-D
self.say("I think it's column number: " + resultColumn)
self.moveXY(resultColumn * mineDistance + firstXPos, firstYPos)



# or
'''

fieldMap = hero.findFriends()[0].getMap()
map=[],i=0,j=0
for(i=0;i<fieldMap.length;i++)
    map.push([]);
for(i=0;i<fieldMap.length;i++)
    for(j=0;j<fieldMap[0].length;j++){
        if(fieldMap[i][j]==="x")
            map[i].push("x");
        else
            map[i].push(".");
    }
hero.say(map[0].length+" nn "+map.length);
function find(arr,i,j){
    var array=[];
    array.push([i,j]);
    while(array.length>0){
        var temp=[];
        for(var x=0;x<array.length;x++){
            var m=array[x][0];
            var n=array[x][1];
            arr[m][n]=".";
            if(n+1<27&&arr[m][n+1]==="x"){
                temp.push([m,n+1]);
                if(m===15&&n+1===13)
                    hero.moveXY(j*5+15,40);
            }
            if(m+1<16&&arr[m+1][n]==="x"){
                temp.push([m+1,n]);
                if(m+1===15&&n===13)
                    hero.moveXY(j*5+15,40);
            }
            if(n-1>=0&&arr[m][n-1]==="x"){
                temp.push([m,n-1]);
                if(m===15&&n-1===13)
                    hero.moveXY(j*5+15,40);
            }
            if(m-1>=0&&arr[m-1][n]==="x"){
                temp.push([m-1,n]);
                if(m-1===15&&n===13)
                    hero.moveXY(j*5+15,40);
            }
        }
        array=[];
        array=temp;
    }
}
for(j=0;j<map[0].length;j++){
    if(map[0][j]==="x"){
        find(map,0,j);
    }
}
