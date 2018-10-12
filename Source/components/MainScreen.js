import React from 'react';
import {View,Text,StatusBar,Keyboard,Animated,KeyboardAvoidingView,TextInput,Image,FlatList,StyleSheet} from 'react-native';
class Connection{
    getMessage(){
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

                xhttp.open("GET","http://192.168.43.211/getMessage",true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send();
        });
    }
    isTyping(){
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

                xhttp.open("GET","http://192.168.43.211/isTyping",true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send();
        });
    }

    push(text){
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

                xhttp.open("GET","http://192.168.43.211/addMessage",true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send("msg="+text);
        });
    }
}


const con=new Connection();
export default class MainScreen extends React.Component{
    static navigationOptions = {header: null };
    constructor(props){
        super(props)
        this.state={
            messages:[],
            typing:0,
            text:"",
            animMTop:new Animated.Value(-3),
            animMarginTopForSendStatus:new Animated.Value(-60),
            statusVisible:false,
            statusBarColor:"#191919",
        }
    }
    componentDidMount(){
        this.keyboardDidShowListener = Keyboard.addListener('keyboardDidShow', this.keyboardDidShow);
        this.keyboardDidHideListener = Keyboard.addListener('keyboardDidHide', this.keyboardDidHide);
        
        const app=this;
        var messages;
        setInterval(function(){
            con.getMessage()
            .then(data=>{
                messages=app.state.messages;
                if(messages[messages.length-1]!==data){
                    messages.push(data);
                    //alert(messages)
                    app.setState({messages:messages})
                }
            })
            .catch({})
        },2000);

        setInterval(function(){
            con.isTyping()
            .then(data=>{
                app.setState({typing:1})
            })
            .catch(error=>{app.setState({typing:0})})
        },500);
    }

    keyboardDidShow=()=>{
        const app=this;
        Animated.timing(
            app.state.animMTop,{
                toValue:-24,
                duration:220,
            }
        ).start()
      }
    
    keyboardDidHide () {
        /*
        const app=this;
        Animated.timing(
            app.state.animMTop,{
                toValue:-3,
                duration:220,
            }
        ).start()
        */
    }

    showStatus=()=>{
        this.msgToSend.clear();
        const app=this;
        if(this.state.statusVisible===false){
            Animated.timing(
                app.state.animMarginTopForSendStatus,{
                    toValue:0,
                    duration:220,
                }
            ).start()
            this.setState({statusVisible:true})
            this.setState({statusBarColor:"#00897B"})
            setTimeout(function(){
                app.showStatus();
            },3000)
        }
        else{
            Animated.timing(
                app.state.animMarginTopForSendStatus,{
                    toValue:-60,
                    duration:220,
                }
            ).start()
            this.setState({statusVisible:false})
            this.setState({statusBarColor:"#191919"})
        }
    }

    push=()=>{
        const app=this;
        if(this.state.text===""){
            return false;
        }
        con.push(this.state.text)
            .then(data=>{
                app.showStatus();
            })
            .catch({})
    }
    render(){
        return(
            <KeyboardAvoidingView style={{flex:1,backgroundColor:"#191919"}} enabled>
                <StatusBar backgroundColor={this.state.statusBarColor} barStyle="light-content"/>
                <Animated.View style={{marginTop:this.state.animMarginTopForSendStatus,height:60,position:"absolute",top:0,left:0,right:0,backgroundColor:"#00897B",zIndex:100,padding:20,fontFamily:"nr",elevation:10,borderBottomLeftRadius:10,borderBottomRightRadius:10,}}>
                    <Text style={{textAlign:"center",color:"#fff"}}>Message Sent</Text>
                </Animated.View>
                <View style={{flex:56,padding:20,}}>
                    <Image 
                        source={require('./person.png')}
                        style={{width:34,borderRadius:34,height:34}}
                    />
                    {this.state.messages.length===0?<Text style={{color:"#fff",paddingTop:20,}}>No Messages</Text>:
                    <FlatList
                        style={{marginTop:20}}
                        data={this.state.messages}
                        ref={listView => { this.listView = listView; }}
                        onContentSizeChange={()=>{
                            this.listView.scrollToEnd()
                        }}
                        renderItem={
                            ({item}) =>
                                    <Text style={[styles.text]}>
                                        {item}
                                    </Text>
                        }
                    />
                    }
                </View>
                {this.state.typing===1?
                <View style={{flex:6,marginBottom:20,}}>
                    <Image source={require("./loading.gif")} style={{height:50,width:100,}}/>
                </View>:
                <View style={{flex:6,marginBottom:20,opacity:0}}>
                    <Image source={require("./loading.gif")} style={{height:50,width:100,}}/>
                </View>}
                <View style={{alignItems:"flex-end",flex:4,}}>
                        <Animated.View style={{width:50,height:50,backgroundColor:'#00695C',alignItems:"center",justifyContent:"center",marginTop:this.state.animMTop,borderRadius:50,elevation:15,marginRight:25}}>
                            <Text onPress={()=>{this.push()}}><Image source={require("./send.png")} style={{height:85,width:85,}}/></Text>
                        </Animated.View>
                </View>
                <View style={{flex:34,backgroundColor:"#202020",borderTopLeftRadius:10,borderTopRightRadius:10,elevation:7}}>
                     <TextInput
                        underlineColorAndroid="transparent"
                        multiline
                        placeholder="Enter something to send..."
                        style={{flex:1,textAlignVertical:'top',color:"#eee",padding:20,fontSize:20,fontFamily:"nr"}}
                        placeholderTextColor="#ccc"
                        ref={(input)=>{this.msgToSend=input}}
                        onChangeText={(text)=>{this.setState({text:text})}}
                        returnKeyType={"submit"}
                        blurOnSubmit={false}
                        />
                </View>
            </KeyboardAvoidingView>
        )
    }
}
const styles=StyleSheet.create({
    text:{fontSize:25,color:"#fff",fontFamily:"nb",marginBottom:10,}
})