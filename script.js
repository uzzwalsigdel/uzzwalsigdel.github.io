document.getElementById("year").textContent = new Date().getFullYear();

const root = document.documentElement;

// Theme toggle (persisted)
document.querySelector(".theme-toggle").addEventListener("click", () => {
  const next = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = next;
  localStorage.setItem("theme", next);
});

// Mobile menu
const burger = document.querySelector(".burger");
const menu = document.querySelector(".menu");
burger.addEventListener("click", () => {
  const open = menu.classList.toggle("open");
  burger.setAttribute("aria-expanded", open);
});
menu.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => {
    menu.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
  })
);

// Scroll progress bar
const bar = document.querySelector(".progress");
let ticking = false;
const onScroll = () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
    ticking = false;
  });
};
addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Typewriter headline. Every character is laid out up front and only faded in,
// so the text never reflows or jumps while typing.
const typer = document.querySelector(".typewrite");
if (typer && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const chars = [];
  const walk = (node) => {
    [...node.childNodes].forEach((n) => {
      if (n.nodeType === Node.TEXT_NODE) {
        const frag = document.createDocumentFragment();
        for (const c of n.textContent) {
          const s = document.createElement("span");
          s.className = "ch";
          s.textContent = c;
          s.setAttribute("aria-hidden", "true");
          frag.appendChild(s);
          chars.push(s);
        }
        n.replaceWith(frag);
      } else if (n.nodeType === Node.ELEMENT_NODE && n.tagName !== "BR") {
        walk(n);
      }
    });
  };
  walk(typer);
  typer.classList.add("typing");

  // A parent's background-clip:text gradient ignores child opacity, so the name
  // would show before it is typed. Give each letter its own slice of the gradient.
  const grad = typer.querySelector(".grad");
  if (grad) {
    const gchars = [...grad.querySelectorAll(".ch")];
    const paint = () => {
      const w = grad.offsetWidth;
      gchars.forEach((s) => {
        s.style.backgroundSize = `${w}px 100%`;
        s.style.backgroundPosition = `${grad.offsetLeft - s.offsetLeft}px 0`;
      });
    };
    paint();
    addEventListener("resize", paint);
    document.fonts?.ready.then(paint);
  }

  let i = 0;
  const next = () => {
    if (i > 0) chars[i - 1].classList.remove("cur");
    if (i >= chars.length) {
      chars[chars.length - 1].classList.add("cur", "done");
      return;
    }
    const c = chars[i++];
    c.classList.add("on", "cur");
    const pause = /[,.]/.test(c.textContent) ? 260 : c.textContent === " " ? 40 : 55;
    setTimeout(next, pause + (chars[i]?.closest("em") && !c.closest("em") ? 300 : 0));
  };
  setTimeout(next, 400);
}

// Reveal on scroll
const io = new IntersectionObserver(
  (entries) =>
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add("visible");
      io.unobserve(e.target);
    }),
  { threshold: 0, rootMargin: "0px 0px -8% 0px" }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

// Highlight the nav link for the section in view
const links = [...menu.querySelectorAll("a")];
const spy = new IntersectionObserver(
  (entries) =>
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      links.forEach((l) => l.classList.toggle("active", l.getAttribute("href") === "#" + e.target.id));
    }),
  { rootMargin: "-45% 0px -50% 0px" }
);
document.querySelectorAll("main section[id]").forEach((s) => spy.observe(s));
