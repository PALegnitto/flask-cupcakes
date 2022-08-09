"use strict";

let list = document.getElementById("#cupcakes");

async function getCupcakes() {
  let response = await axios.get("/api/cupcakes");
  console.log("got", response);
  return response.data; //returns response object
}

function cupcakeOnPage() {
  let response = getCupcakes();

  $("#cupcakes").html(response.data);

}
