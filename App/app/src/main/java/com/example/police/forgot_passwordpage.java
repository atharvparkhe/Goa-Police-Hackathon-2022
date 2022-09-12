package com.example.police;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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

public class forgot_passwordpage extends AppCompatActivity {

    EditText ip_otp_email,ip_otp,ip_new_password,ip_verify_password;
    Button btn_sendOtp,btn_verify;
    Boolean otp_Sent = false;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_forgot_passwordpage);
        ip_otp_email = findViewById(R.id.input_opt_email);
        btn_sendOtp = findViewById(R.id.btn_otp);
        btn_verify = findViewById(R.id.btn_verify);
        ip_otp = findViewById(R.id.input_otp);
        ip_new_password = findViewById(R.id.input_new_password);
        ip_verify_password = findViewById(R.id.input_re_password);
        btn_sendOtp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(ip_otp_email.getText().toString().matches("")){
                    Toast.makeText(forgot_passwordpage.this,"Insufficient data",Toast.LENGTH_SHORT).show();
                }
////                else{
////                    postDataUsingVolley();
////                }
                JSONObject postData = new JSONObject();

                try {

                    postData.put("email", ip_otp_email.getText().toString());
//                    postData.put("email", "aniket@gmail.com");
//                    postData.put("password", "qbwknnhi");
                } catch (JSONException e) {
                    e.printStackTrace();
                }


                Log.d("POST",postData.toString());
                RequestQueue requestQueue = Volley.newRequestQueue(forgot_passwordpage.this);
                JsonObjectRequest jsonAbjectRequest = new JsonObjectRequest(Request.Method.POST,
                        "http://192.168.0.134:3456/api/police-forgot/", postData, new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {

                        try {
                            Toast.makeText(forgot_passwordpage.this,response.getString("message"),Toast.LENGTH_SHORT).show();
                            otp_Sent = true;
//                            if(response.)

//                            SharedPreferences sharedPreferences = getSharedPreferences("AuthToken",MODE_PRIVATE);
//                            SharedPreferences.Editor editor = sharedPreferences.edit();
//                            editor.putString("token",response.getString("token"));
//                            editor.apply();


//                            Intent intent = new Intent(firstpage.this, MainActivity.class);
//                            startActivity(intent);
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
                        Toast.makeText(forgot_passwordpage.this,error.getMessage().toString(),Toast.LENGTH_LONG).show();
                        if(error.networkResponse.statusCode == 400){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                JSONObject errors = data.getJSONObject("error");
                                JSONArray jsonMessage = errors.getJSONArray("email");
                                String message = jsonMessage.getString(0);
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();

                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }else if(error.networkResponse.statusCode == 406){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }else{
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }
                    }
                });

                requestQueue.add(jsonAbjectRequest);
            }

        });

        btn_verify.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               if(ip_otp.getText().toString().matches("")){
                   Toast.makeText(forgot_passwordpage.this,"Enter the otp",Toast.LENGTH_SHORT).show();
                   return;
               }
               if(!ip_new_password.getText().toString().matches(ip_verify_password.getText().toString())){
                   Toast.makeText(forgot_passwordpage.this,"Password not same",Toast.LENGTH_SHORT).show();
                    return;
               }
////                else{
////                    postDataUsingVolley();
////                }
                JSONObject postData = new JSONObject();

                try {

                    postData.put("otp", ip_otp.getText().toString());
                    postData.put("pw", ip_new_password.getText().toString());
                    postData.put("cpw", ip_verify_password.getText().toString());
//                    postData.put("password", ip_password.getText().toString());
//                    postData.put("email", "aniket@gmail.com");
//                    postData.put("password", "qbwknnhi");
                } catch (JSONException e) {
                    e.printStackTrace();
                }


                Log.d("POST",postData.toString());
                RequestQueue requestQueue = Volley.newRequestQueue(forgot_passwordpage.this);
                JsonObjectRequest jsonAbjectRequest = new JsonObjectRequest(Request.Method.POST,
                        "http://192.168.0.134:3456/api/police-reset/", postData, new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {

                        try {
                            Toast.makeText(forgot_passwordpage.this,response.getString("message"),Toast.LENGTH_SHORT).show();

                            SharedPreferences sharedPreferences = getSharedPreferences("AuthToken",MODE_PRIVATE);
//                            SharedPreferences.Editor editor = sharedPreferences.edit();
//                            editor.putString("token",response.getString("token"));
//                            editor.apply();


                            Intent intent = new Intent(forgot_passwordpage.this, firstpage.class);
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
                        Toast.makeText(forgot_passwordpage.this,error.getMessage(),Toast.LENGTH_LONG).show();
                        if(error.networkResponse.statusCode == 400){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                JSONObject errors = data.getJSONObject("error");
                                JSONArray jsonMessage = errors.getJSONArray("email");
                                String message = jsonMessage.getString(0);
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();

                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }else if(error.networkResponse.statusCode == 406){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }else{
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("result");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }
                    }
                });

                requestQueue.add(jsonAbjectRequest);

            }
        });

    }
}