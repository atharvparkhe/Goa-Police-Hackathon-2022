package com.example.police;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private GpsTracker gpsTracker;
    private TextView tvLatitude,tvLongitude;
    protected LocationManager mLocationManager;
    protected LocationListener locationListener;
    protected Context context;
    String lat;
    String provider;
    protected String latitude, longitude;
    protected boolean gps_enabled, network_enabled;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvLatitude = findViewById(R.id.textView2);
        tvLongitude = findViewById(R.id.textView3);

//

        SharedPreferences sharedPreferences = getSharedPreferences("AuthToken",MODE_PRIVATE);
//        Toast.makeText(this,sharedPreferences.getString("token",""),Toast.LENGTH_SHORT).show();
        if(sharedPreferences.getString("token","").matches("")){
            Intent i=new Intent(this,firstpage.class);
            startActivity(i);
        }
        else{
            Intent i=new Intent(this,dashboard.class);
            startActivity(i);
        }
//
        Button logout = findViewById(R.id.btn_logout);
        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences.Editor editor = sharedPreferences.edit();
                editor.putString("token","");
                editor.apply();
                Intent i=new Intent(MainActivity.this,firstpage.class);
                startActivity(i);
                Toast.makeText(MainActivity.this,"logged out",Toast.LENGTH_SHORT).show();

            }
        });


//        try {
//            if (ContextCompat.checkSelfPermission(getApplicationContext(), android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED ) {
//                ActivityCompat.requestPermissions(this, new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION}, 101);
//            }
//        } catch (Exception e){
//            e.printStackTrace();
//        }

//        getLocation(null);


    }
    // location
//    public void getLocation(View view){
//        gpsTracker = new GpsTracker(MainActivity.this);
//        if(gpsTracker.canGetLocation()){
//            double latitude = gpsTracker.getLatitude();
//            double longitude = gpsTracker.getLongitude();
//            tvLatitude.setText(String.valueOf(latitude));
//            tvLongitude.setText(String.valueOf(longitude));
//        }else{
//            gpsTracker.showSettingsAlert();
//        }
//    }
}