// Bug 3: Convert each user's name to uppercase safely.
function getDisplayName(user) {
    return user.profile.name.toUpperCase();
}

const users = [
    { profile: { name: "Amina" } },
    { profile: null },
    { profile: { name: "Rashad" } }
];

users.forEach((user) => {
    const displayName = getDisplayName(user);
    console.log(displayName);
});
