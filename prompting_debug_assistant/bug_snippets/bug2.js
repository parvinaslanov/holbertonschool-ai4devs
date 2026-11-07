function getFirstNItems(items, n) {
    /**
     * Intended Behavior: Return the first n items from an array.
     * Issue Type: Off-by-one loop logic issue
     */
    let result = [];
    
    // Bug: Uses '<=' instead of '<', causing an out-of-bounds issue
    for (let i = 0; i <= n; i++) {
        if (i < items.length) {
            result.push(items[i]);
        }
    }
    return result;
}
