package com.example.android.breathesense;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.example.android.breathesense.MqttHelper;
import com.example.android.breathesense.MqttHelper2;
import com.example.android.breathesense.R;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class Main2Activity extends AppCompatActivity {
    MqttHelper2 mqttHelper2;

    TextView word;

    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        word = (TextView) findViewById(R.id.word);

        startMqtt();
    }

    public void Developer(View View)
    {
            Intent Developer = new Intent(this,MainActivity.class);
            startActivity(Developer);
    }

        private void startMqtt() {
        mqttHelper2 = new MqttHelper2(getApplicationContext());
        mqttHelper2.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean b, String s) {

            }

            @Override
            public void connectionLost(Throwable throwable) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage mqttMessage) throws Exception {
                Log.w("Debug", mqttMessage.toString());
                word.setText(mqttMessage.toString());
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken iMqttDeliveryToken) {

            }
        });
    }
}