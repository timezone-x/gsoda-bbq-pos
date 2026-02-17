var cart = {};
let items = [];
document.addEventListener("DOMContentLoaded", loadPricing);


function updateCart() {
    let html = "";
    var orderTotal = 0;
    for (let key in cart) {
        const item = cart[key]
        const lineTotal = item.price * item.qty;
        orderTotal += lineTotal;
        html += `
                <tr>
                    <td>${key}</td>
                    <td>$${lineTotal.toFixed(2)}</td>
                </tr>
                <tr>
                    <td colspan="2">$${item.price.toFixed(2)} x ${item.qty}</td>
                </tr>
        `;
    }
    document.getElementById("cart").innerHTML = html
    document.getElementById("totalDisplay").textContent = 'Total: $' + orderTotal.toFixed(2);

}

function addToCart() {
    const id = event.target.id;
    for (let i = 0; i < items.length; i++) {
        let tempName = items[i].name;
        console.log(tempName);
        if (tempName == id) {
            var item = items[i];
            break;
        }

    }
    if (id in cart) {
        cart[id].qty++;
    }
    else {
        cart[id] = {
            price: item.price,
            qty: 1
        };
    }
    updateCart();

}

async function fetchPricing() {
    const response = await fetch('/api/items');
    const data = await response.json();
    return data;
}

async function loadPricing() {
    items = await fetchPricing();
    console.table(items);
}

function clearCart() {
    cart = []
    updateCart();
}