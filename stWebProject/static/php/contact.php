<?php
    $name= $_POST['name'];
    $email= $_POST['email'];
    $message= $_POST['message'];

    $email_from = 'sleekTiki Interactive Site';
    $email_subject = 'New Message From Site';
    $email_body = "Name: $name.\n".
                  "Email: $email.\n".
                  "Message: $message.\n";
     $to ="mboard76#gmail.com";
     $headers = "From: $email.from \r\n";
     $header .= "Reply-To: $email.from \r\n";

     mail($to,$email_subject,$email_body,$headers);

     header("location: home.html");
?>