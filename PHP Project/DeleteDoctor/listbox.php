<!--
    Title:  Doctor listbox
    name: Michael Cullen
    Student id: C00261635
    Date: 20/03/2023
    Purpose: listbox for all doctors that aare not deleted
-->

<?php
include '../../assets/php/db_connection.php';

$sql = "SELECT * FROM Doctor WHERE deleted = false";

if(!$result = mysqli_query($conn, $sql)){
    die("Error in query " . mysqli_error($conn));
}

echo "<br><select name = 'listbox' id = 'listbox' onclick = 'populate()'>";

while ($row = mysqli_fetch_array($result)) {
    $id = $row['doctorID'];
    $firstName = $row['firstName'];
    $lastName = $row['lastName'];
    $surgAddress = $row['surgeryAddress'];
    $surgPhone = $row['surgeryTelephone'];
    $mobPhone = $row['mobileNumber'];
    $homeAddress = $row['homeAddress'];
    $homePhone = $row['homeTelephone'];

    $all = "$id+ $firstName+ $lastName+ $surgAddress+ $surgPhone+ $mobPhone+ $homeAddress+ $homePhone";
    echo "<option value= '$all'> Dr. $lastName </option>";
}

echo "</select>";
mysqli_close($conn);
?>
