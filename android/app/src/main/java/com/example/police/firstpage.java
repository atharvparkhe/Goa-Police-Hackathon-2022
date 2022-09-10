package com.example.police;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class firstpage extends AppCompatActivity {

    EditText ip_email,ip_password;
    TextView bt_forgot_password;
    Button bt_login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_firstpage);
        ip_email = findViewById(R.id.input_email);
        ip_password = findViewById(R.id.input_password);
        bt_login = findViewById(R.id.btn_login);


        bt_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                if(ip_email.getText().equals("") || ip_password.getText().equals("")){
//                    Toast.makeText(firstpage.this,"Insufficient data",Toast.LENGTH_SHORT).show();
//                }
//                else{
                    postDataUsingVolley();
//                }
            }
        });

    }
    private void postDataUsingVolley() {
        // url to post our data
        String url = "https://127.0.0.1:8000/api/police-login/";

        // creating a new variable for our request queue
        RequestQueue queue = Volley.newRequestQueue(firstpage.this);

        // on below line we are calling a string
        // request method to post the data to our API
        // in this we are calling a post method.
        StringRequest request = new StringRequest(Request.Method.POST, url, new com.android.volley.Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // inside on response method we are
                // hiding our progress bar
                // and setting data to edit text as empty
                ip_email.setText("");
                ip_password.setText("");

                // on below line we are displaying a success toast message.
                Toast.makeText(firstpage.this, "Data added to API", Toast.LENGTH_SHORT).show();
                try {
                    // on below line we are parsing the response
                    // to json object to extract data from it.
                    JSONObject respObj = new JSONObject(response);

                    // below are the strings which we
                    SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(firstpage.this);
                    SharedPreferences.Editor editor = preferences.edit();
                    // extract from our json object.
//                    SharedPreferences sharedPreferences = getPreferences(MODE_PRIVATE);
//                    SharedPreferences.Editor editor = sharedPreferences.edit();
                    String resp = respObj.getString("message");
                    String token = respObj.getString("job");
                    editor.putString("token",token);
                    editor.apply();
//                    editor.putString("token", token);
//                    editor.commit();
                    String name = preferences.getString("token", "");
                    Toast.makeText(firstpage.this,resp+" - "+name,Toast.LENGTH_LONG).show();

                    // on below line we are setting this string s to our text view.
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }, new com.android.volley.Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                // method to handle errors.
                Toast.makeText(firstpage.this,  "" + error, Toast.LENGTH_SHORT).show();
                System.out.println(error);
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                // below line we are creating a map for
                // storing our values in key and value pair.
                Map<String, String> params = new HashMap<String, String>();

                // on below line we are passing our key
                // and value pair to our parameters.
                params.put("email", String.valueOf(ip_email.getText()));
                params.put("password", String.valueOf(ip_password.getText()));

                // at last we are
                // returning our params.
                return params;
            }
        };
        // below line is to make
        // a json object request.
        queue.add(request);

    }

}