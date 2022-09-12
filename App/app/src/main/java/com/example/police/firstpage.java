package com.example.police;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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

public class firstpage extends AppCompatActivity {
    EditText ip_email,ip_password;
    Button bt_forgot_password;
    Button bt_login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_firstpage);
        ip_email = findViewById(R.id.input_email);
        ip_password = findViewById(R.id.input_password);
        bt_login = findViewById(R.id.btn_login);
        findViewById(R.id.btn_forgot_password).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(firstpage.this,forgot_passwordpage.class);
                startActivity(i);
            }
        });

        bt_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(ip_email.getText().toString().matches("") || ip_password.getText().toString().matches("")){
                    ip_password.setError("Check Email");
                    ip_email.setError("Incorrect Password");
                    Toast.makeText(firstpage.this,"Insufficient data",Toast.LENGTH_SHORT).show();
                    return;
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
                RequestQueue requestQueue = Volley.newRequestQueue(firstpage.this);
                JsonObjectRequest jsonAbjectRequest = new JsonObjectRequest(Request.Method.POST,
                        "http://192.168.0.134:3456/api/police-login/", postData, new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {

                        try {

                            SharedPreferences sharedPreferences = getSharedPreferences("AuthToken",MODE_PRIVATE);
                            SharedPreferences.Editor editor = sharedPreferences.edit();
                            editor.putString("token",response.getString("token"));
                            editor.apply();

                            Toast.makeText(firstpage.this,response.getString("message"),Toast.LENGTH_SHORT).show();
                            if(response.getString("message").matches("Login successfull")){
                                Intent intent = new Intent(firstpage.this, dashboard.class);
                                startActivity(intent);
                            }

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
                            }
                        }else if(error.networkResponse.statusCode == 406){
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("message");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                                ip_password.setError("Incorrect Password");
                            } catch (JSONException | UnsupportedEncodingException e) {
                            }
                        }else{
                            try {
                                String responseBody = new String(error.networkResponse.data, "utf-8");
                                JSONObject data = new JSONObject(responseBody);
                                String message = data.getString("message");
                                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
                                ip_password.setError("Incorrect Password");
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
//private void postDataUsingVolley() {
//        // url to post our data
//        String url = "https://127.0.0.1:8000/api/police-login/";
//
//        // creating a new variable for our request queue
//        RequestQueue queue = Volley.newRequestQueue(firstpage.this);
//
//        // on below line we are calling a string
//        // request method to post the data to our API
//        // in this we are calling a post method.
//        StringRequest request = new StringRequest(Request.Method.POST, url, new com.android.volley.Response.Listener<String>() {
//            @Override
//            public void onResponse(String response) {
//                // inside on response method we are
//                // hiding our progress bar
//                // and setting data to edit text as empty
//                ip_email.setText("");
//                ip_password.setText("");
//
//                // on below line we are displaying a success toast message.
//                Toast.makeText(firstpage.this, "Data added to API", Toast.LENGTH_SHORT).show();
//                try {
//                    // on below line we are parsing the response
//                    // to json object to extract data from it.
//                    JSONObject respObj = new JSONObject(response);
//
//                    // below are the strings which we
//                    SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(firstpage.this);
//                    SharedPreferences.Editor editor = preferences.edit();
//                    // extract from our json object.
////                    SharedPreferences sharedPreferences = getPreferences(MODE_PRIVATE);
////                    SharedPreferences.Editor editor = sharedPreferences.edit();
//                    String resp = respObj.getString("message");
//                    String token = respObj.getString("job");
//                    editor.putString("token",token);
//                    editor.apply();
////                    editor.putString("token", token);
////                    editor.commit();
//                    String name = preferences.getString("token", "");
//                    Toast.makeText(firstpage.this,resp+" - "+name,Toast.LENGTH_LONG).show();
//
//                    // on below line we are setting this string s to our text view.
//                } catch (JSONException e) {
//                    e.printStackTrace();
//                }
//            }
//        }, new com.android.volley.Response.ErrorListener() {
//            @Override
//            public void onErrorResponse(VolleyError error) {
//                // method to handle errors.
//                Toast.makeText(firstpage.this,  "" + error, Toast.LENGTH_SHORT).show();
//                System.out.println(error);
//            }
//        }) {
//            @Override
//            protected Map<String, String> getParams() {
//                // below line we are creating a map for
//                // storing our values in key and value pair.
//                Map<String, String> params = new HashMap<String, String>();
//
//                // on below line we are passing our key
//                // and value pair to our parameters.
//                params.put("email", String.valueOf(ip_email.getText()));
//                params.put("password", String.valueOf(ip_password.getText()));
//
//                // at last we are
//                // returning our params.
//                return params;
//            }
//        };
//        // below line is to make
//        // a json object request.
//        queue.add(request);
//
//    }
//
