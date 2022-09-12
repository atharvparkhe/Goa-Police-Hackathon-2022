package com.example.police;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class AddCrime2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_crime2);
        findViewById(R.id.request_submit).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(AddCrime2.this,"Added",Toast.LENGTH_SHORT).show();
                Intent i = new Intent(AddCrime2.this,dashboard.class);
                startActivity(i);
            }
        });
    }
}