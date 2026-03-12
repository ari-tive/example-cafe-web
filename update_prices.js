const fs = require('fs');
const path = require('path');

const baseDir = __dirname;
const menuFile = path.join(baseDir, 'menu.html');

let content = fs.readFileSync(menuFile, 'utf-8');

// Replace all occurrences of ₹<number>
content = content.replace(/₹(\d+)/g, (match, p1) => {
    let currentPrice = parseInt(p1, 10);
    // Reduce by 50%
    let newPrice = Math.floor(currentPrice / 2);
    // Subtract 1 to end in 9 (if newPrice > 0)
    if (newPrice > 0) {
        newPrice -= 1;
    }
    return `₹${newPrice}`;
});

fs.writeFileSync(menuFile, content, 'utf-8');
console.log("Prices successfully updated to 50% off - 1 format.");
