// Bug 4: Print every item in an array with its position
function printItems(items) {
    for (let i = 0; i <= items.length; i++) {
        console.log(i + ": " + items[i]);
    }
}

const groceries = ["bread", "milk", "apples", "rice"];
printItems(groceries);
