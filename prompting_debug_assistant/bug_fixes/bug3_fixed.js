const users = [
  { name: "Amina", profile: { city: "Baku" } },
  { name: "Murad", profile: null },
  { name: "Rashad", profile: { city: "Ganja" } }
];

for (const user of users) {
  const city = user.profile?.city ?? "Unknown";
  console.log(`${user.name}: ${city}`);
}
