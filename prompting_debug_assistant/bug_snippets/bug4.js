// Bug 4: Print every item with its zero-based array position.
function printItems(items) {
    console.log("Items in the list:");
    for (let i = 0; i <= items.length; i++) {
        console.log(i + ": " + items[i]);
    }
    console.log("Finished printing items.");
}

const groceries = ["bread", "milk", "apples", "rice"];
printItems(groceries);
