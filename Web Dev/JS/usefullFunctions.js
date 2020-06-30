

function searchCountryJSON(data){
  // data:
  // [
  //   { "name": "my Name", "id": 12, "type": "car owner" },
  //   { "name": "my Name2", "id": 13, "type": "car owner2" },
  //   { "name": "my Name4", "id": 14, "type": "car owner3" },
  //   { "name": "my Name4", "id": 15, "type": "car owner5" }
  // ]
  var results = [];
  var searchField = "name";
  var searchVal = "my name";
  for (var i = 0; i < data.length; i++) {
    if (data[i][searchField] == searchVal) {
      results.push(data[i]);
    }
  }
  console.log(results[0].TotalConfirmed)
  return results[0]
}