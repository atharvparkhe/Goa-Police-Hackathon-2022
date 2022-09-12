package com.example.police;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.Toast;

public class dashboard extends AppCompatActivity {

//    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        CardView btn_search = findViewById(R.id.btn_search);
        btn_search.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(dashboard.this,"clicked",Toast.LENGTH_SHORT).show();
                Intent i = new Intent(dashboard.this,Search.class);
                startActivity(i);
            }
        });
        findViewById(R.id.btn_hotspot).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(dashboard.this,"clicked",Toast.LENGTH_SHORT).show();
                Intent i = new Intent(dashboard.this,Hotspot.class);
                startActivity(i);
            }
        });
        findViewById(R.id.btn_addCrime).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(dashboard.this,"clicked",Toast.LENGTH_SHORT).show();
                Intent i = new Intent(dashboard.this,AddCrime.class);
                startActivity(i);
            }
        });
    }
}