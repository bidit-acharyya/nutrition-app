function addToLog(meal){
    var food = document.getElementById("name").textContent;
    var calories = document.getElementById("cals").textContent;

    var logTable = document.getElementById(meal);
    var newRow = logTable.insertRow(-1);

    var foodSlot = newRow.insertCell(0);
    var calsSlot = newRow.insertCell(1);

    foodSlot.innerHtml = food;
    calsSlot.innerHtml = cals;
    //window.location.href = "log.html";
}