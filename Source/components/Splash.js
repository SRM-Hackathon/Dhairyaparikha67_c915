import React from 'react';
import {View,StatusBar,Image,Text} from 'react-native';
import { StackActions, NavigationActions } from 'react-navigation'

class Connection{
    checkIfServerLives(){
        var xhttp=new XMLHttpRequest();
            return new Promise((resolve,reject)=>{
                var data;
                xhttp.onreadystatechange=function(){
                    if(this.readyState===4 && this.status===200){
                        data=this.responseText;
                        if(data=="0")
                            reject(data);
                        else resolve(data);
                    }
                };

                xhttp.open("GET","http://192.168.43.211/isLive",true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send();
        });
    }
}

const con=new Connection();

export default class Splash extends React.Component{
    static navigationOptions = {header: null };
    doNav=()=>{
        const navigationAction=StackActions.reset({
            index: 0,
            key:null,
            actions: [NavigationActions.navigate({ routeName:"MainScreen"})],
        });
        this.props.navigation.dispatch(navigationAction);
    }
    componentDidMount(){
        const app=this;
        const repeat=setInterval(function(){
            con.checkIfServerLives()
            .then(data=>{
                app.doNav();
                clearInterval(repeat);
            })
            .catch(err=>{})
        },1000);
    }

    render(){
        return(
            <View style={{flex:1,backgroundColor:"#fff",alignItems:"center",justifyContent:"center"}}>
                <StatusBar backgroundColor="#fff" barStyle="dark-content"/>
                <View style={{}}>
                <Image source={require('./waiting.gif')} style={{width:100,height:100,}}/>
                <Text>Searching for Device</Text>
                </View>
            </View>
        )
    }
}