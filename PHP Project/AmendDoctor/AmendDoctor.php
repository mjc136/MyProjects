<!--
    Title:  Doctor amend
    name: Michael Cullen
    Student id: C00261635
    Date: 20/03/2023
    Purpose: UJpdates details in doctor table
-->

<?php 
    include '../../assets/php/db_connection.php';
    // updates doctor as id entered
    $sql = "UPDATE Doctor SET firstName = '$_POST[amendFirstname]', 
    lastName = '$_POST[amendSurname]', 
    surgeryAddress = '$_POST[amendSurgAddress]', 
    surgeryTelephone = '$_POST[amendSurgPhone]', 
    mobileNumber = '$_POST[amendPhone]', 
    homeAddress = '$_POST[amendAddress]',
    homeTelephone = '$_POST[amendHomePhone]' WHERE doctorID = '$_POST[amendid]'";

    if(!mysqli_query($conn, $sql)){
        echo "Error in query " . mysqli_error($conn);
    }
    else{
        if(mysqli_affected_rows($conn) != 0){
            echo mysqli_affected_rows($conn) . " record(s) updated <br>";
            echo "Dr. " .  $_POST['amendSurname'];
        }
        else{
            echo "No records updated";
        }
    }
    mysqli_close($conn);

    ?>

    <form action = "AmendDoctor.html.php" method = "post">
    <input type = "submit" value = "Return to previous page">
</form>