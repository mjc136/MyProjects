<!--
    Title:  Doctor insert
    name: Michael Cullen
    Student id: C00261635
    Date: 20/03/2023
    Purpose: enter details doctor table
-->


<?php
include '../../assets/php/db_connection.php';

date_default_timezone_set ("UTC");

$sql = "SELECT MAX(doctorID) AS id FROM Doctor";

$result = mysqli_query($conn, $sql);
while($row = mysqli_fetch_array($result)){
    $id = $row['id'];
}
$id = $id + 1;
// enters details into the table
$sql = "Insert into Doctor(doctorID, firstName, lastName, surgeryAddress, surgeryTelephone, mobileNumber, homeAddress, homeTelephone)
VALUES ($id, '$_POST[firstname]','$_POST[surname]','$_POST[surgAddress]','$_POST[surgPhone]','$_POST[phone]','$_POST[address]','$_POST[homePhone]')";

if (!mysqli_query($conn, $sql) ){ 
    die ("An Error in the SQL Query: " . mysqli_error($conn));
}

echo "<br>A record has been added for Dr. " . $_POST['surname'];

mysqli_close($conn);

?>
<form action = "DoctorInsert.html.php" method = "post">
    <input type = "submit" value = "Return to previous page">
</form>
