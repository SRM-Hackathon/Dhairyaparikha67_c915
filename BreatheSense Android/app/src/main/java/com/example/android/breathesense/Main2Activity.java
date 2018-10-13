package com.example.android.breathesense;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.android.breathesense.MqttHelper;
import com.example.android.breathesense.MqttHelper2;
import com.example.android.breathesense.R;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.util.Locale;

public class Main2Activity extends AppCompatActivity {
    MqttHelper2 mqttHelper2;

    Button button_speak;
    TextView word;
    TextToSpeech textToSpeech;

    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        button_speak = (Button)findViewById(R.id.button_speak);
        word = (TextView) findViewById(R.id.word);

        textToSpeech = new TextToSpeech(this, new TextToSpeech.OnInitListener() {
            public void onInit(int status)
            {
                if(status == TextToSpeech.SUCCESS)
                {
                    int result = textToSpeech.setLanguage(Locale.ENGLISH);
                    if(result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED)
                    {
                        Toast.makeText(Main2Activity.this, "this Language is not supported",Toast.LENGTH_SHORT).show();
                    }
                    else
                    {
                        button_speak.setEnabled(true);
                        textToSpeech.setPitch(0.6f);
                        textToSpeech.setSpeechRate(1.0f);
                        speak();
                    }
                }
            }
        });
        startMqtt();
        button_speak.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v)
            {
                speak();
            }
        });
    }

    private void speak()
    {
        String text = word.getText().toString();
        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP)
            textToSpeech.speak(text,TextToSpeech.QUEUE_FLUSH,null,null);
        else
            textToSpeech.speak(text,TextToSpeech.QUEUE_FLUSH,null);

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