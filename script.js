document.getElementById("year").textContent = new Date().getFullYear();

// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".nav nav");
toggle.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});
nav.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => nav.classList.remove("open"))
);

// Scroll reveal
const observer = new IntersectionObserver(
  (entries) =>
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("visible");
        observer.unobserve(e.target);
      }
    }),
  { threshold: 0.15 }
);
document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

// Typing effect
const typed = document.querySelector(".typed");
const words = typed.dataset.words.split("|");
let w = 0, i = words[0].length, deleting = true;
function tick() {
  const word = words[w];
  typed.textContent = word.slice(0, i);
  if (deleting) {
    i--;
    if (i < 0) { deleting = false; w = (w + 1) % words.length; i = 0; }
  } else {
    i++;
    if (i > words[w].length) { deleting = true; i = words[w].length; setTimeout(tick, 1600); return; }
  }
  setTimeout(tick, deleting ? 60 : 110);
}
if (!matchMedia("(prefers-reduced-motion: reduce)").matches) setTimeout(tick, 1600);
