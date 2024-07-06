const BASE_URL = "http://localhost:5000/api";

function createCupcakeHTML(cupcake){
  let cupcakeHTML = `
      <div id='${cupcake.id}' >
        <img src='${cupcake.image}' class="card-img-top" alt="...">
        <li>Flavor: ${cupcake.flavor}</li>
        <li>Size: ${cupcake.size}</li>
        <li>Rating: ${cupcake.rating}</li>
        <button class="btn btn-danger">Delete</button>
      </div>`

  $("#cupcakes-list").append(cupcakeHTML);
}

async function displayCupcakes(){
  const response = await axios.get(`${BASE_URL}/cupcakes`);
  for (let cupcake of response.data.cupcakes){
    let cupcakeList = createCupcakeHTML(cupcake);
    $("#cupcake-list").append(cupcakeList);
  }
}

$("#cupcake-form").on("submit", async function (e) {
  e.preventDefault();

  const cupcakeData = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
    image: $("#image").val()
  };

  const response = await axios.post(`${BASE_URL}/cupcakes`, cupcakeData);
  createCupcakeHTML(response.data.cupcake);
  $("#cupcake-list").append(cupcakeList);
  $("#cupcake-form").trigger("reset");
  

});

$("#cupcakes-list").on("click", "button", async function (e) {
  e.preventDefault();
  let $cupcake = $(e.target).closest("div");
  let cupcakeId = $cupcake.attr("id");

  await axios.delete(`/api/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});

displayCupcakes();




