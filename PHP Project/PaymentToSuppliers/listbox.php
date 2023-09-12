<!--
    Title:  supplier listbox
    name: Michael Cullen
    Student id: C00261635
    Date: 20/03/2023
    Purpose: listbox for all suppliers that aare not deleted
-->

<?php
    include '../../assets/php/db_connection.php';

    $sql = ("SELECT * FROM Suppliers WHERE deleted = 0");
    // selects all non deleted suppliers

    if(!$result = mysqli_query($conn, $sql)){
        die("Error in query " . mysqli_error($conn));
    }

    echo "<br><select name = 'listbox' id = 'listbox' onclick = 'populate()'>";

    while ($row = $result->fetch_assoc()) {
        $id = $row['supplierID'];
        $name = $row['supplierName'];
        $address = $row['address'];
        $email = $row['email'];
        $website = $row['website'];
        $telephone = $row['telephone'];
        $infoString = $id . "|" . $name . "|" . $address . "|" . $email . "|" . $website . "|" . $telephone;
        echo "<option value=\"$infoString\">$name</option>";
    }

    echo "</select>";
    mysqli_close($conn);
?>