package com.example.police;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class Search extends AppCompatActivity {
    //
    private static final int CAMERA_REQUEST = 1888;
    private ImageView imageView;
    private static final int MY_CAMERA_PERMISSION_CODE = 100;
    ActivityResultLauncher<Intent> activityResultLauncher;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
//        ActivityResultLauncher<Intent> someActivityResultLauncher = registerForActivityResult(
//                new ActivityResultContracts.StartActivityForResult(),
//                new ActivityResultCallback<ActivityResult>() {
//                    @Override
//                    public void onActivityResult(ActivityResult result) {
//                        if (result.getResultCode() == Activity.RESULT_OK) {
//                            // There are no request codes
//                            Intent data = result.getData();
//                            Uri uri = data.getData();
//                            ImageView imageView = findViewById(R.id.personPhoto);
//                            imageView.setImageURI(uri);
//                        }
//                    }
//                });
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        ImageView take_photo = findViewById(R.id.take_photo);
        imageView = findViewById(R.id.imgV);
        TextView t = findViewById(R.id.textView5);
        TextView t2 = findViewById(R.id.textView6);



        findViewById(R.id.btn_searchh).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Bitmap largeIcon = BitmapFactory.decodeResource(getResources(), R.drawable.img);
                imageView.setImageBitmap(largeIcon);
                t.setText("Match Found");
                t2.setText("Ruthveek Dessai");
            }
        });
        activityResultLauncher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(), new ActivityResultCallback<ActivityResult>() {
            @Override
            public void onActivityResult(ActivityResult result) {
                if (result.getResultCode() == RESULT_OK && result.getData()!=null) {
                    Bitmap photo = (Bitmap) result.getData().getExtras().get("data");
                    take_photo.setImageBitmap(photo);
                    Bitmap largeIcon = BitmapFactory.decodeResource(getResources(), R.drawable.img);
                    imageView.setImageBitmap(largeIcon);
                    t.setText("Match Found");
                    t2.setText("Ruthveek Dessai");
                }
            }
        });
        take_photo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

//                if(ContextCompat.checkSelfPermission(SearchActivity.this,Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED){
//                    ActivityCompat.requestPermissions(SearchActivity.this,new String[]{
//                            Manifest.permission.CAMERA
//                    },100);
//                }
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                    if (checkSelfPermission(Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED)
                    {
                        requestPermissions(new String[]{Manifest.permission.CAMERA}, MY_CAMERA_PERMISSION_CODE);
                    }
                    else
                    {
//                         Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
//                         startActivityForResult(cameraIntent, CAMERA_REQUEST);
                        Intent takePicture = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
                        if(takePicture.resolveActivity(getPackageManager())!=null){
                            activityResultLauncher.launch(takePicture);
                        }
                        else {
                            Toast.makeText(Search.this,"Not app that supports this action",Toast.LENGTH_LONG).show();
                        }
//                         takePicture.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
//                         startActivityForResult(takePicture, CAMERA_REQUEST);
                    }
                }
            }
        });
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults)
    {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == MY_CAMERA_PERMISSION_CODE)
        {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED)
            {
                Toast.makeText(this, "camera permission granted", Toast.LENGTH_LONG).show();
                Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(cameraIntent, CAMERA_REQUEST);
            }
            else
            {
                Toast.makeText(this, "camera permission denied", Toast.LENGTH_LONG).show();
            }
        }
    }
//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//        if (requestCode == CAMERA_REQUEST && resultCode == Activity.RESULT_OK) {
//            Bitmap photo = (Bitmap) data.getExtras().get("data");
//            take_photo.setImageBitmap(photo);
//        }
//    }

}