// Bug 3: Find a user's display name safely
function getDisplayName(user) {
    return user.profile.name.toUpperCase();
}

const users = [
    { profile: { name: "Amina" } },
    { profile: null },
    { profile: { name: "Rashad" } }
];

users.forEach((user) => {
    console.log(getDisplayName(user));
});
