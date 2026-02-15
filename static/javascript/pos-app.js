const items = {{ items | tojson }}

var cart = [['snag', 3.5, 1], ['drink', 2, 1]];

function updateCart() {
    let html = "";
    var orderTotal = 0;
    for (let i = 0; i < cart.length; i++) {
        let total = cart[i][1] * cart[i][2];
        orderTotal += total;
        html += '<tr> <td>' + cart[i][0] + '</td> <td>' + '$' + total +
            '</td></tr><tr><td colspan="2">' + cart[i][1] + '  x' + cart[i][2] + '</td></tr>'
    }
    document.getElementById("cart").innerHTML = html
    document.getElementById("totalDisplay").textContent = '$' + orderTotal

}

function addToCart() {

}