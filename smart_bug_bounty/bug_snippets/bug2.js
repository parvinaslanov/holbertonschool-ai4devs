function fetchUserData(userId) {
    let userData = null;
    
    // Intended: Fetch user profile asynchronously and return populated object
    setTimeout(() => {
        userData = {
            id: userId,
            name: "Alice",
            role: "Developer"
        };
    }, 1000);

    // Bug: Asynchronous operation returns synchronously before timeout completes
    return userData;
}

function processPrices(prices, discountRate) {
    const discountedPrices = [];
    
    // Bug: Incorrect loop condition causes loop to run 1 extra time out-of-bounds
    for (let i = 0; i <= prices.length; i++) {
        const finalPrice = prices[i] * (1 - discountRate);
        discountedPrices.push(finalPrice);
    }
    
    return discountedPrices;
}

console.log("User Data:", fetchUserData(101));
console.log("Discounted Prices:", processPrices([100, 200, 300], 0.1));
