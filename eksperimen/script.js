// Generate random flowers on the screen
const container = document.querySelector(".flower-container");

function generateRandomFlower() {
  const flower = document.createElement("div");
  flower.className = "flower";

  const randomSize = Math.random() * 50 + 20;
  flower.style.borderBottomWidth = `${randomSize}px`;
  flower.style.borderLeftWidth = `${randomSize / 2}px`;
  flower.style.borderRightWidth = `${randomSize / 2}px`;

  const randomPositionX = Math.random() * window.innerWidth;
  const randomPositionY = Math.random() * window.innerHeight;
  flower.style.transform = `translate(${randomPositionX}px, ${randomPositionY}px)`;

  container.appendChild(flower);

  // Remove the flower after it's out of view
  flower.addEventListener("animationiteration", () => {
    container.removeChild(flower);
  });
}

// Generate flowers every 2 seconds
setInterval(generateRandomFlower, 2000);
