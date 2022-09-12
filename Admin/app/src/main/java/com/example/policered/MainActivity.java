package com.example.policered;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.media.effect.Effect;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ExpandableListAdapter;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.UnsupportedEncodingException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EditText ip_email = findViewById(R.id.input_email);
        EditText ip_password = findViewById(R.id.input_password);

        Button btn_login = findViewById(R.id.btn_login);

        findViewById(R.id.btn_fp).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this,forgot_resetPassword.class);
                startActivity(i);
            }
        });

        btn_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(ip_email.getText().toString().matches("") || ip_password.getText().toString().matches("")){
                    Toast.makeText(MainActivity.this,"Insufficient data",Toast.LENGTH_SHORT).show();
                }
////                else{
////                    postDataUsingVolley();
////                }
                JSONObject postData = new JSONObject();

                try {

                    postData.put("email", ip_email.getText().toString());
                    postData.put("password", ip_password.getText().toString());
//                    postData.put("email", "aniket@gmail.com");
//                    postData.put("password", "qbwknnhi");
                } catch (JSONException e) {
                    e.printStackTrace();
                }


                Log.d("POST",postData.toString());
                RequestQueue requestQueue = Volley.newRequestQueue(MainActivity.this);
                JsonObjectRequest jsonAbjectRequest = new JsonObjectRequest(Request.Method.POST,
                        "http://192.168.0.134:3456/api/police-head-login/", postData, new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {

                        try {
                            Toast.makeText(MainActivity.this,response.getString("message"),Toast.LENGTH_SHORT).show();

                            SharedPreferences sharedPreferences = getSharedPreferences("AuthToken",MODE_PRIVATE);
                            SharedPreferences.Editor editor = sharedPreferences.edit();
                            editor.putString("token",response.getString("token"));
                            editor.apply();


                            Intent intent = new Intent(MainActivity.this, dashboard.class);
                            startActivity(intent);
//                            progressDialog.dismiss();
//                            finish();

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }





                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.d("VolleyDebug","Error retrieving data");
                        if(ip_password.getText().toString().matches("")) {
                            ip_password.setError("Enter Password");
                        }
//                        Toast.makeText(MainActivity.this,error.getMessage(),Toast.LENGTH_LONG).show();
                        if(error.networkResponse.statusCode == 400){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                JSONObject errors = data.getJSONObject("error");
                                JSONArray jsonMessage = errors.getJSONArray("email");
                                String message = jsonMessage.getString(0);
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                                ip_email.setError("Check Email");

                            } catch (JSONException | UnsupportedEncodingException e) {
                                Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_SHORT).show();
                            }
                        }else if(error.networkResponse.statusCode == 406){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                                ip_password.setError("Incorrect Password");
                            } catch (Exception e) {
                                Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_SHORT).show();
                            }
                        }
                        else if(error.networkResponse.statusCode == 404){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                                ip_password.setError("Incorrect Password");
                            } catch (Exception  e) {
                                Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_SHORT).show();
                            }
                        }else{
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                                ip_password.setError("Incorrect Password");
                            } catch (Exception  e) {
                                Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_SHORT).show();
                            }
                        }
                    }
                });

                requestQueue.add(jsonAbjectRequest);
            }
        });



    }
}